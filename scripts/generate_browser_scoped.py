#!/usr/bin/env python3
"""Generate browser-scoped binding classes from AST of src/kernel/resources/browsers/**."""
# pyright: reportUnknownParameterType=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false, reportUndefinedVariable=false, reportUnusedVariable=false

from __future__ import annotations

import ast
from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class IdBinding:
    kind: str  # "positional" | "kwonly"


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _browsers_root() -> Path:
    return _repo_root() / "src/kernel/resources/browsers"


def _iter_browser_py_files() -> list[Path]:
    root = _browsers_root()
    out: list[Path] = []
    for p in sorted(root.rglob("*.py")):
        if p.name in ("__init__.py", "browsers.py"):
            continue
        out.append(p)
    return out


def _is_resource_class(node: ast.ClassDef) -> bool:
    if not node.name.endswith("Resource"):
        return False
    if node.name.startswith("Async"):
        return False
    if "With" in node.name:
        return False
    for b in node.bases:
        if isinstance(b, ast.Name) and b.id == "SyncAPIResource":
            return True
        if isinstance(b, ast.Attribute) and b.attr == "SyncAPIResource":
            return True
    return False


def _is_async_resource_class(node: ast.ClassDef) -> bool:
    if not node.name.startswith("Async") or not node.name.endswith("Resource"):
        return False
    if "With" in node.name:
        return False
    for b in node.bases:
        if isinstance(b, ast.Name) and b.id == "AsyncAPIResource":
            return True
        if isinstance(b, ast.Attribute) and b.attr == "AsyncAPIResource":
            return True
    return False


def _async_resource_name(sync_name: str) -> str:
    if sync_name.startswith("Async"):
        return sync_name
    return f"Async{sync_name}"


def _has_cached_property_decorator(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    for d in node.decorator_list:
        if isinstance(d, ast.Name) and d.id == "cached_property":
            return True
        if isinstance(d, ast.Attribute) and d.attr == "cached_property":
            return True
    return False


def _annotation_root_name(node: ast.AST | None) -> str | None:
    if node is None:
        return None
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Subscript):
        return _annotation_root_name(node.value)
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return _annotation_root_name(node.left) or _annotation_root_name(node.right)
    return None


def _find_id_binding(arguments: ast.arguments) -> IdBinding | None:
    pos = list(arguments.posonlyargs) + list(arguments.args)
    if len(pos) > 0 and pos[0].arg == "self":
        rest = pos[1:]
    else:
        rest = pos
    for a in rest:
        if a.arg == "id":
            return IdBinding("positional")
    for a in arguments.kwonlyargs:
        if a.arg == "id":
            return IdBinding("kwonly")
    return None


def _strip_id_from_arguments(arguments: ast.arguments) -> ast.arguments:
    """Remove `id` from positional and keyword-only parameters; fix defaults tail."""

    posonly = list(arguments.posonlyargs)
    pos = list(arguments.args)
    combined = posonly + pos
    defaults = list(arguments.defaults or [])
    nd = len(defaults)

    kept: list[tuple[ast.arg, ast.expr | None, str]] = []
    for i, a in enumerate(combined):
        if a.arg == "id":
            continue
        d: ast.expr | None = None
        if nd and i >= len(combined) - nd:
            d = defaults[i - (len(combined) - nd)]
        kind = "posonly" if i < len(posonly) else "pos"
        kept.append((a, d, kind))

    new_posonly = [a for a, _d, k in kept if k == "posonly"]
    new_pos = [a for a, _d, k in kept if k == "pos"]
    new_combined = new_posonly + new_pos
    new_defaults_list = [d for a, d, k in kept if d is not None]
    new_nd = len(new_defaults_list)
    if new_nd > len(new_combined):
        raise RuntimeError("invalid defaults after strip")
    new_defaults = new_defaults_list[-new_nd:] if new_nd else []

    kwonly = [a for a in arguments.kwonlyargs if a.arg != "id"]
    kw_defaults_old = list(arguments.kw_defaults or [])
    new_kw_defaults: list[ast.expr | None] = []
    for i, a in enumerate(arguments.kwonlyargs):
        d = kw_defaults_old[i] if i < len(kw_defaults_old) else None
        if a.arg != "id":
            new_kw_defaults.append(d)

    return ast.arguments(
        posonlyargs=new_posonly,
        args=new_pos,
        kwonlyargs=kwonly,
        kw_defaults=new_kw_defaults,
        defaults=new_defaults,
        vararg=arguments.vararg,
        kwarg=arguments.kwarg,
    )


def _public_signature(inner: ast.FunctionDef | ast.AsyncFunctionDef) -> ast.arguments:
    if _find_id_binding(inner.args) is None:
        return inner.args
    return _strip_id_from_arguments(inner.args)


def _without_leading_self(arguments: ast.arguments) -> ast.arguments:
    """Drop `self` from positional args for use in subclass method signatures (posonly unused here)."""

    if arguments.posonlyargs:
        raise RuntimeError("positional-only parameters are not supported for browser binding generation")
    args = list(arguments.args)
    defaults = list(arguments.defaults or [])
    if not args or args[0].arg != "self":
        raise RuntimeError("expected leading self parameter")
    new_args = args[1:]
    n_old = len(args)
    n_new = len(new_args)
    nd = len(defaults)
    if nd:
        if nd > n_old:
            raise RuntimeError("too many defaults")
        new_defaults = defaults[-min(nd, n_new) :] if n_new else []
    else:
        new_defaults = []
    return ast.arguments(
        posonlyargs=[],
        args=new_args,
        kwonlyargs=list(arguments.kwonlyargs),
        kw_defaults=list(arguments.kw_defaults or []),
        defaults=new_defaults,
        vararg=arguments.vararg,
        kwarg=arguments.kwarg,
    )


def _emit_call_forward(inner_name: str, inner: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    binding = _find_id_binding(inner.args)
    pos_all = list(inner.args.posonlyargs) + list(inner.args.args)
    if not pos_all or pos_all[0].arg != "self":
        raise RuntimeError(f"expected self first on {inner_name}")
    rest_pos = pos_all[1:]

    pos_call: list[str] = []
    for a in rest_pos:
        if a.arg == "id":
            pos_call.append("self._session_id")
        else:
            pos_call.append(a.arg)

    kw_parts: list[str] = []
    for a in inner.args.kwonlyargs:
        if a.arg == "id":
            kw_parts.append("id=self._session_id")
        else:
            kw_parts.append(f"{a.arg}={a.arg}")

    if inner.args.vararg is not None or inner.args.kwarg is not None:
        raise RuntimeError(f"unsupported vararg/kwarg on {inner_name}")

    if binding is None:
        inner_pos = ", ".join(a.arg for a in rest_pos)
        inner_kw = ", ".join(f"{a.arg}={a.arg}" for a in inner.args.kwonlyargs)
        bits = [inner_pos] if inner_pos else []
        if inner_kw:
            bits.append(inner_kw)
        return f"self._inner.{inner_name}({', '.join(bits)})"

    return f"self._inner.{inner_name}({', '.join([*pos_call, *kw_parts])})"


def _emit_method(
    inner: ast.FunctionDef | ast.AsyncFunctionDef,
    *,
    is_async: bool,
) -> str | None:
    if inner.name.startswith("_"):
        return None
    if _has_cached_property_decorator(inner):
        return None

    binding = _find_id_binding(inner.args)
    if binding is None:
        return None

    pub_args = _without_leading_self(_public_signature(inner))
    ret = inner.returns
    ret_s = "" if ret is None else f" -> {ast.unparse(ret)}"
    prefix = "async def" if is_async else "def"
    await_kw = "await " if is_async else ""
    body = f"return {await_kw}{_emit_call_forward(inner.name, inner)}"

    args_s = ast.unparse(pub_args)
    if args_s.startswith("(") and args_s.endswith(")"):
        inner_args = args_s[1:-1].strip()
    else:
        inner_args = args_s.strip()
    if inner_args:
        sig_inner = f"self, {inner_args}"
    else:
        sig_inner = "self"

    lines = [f"    {prefix} {inner.name}({sig_inner}){ret_s}:", f"        {body}"]
    return "\n".join(lines)


def _bound_class_name(sync_cls: str) -> str:
    return f"Bound{sync_cls}"


def _import_line_for_class(file_path: Path, class_name: str) -> str:
    rel = file_path.relative_to(_repo_root() / "src/kernel")
    mod = ".".join(rel.with_suffix("").parts)
    return f"from ...{mod} import {class_name}"


def _discover_nested_subresources(sync_class: ast.ClassDef) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for node in sync_class.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not _has_cached_property_decorator(node):
            continue
        if node.name.startswith("with_"):
            continue
        root = _annotation_root_name(node.returns)
        if root is None:
            continue
        if not root.endswith("Resource") or root.startswith("Async"):
            continue
        if "With" in root:
            continue
        out.append((node.name, root))
    return out


def _collect_sync_resource_classes(tree: ast.Module) -> dict[str, ast.ClassDef]:
    out: dict[str, ast.ClassDef] = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and _is_resource_class(node):
            out[node.name] = node
    return out


def _collect_async_resource_classes(tree: ast.Module) -> dict[str, ast.ClassDef]:
    out: dict[str, ast.ClassDef] = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and _is_async_resource_class(node):
            out[node.name] = node
    return out


def _emit_bound_class_pair(
    sync_name: str,
    sync_cls: ast.ClassDef,
    async_cls: ast.ClassDef | None,
    nested: dict[str, list[tuple[str, str]]],
) -> str:
    bound = _bound_class_name(sync_name)
    lines: list[str] = [
        f"class {bound}(ScopedResourceProxy):",
        '    """Session id is injected for browser API methods."""',
    ]

    for prop_name, inner_cls in nested.get(sync_name, []):
        ib = _bound_class_name(inner_cls)
        imp = _import_line_for_class(_class_file(inner_cls), inner_cls)
        lines.append("    @cached_property")
        lines.append(f"    def {prop_name}(self) -> {ib}:")
        lines.append(f"        {imp}")
        lines.append(f"        return {ib}({inner_cls}(self._inner._client), self._session_id)")
        lines.append("")

    for node in sync_cls.body:
        if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
            chunk = _emit_method(node, is_async=False)
            if chunk:
                lines.append(chunk)
                lines.append("")

    if async_cls is not None:
        an = _async_resource_name(sync_name)
        bound_a = _bound_class_name(an)
        lines.append("")
        lines.append(f"class {bound_a}(ScopedResourceProxy):")
        lines.append('    """Async variant: session id is injected for browser API methods."""')

        for prop_name, inner_cls in nested.get(sync_name, []):
            ainner = _async_resource_name(inner_cls)
            ib = _bound_class_name(ainner)
            imp = _import_line_for_class(_class_file(inner_cls), ainner)
            lines.append("    @cached_property")
            lines.append(f"    def {prop_name}(self) -> {ib}:")
            lines.append(f"        {imp}")
            lines.append(f"        return {ib}({ainner}(self._inner._client), self._session_id)")
            lines.append("")

        for node in async_cls.body:
            if isinstance(node, ast.AsyncFunctionDef) and not node.name.startswith("_"):
                chunk = _emit_method(node, is_async=True)
                if chunk:
                    lines.append(chunk)
                    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


_class_file_cache: dict[str, Path] = {}


def _index_classes_by_name() -> None:
    global _class_file_cache
    _class_file_cache = {}
    for path in _iter_browser_py_files():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for name in _collect_sync_resource_classes(tree):
            _class_file_cache[name] = path
        for name in _collect_async_resource_classes(tree):
            _class_file_cache[name] = path


def _class_file(class_name: str) -> Path:
    return _class_file_cache[class_name]


def _nested_map() -> dict[str, list[tuple[str, str]]]:
    nested: dict[str, list[tuple[str, str]]] = {}
    for path in _iter_browser_py_files():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for name, cls in _collect_sync_resource_classes(tree).items():
            pairs = _discover_nested_subresources(cls)
            if pairs:
                nested[name] = pairs
    return nested


def _browsers_py_path() -> Path:
    return _browsers_root() / "browsers.py"


def _cached_property_resource_subresources(cls: ast.ClassDef) -> dict[str, str]:
    """prop_name -> sync Resource class name for @cached_property -> XResource style members."""

    out: dict[str, str] = {}
    for node in cls.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        if not _has_cached_property_decorator(node):
            continue
        if node.name.startswith("with_"):
            continue
        root = _annotation_root_name(node.returns)
        if root is None:
            continue
        if "With" in root or not root.endswith("Resource"):
            continue
        if root.startswith("Async"):
            continue
        out[node.name] = root
    return out


def _facade_entries_from_browsers_py() -> list[tuple[str, str]]:
    """Top-level browser subresources from `BrowsersResource` / `AsyncBrowsersResource` (AST)."""

    path = _browsers_py_path()
    tree = ast.parse(path.read_text(encoding="utf-8"))
    sync_cls: ast.ClassDef | None = None
    async_cls: ast.ClassDef | None = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "BrowsersResource":
            sync_cls = node
        elif isinstance(node, ast.ClassDef) and node.name == "AsyncBrowsersResource":
            async_cls = node
    if sync_cls is None or async_cls is None:
        raise RuntimeError(f"expected BrowsersResource and AsyncBrowsersResource in {path}")

    sync_map = _cached_property_resource_subresources(sync_cls)
    async_map: dict[str, str] = {}
    for node in async_cls.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        if not _has_cached_property_decorator(node):
            continue
        if node.name.startswith("with_"):
            continue
        root = _annotation_root_name(node.returns)
        if root is None or "With" in root:
            continue
        if not (root.startswith("Async") and root.endswith("Resource")):
            continue
        async_map[node.name] = root

    if set(sync_map) != set(async_map):
        raise RuntimeError(
            "BrowsersResource vs AsyncBrowsersResource cached_property session resources mismatch: "
            f"sync={sorted(sync_map)!r} async={sorted(async_map)!r}"
        )

    for prop in sorted(sync_map):
        expected = _async_resource_name(sync_map[prop])
        got = async_map[prop]
        if got != expected:
            raise RuntimeError(f"{path}: property {prop!r}: expected async return {expected!r}, got {got!r}")

    return sorted(sync_map.items(), key=lambda t: t[0])


def _emit_facade_mixins(entries: list[tuple[str, str]]) -> str:
    lines: list[str] = [
        "class BrowserScopedFacadeMixin:",
        '    """Top-level browser session subresources (sync); uses `_http` and `session_id`."""',
        "",
        "    _http: Any",
        "    session_id: str",
        "",
    ]
    for prop, sync_cls in entries:
        bound = _bound_class_name(sync_cls)
        imp = _import_line_for_class(_class_file(sync_cls), sync_cls)
        lines.append("    @cached_property")
        lines.append(f"    def {prop}(self) -> {bound}:")
        lines.append(f"        {imp}")
        lines.append(f"        return {bound}({sync_cls}(self._http), self.session_id)")
        lines.append("")

    lines.extend(
        [
            "",
            "class AsyncBrowserScopedFacadeMixin:",
            '    """Top-level browser session subresources (async); uses `_http` and `session_id`."""',
            "",
            "    _http: Any",
            "    session_id: str",
            "",
        ]
    )
    for prop, sync_cls in entries:
        async_cls = _async_resource_name(sync_cls)
        bound = _bound_class_name(async_cls)
        imp = _import_line_for_class(_class_file(sync_cls), async_cls)
        lines.append("    @cached_property")
        lines.append(f"    def {prop}(self) -> {bound}:")
        lines.append(f"        {imp}")
        lines.append(f"        return {bound}({async_cls}(self._http), self.session_id)")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _generation_order(all_sync: list[str], nested: dict[str, list[tuple[str, str]]]) -> list[str]:
    deps: dict[str, set[str]] = {c: set() for c in all_sync}
    for parent, pairs in nested.items():
        for _, inner in pairs:
            deps.setdefault(parent, set()).add(inner)

    ordered: list[str] = []
    remaining = set(all_sync)
    while remaining:
        ready = sorted([c for c in remaining if not (deps.get(c, set()) & remaining)])
        if not ready:
            raise RuntimeError(f"cycle in nested resources: {remaining}")
        for c in ready:
            ordered.append(c)
            remaining.remove(c)
    return ordered


def _path_to_module(path: Path) -> str:
    src = _repo_root() / "src"
    rel = path.resolve().relative_to(src)
    return ".".join(rel.with_suffix("").parts)


def _import_from_to_absolute(module_file: Path, imp: ast.ImportFrom) -> ast.ImportFrom:
    level = imp.level or 0
    if level == 0:
        return imp
    cur = _path_to_module(module_file)
    pkg = ".".join(cur.split(".")[:-1])
    if level > 1:
        pkg_parts = pkg.split(".")
        up = level - 1
        if len(pkg_parts) < up:
            raise ValueError(f"cannot resolve import {ast.dump(imp)} from {module_file}")
        pkg = ".".join(pkg_parts[:-up])
    if imp.module:
        base = f"{pkg}.{imp.module}"
    else:
        base = pkg
    return ast.ImportFrom(module=base, names=imp.names, level=0)


def _imports_from_resource_modules(paths: Iterable[Path]) -> list[str]:
    """Collect imports from resource modules, rewritten as absolute `kernel.*` paths."""

    def skip_line(line: str) -> bool:
        if "from __future__ import annotations" in line:
            return True
        if "kernel._resource import" in line:
            return True
        if "kernel._utils import" in line:
            return True
        if "kernel._base_client import" in line:
            return True
        if "kernel._compat import cached_property" in line:
            return True
        return False

    seen: set[str] = set()
    lines: list[str] = []
    for path in sorted({p.resolve() for p in paths}):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, ast.ImportFrom):
                node = _import_from_to_absolute(path, node)
                line = ast.unparse(node)
            elif isinstance(node, ast.Import):
                line = ast.unparse(node)
            else:
                continue
            if skip_line(line):
                continue
            if line not in seen:
                seen.add(line)
                lines.append(line)
    return lines


def _emit_module() -> str:
    _index_classes_by_name()
    nested = _nested_map()
    all_sync = sorted(n for n in _class_file_cache if not n.startswith("Async"))
    order = _generation_order(all_sync, nested)

    resource_paths = {_class_file_cache[name] for name in all_sync}
    import_lines = _imports_from_resource_modules(resource_paths)

    parts: list[str] = [
        "# Code generated by scripts/generate_browser_scoped.py. DO NOT EDIT.",
        "# ruff: noqa: I001, F401",
        "# pyright: reportUnusedImport=false",
        '"""Browser-scoped wrappers over generated `resources.browsers` classes (AST-driven)."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from ..._compat import cached_property",
        "from .util import ScopedResourceProxy",
    ]
    if import_lines:
        parts.append("")
        parts.extend(import_lines)
    parts.append("")

    for sync_name in order:
        path = _class_file_cache[sync_name]
        tree = ast.parse(path.read_text(encoding="utf-8"))
        sync_cls = _collect_sync_resource_classes(tree)[sync_name]
        async_name = _async_resource_name(sync_name)
        async_cls = _collect_async_resource_classes(tree).get(async_name)
        parts.append(_emit_bound_class_pair(sync_name, sync_cls, async_cls, nested))
        parts.append("")

    facade_entries = _facade_entries_from_browsers_py()
    for _prop, sync_cls in facade_entries:
        if sync_cls not in _class_file_cache:
            raise RuntimeError(f"facade references unknown resource class {sync_cls!r}")
    parts.append(_emit_facade_mixins(facade_entries))
    parts.append("")

    export_names: list[str] = []
    for sync_name in sorted(all_sync):
        export_names.append(_bound_class_name(sync_name))
        an = _async_resource_name(sync_name)
        if an in _class_file_cache and an != sync_name:
            export_names.append(_bound_class_name(an))

    parts.append("__all__ = [")
    for n in sorted(set(export_names)):
        parts.append(f'    "{n}",')
    parts.append("]")
    parts.append("")
    return "\n".join(parts)


def main() -> int:
    out = _repo_root() / "src/kernel/lib/browser_scoped/generated_bindings.py"
    text = _emit_module()
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {out} ({len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
