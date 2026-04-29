# Changelog

## 0.52.0 (2026-04-29)

Full Changelog: [v0.51.0...v0.52.0](https://github.com/kernel/kernel-python-sdk/compare/v0.51.0...v0.52.0)

### Features

* profile download: 409 for empty profile + surface API errors in dashboard ([fd0c20e](https://github.com/kernel/kernel-python-sdk/commit/fd0c20eb17f0a6df382672c34830a81fac9217d9))
* support setting headers via env ([37dda88](https://github.com/kernel/kernel-python-sdk/commit/37dda88a1f88fdf4bd8da615cbb6be1aadae3f41))


### Bug Fixes

* use correct field name format for multipart file arrays ([663f0a8](https://github.com/kernel/kernel-python-sdk/commit/663f0a8a633fd5b0f5f8b65ed169c4d780251e1d))


### Documentation

* annotate response with httpx.Response in browser routing example ([0dfa1fb](https://github.com/kernel/kernel-python-sdk/commit/0dfa1fb978da1c4fd474840ae8664f027e1feb39))
* print buffered body and mention httpx.Response semantics ([84cb2e3](https://github.com/kernel/kernel-python-sdk/commit/84cb2e38486f330635487ed049d692f7c9716a1f))
* show both raw streaming and buffered curl in routing example ([407e748](https://github.com/kernel/kernel-python-sdk/commit/407e74862f99db13320ea6c02a8752759d4de60a))
* simplify browser routing example ([58b0ee2](https://github.com/kernel/kernel-python-sdk/commit/58b0ee27cdac1f4021c6e333f8157318c838ec56))

## 0.51.0 (2026-04-25)

Full Changelog: [v0.50.0...v0.51.0](https://github.com/kernel/kernel-python-sdk/compare/v0.50.0...v0.51.0)

### Features

* add browser-scoped session client ([7ca6887](https://github.com/kernel/kernel-python-sdk/commit/7ca68877e7011bb83862b7cc810a20d8254ea7dd))
* Expire stuck IN_PROGRESS managed auth sessions via background worker ([7781a3b](https://github.com/kernel/kernel-python-sdk/commit/7781a3b4635ded02dea60adf85878f50f7b7fb27))
* Expose browser_session_id on managed auth connection ([0ccb507](https://github.com/kernel/kernel-python-sdk/commit/0ccb50744032b4c31e0575fa7b06fb20503c8f55))
* generate browser-scoped resource bindings ([53b17c8](https://github.com/kernel/kernel-python-sdk/commit/53b17c8241cc71261d1e96f5929cbd4f05b2064b))


### Bug Fixes

* address python browser routing ci follow-ups ([9690923](https://github.com/kernel/kernel-python-sdk/commit/9690923666cfe07de76267eee050d7743a8bad6f))
* evict deleted browser routes ([a873a18](https://github.com/kernel/kernel-python-sdk/commit/a873a18eba3f36937dc177ab981372e395722f8b))
* finish python browser routing cleanup ([694907a](https://github.com/kernel/kernel-python-sdk/commit/694907ab3419477e7058b85a7365ac4cce941105))
* normalize browser route cache session IDs ([f4c247b](https://github.com/kernel/kernel-python-sdk/commit/f4c247b425680b54d0ce3c7738fb82313bca7918))
* normalize python browser request string bodies ([3ce80e7](https://github.com/kernel/kernel-python-sdk/commit/3ce80e767d373b638ba1c2959bf18bf999629db0))
* quiet generator-script pyright noise ([0bdf85e](https://github.com/kernel/kernel-python-sdk/commit/0bdf85e0c38d4813056b61599273e88c7a64713a))
* reserve internal browser request query params ([b2c7aac](https://github.com/kernel/kernel-python-sdk/commit/b2c7aacac09a1bb7680cf493e9985438b169286c))
* satisfy browser-scoped lint checks ([8e8dde2](https://github.com/kernel/kernel-python-sdk/commit/8e8dde241c8817944baaacd155fe196f200868e8))
* satisfy generated browser-scoped type checks ([b410245](https://github.com/kernel/kernel-python-sdk/commit/b410245e1ad4bf8e29c17c59a5931654567b141f))
* sniff browser pool route cache updates ([5328730](https://github.com/kernel/kernel-python-sdk/commit/532873072f0400029768d1b7cf54b9fb1428ada9))
* type-check browser-scoped helpers ([cfff5b4](https://github.com/kernel/kernel-python-sdk/commit/cfff5b4c3635d327dd1ac0779d4e17e395efbec0))


### Chores

* fix browser-scoped test import order ([fc34859](https://github.com/kernel/kernel-python-sdk/commit/fc34859c4f60f84038b425d9930c512e58134dea))
* **internal:** more robust bootstrap script ([6c9cdf3](https://github.com/kernel/kernel-python-sdk/commit/6c9cdf3ce828fab358c7e060f4e3313408cad257))
* keep browser-scoped generator lint clean ([a80716b](https://github.com/kernel/kernel-python-sdk/commit/a80716b791bf1f707aa7869290c47caefb0d9e27))


### Documentation

* flesh out browser-scoped example ([ca5d188](https://github.com/kernel/kernel-python-sdk/commit/ca5d1884b590634df5623945e9585e0a66228ec3))


### Refactors

* clean up python browser routing diff ([622f844](https://github.com/kernel/kernel-python-sdk/commit/622f8448a8a32f00b41d6e4890bfaf0a9374bd3e))
* drop browser-scoped wrapper clients ([dba503e](https://github.com/kernel/kernel-python-sdk/commit/dba503e832d54aa8d462d3d74b3027f8a9e865b6))
* inline browser resource passthrough returns ([02a2f59](https://github.com/kernel/kernel-python-sdk/commit/02a2f595c7e76ae7f0cea2ec1e88075df3a25be1))
* move python browser routing rollout to env ([0647d5c](https://github.com/kernel/kernel-python-sdk/commit/0647d5cab166e680bcb3436d1b502c3215492400))
* rename browser routing subresources config ([3ae9dab](https://github.com/kernel/kernel-python-sdk/commit/3ae9dab6b841e6f1191cdde073e36696f97feb39))
* simplify browser routing cache ([de0476f](https://github.com/kernel/kernel-python-sdk/commit/de0476fc043df48a58dd4067bb4b3c0fe7a83f0e))
* sniff browser routes in response hooks ([563de7d](https://github.com/kernel/kernel-python-sdk/commit/563de7d0ac8f141320edb060b4671935808e473a))

## 0.50.0 (2026-04-20)

Full Changelog: [v0.49.0...v0.50.0](https://github.com/kernel/kernel-python-sdk/compare/v0.49.0...v0.50.0)

### Features

* add POST /browsers/{id}/curl and /curl/raw endpoints ([e91bc38](https://github.com/kernel/kernel-python-sdk/commit/e91bc387e5ef74c1b02f62e19e9ae31867296af4))
* remove paid plan gating from project endpoints ([284c2d4](https://github.com/kernel/kernel-python-sdk/commit/284c2d434be9d098efbaf33b14b416acd4c78e18))


### Bug Fixes

* ensure file data are only sent as 1 parameter ([e566aa5](https://github.com/kernel/kernel-python-sdk/commit/e566aa50a9022d5b284c6334b3704df2a96643cc))
* include MFA and sign-in options in CUA SSO-only step response ([ea9576b](https://github.com/kernel/kernel-python-sdk/commit/ea9576b87a17b903f880ab8d14379b8ca5fe53d5))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([d46c711](https://github.com/kernel/kernel-python-sdk/commit/d46c711588904a9e249a0e852a790c3431d12aa1))

## 0.49.0 (2026-04-10)

Full Changelog: [v0.48.0...v0.49.0](https://github.com/kernel/kernel-python-sdk/compare/v0.48.0...v0.49.0)

### Features

* Neil/kernel 1180 fuzzy matching for browser pools ([4089baf](https://github.com/kernel/kernel-python-sdk/commit/4089bafcec6fe6029b0b3730767e7428e2ab6e07))
* Raise replay framerate limit from 20 to 60 fps ([707b339](https://github.com/kernel/kernel-python-sdk/commit/707b3398f435ebaf1a801e6310e2c827b1766e82))

## 0.48.0 (2026-04-10)

Full Changelog: [v0.47.0...v0.48.0](https://github.com/kernel/kernel-python-sdk/compare/v0.47.0...v0.48.0)

### Features

* [kernel-1116] add base_url field to browser session response ([335d9e0](https://github.com/kernel/kernel-python-sdk/commit/335d9e04998dd9e581f47d8869dd7f07a8f2db74))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([6dfd882](https://github.com/kernel/kernel-python-sdk/commit/6dfd8826b84ed191d72ac114df986c398fa83c5c))


### Chores

* retrigger Stainless codegen for projects resource ([ca22fd9](https://github.com/kernel/kernel-python-sdk/commit/ca22fd9dc4b5f4cd70e15ecb1ddd3607d8a99df8))

## 0.47.0 (2026-04-07)

Full Changelog: [v0.46.0...v0.47.0](https://github.com/kernel/kernel-python-sdk/compare/v0.46.0...v0.47.0)

### Features

* Include login_url in managed auth connection response ([b97b320](https://github.com/kernel/kernel-python-sdk/commit/b97b3203c612f3883d7d08d6f3f6282ce726ec59))

## 0.46.0 (2026-04-06)

Full Changelog: [v0.45.0...v0.46.0](https://github.com/kernel/kernel-python-sdk/compare/v0.45.0...v0.46.0)

### Features

* Add optional url parameter to proxy check endpoint ([cdd4b02](https://github.com/kernel/kernel-python-sdk/commit/cdd4b026fc01b1118cbc35cbc61890d15af3e021))

## 0.45.0 (2026-03-30)

Full Changelog: [v0.44.0...v0.45.0](https://github.com/kernel/kernel-python-sdk/compare/v0.44.0...v0.45.0)

### Features

* [kernel-1008] browser pools add custom policy ([09f8520](https://github.com/kernel/kernel-python-sdk/commit/09f85209bc3c646d8a2a1231ed3925cad830f3dc))
* Add disable_default_proxy for stealth browsers ([3a75e81](https://github.com/kernel/kernel-python-sdk/commit/3a75e819e6e7caffdfba74a9627ed418de247de7))
* **internal:** implement indices array format for query and form serialization ([c798c39](https://github.com/kernel/kernel-python-sdk/commit/c798c39251def1447d61215c187f0e285f225f3d))


### Chores

* **ci:** skip lint on metadata-only changes ([f0815a8](https://github.com/kernel/kernel-python-sdk/commit/f0815a8d36799444220552cb599a19b79c9b5e12))
* **internal:** update gitignore ([34b47ab](https://github.com/kernel/kernel-python-sdk/commit/34b47ab40aeb12ad9f78e923493caaca88a554b4))

## 0.44.0 (2026-03-20)

Full Changelog: [v0.43.0...v0.44.0](https://github.com/kernel/kernel-python-sdk/compare/v0.43.0...v0.44.0)

### Features

* Add GPU viewport presets and GPU encoder defaults ([0735b45](https://github.com/kernel/kernel-python-sdk/commit/0735b45fc92950cef3afea92a879712ea0ebdf0f))
* Adds description to OAS spec for docs about delta_x, delta_y ([9841aac](https://github.com/kernel/kernel-python-sdk/commit/9841aac21588beb0c6a22baf5c5b0bf8e8cdd024))
* Drop headless GPU support and disable pooling ([cda8f94](https://github.com/kernel/kernel-python-sdk/commit/cda8f94f6cebabc3b3b6f95aff765816255a9270))
* Enhance managed authentication with CUA support and new features ([ece76c2](https://github.com/kernel/kernel-python-sdk/commit/ece76c2f7d2a20af7c00988d161c4e275623aaac))
* expose smooth drag mouse movement via public API ([c6f6862](https://github.com/kernel/kernel-python-sdk/commit/c6f6862d03620bb218a99c85431e384c5c8e5e4c))
* Rename hardware acceleration UI/docs wording to GPU acceleration ([9ee4d0c](https://github.com/kernel/kernel-python-sdk/commit/9ee4d0c080da7f649a3bde63640593f33d5d0f6b))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([fd55947](https://github.com/kernel/kernel-python-sdk/commit/fd55947f1776b43cca804622d0c771ebe99ead60))
* **pydantic:** do not pass `by_alias` unless set ([a815a82](https://github.com/kernel/kernel-python-sdk/commit/a815a8237cce2098b2f5d6a8ad5def400d418fbb))
* sanitize endpoint path params ([9b55d2b](https://github.com/kernel/kernel-python-sdk/commit/9b55d2be9472f779fe20d7d863dacae1030d2b49))


### Chores

* **internal:** tweak CI branches ([8781c7d](https://github.com/kernel/kernel-python-sdk/commit/8781c7d9aa8759e487e5d86cbb82bfb7eb3d314e))

## 0.43.0 (2026-03-10)

Full Changelog: [v0.42.1...v0.43.0](https://github.com/kernel/kernel-python-sdk/compare/v0.42.1...v0.43.0)

### Features

* Add webdriver_ws_url and metro webdriver session proxy ([66c7364](https://github.com/kernel/kernel-python-sdk/commit/66c73649f84a3e481672ba876b6882bd79069f16))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([52a392c](https://github.com/kernel/kernel-python-sdk/commit/52a392ca2bca701c3c1136fad0ef0d09f526918a))
* update placeholder string ([6e71435](https://github.com/kernel/kernel-python-sdk/commit/6e71435500ee1eca1b243e73e0dfd316343ca21e))

## 0.42.1 (2026-03-05)

Full Changelog: [v0.42.0...v0.42.1](https://github.com/kernel/kernel-python-sdk/compare/v0.42.0...v0.42.1)

### Features

* [kernel-1028] add api clipboard support ([077a61c](https://github.com/kernel/kernel-python-sdk/commit/077a61c3c3f287eaddd3f90cf4f5cf04dc7baf39))
* add force flag to viewport resize to bypass live view/recording check ([c4b8c62](https://github.com/kernel/kernel-python-sdk/commit/c4b8c62622354859847c13234ee9f54611f4175f))
* expose smooth mouse movement via public API ([8b3db28](https://github.com/kernel/kernel-python-sdk/commit/8b3db281a64cafba5dac7effdc264f30a94c38ea))


### Chores

* **internal:** codegen related update ([e9265c4](https://github.com/kernel/kernel-python-sdk/commit/e9265c4ffba59e8cfd8a02e12653b83a471aced3))

## 0.42.0 (2026-03-02)

Full Changelog: [v0.41.0...v0.42.0](https://github.com/kernel/kernel-python-sdk/compare/v0.41.0...v0.42.0)

### Features

* Neil/kernel 1052 deployments list endpoint ([45ba6bb](https://github.com/kernel/kernel-python-sdk/commit/45ba6bbba291e9cca45a30c8ba2b1fb57f1f10bb))

## 0.41.0 (2026-02-27)

Full Changelog: [v0.40.0...v0.41.0](https://github.com/kernel/kernel-python-sdk/compare/v0.40.0...v0.41.0)

### Features

* Return uptime_ms for deleted browser sessions ([067207f](https://github.com/kernel/kernel-python-sdk/commit/067207fb709eb78064118d6d71fdb390ff9e31e8))

## 0.40.0 (2026-02-26)

Full Changelog: [v0.39.0...v0.40.0](https://github.com/kernel/kernel-python-sdk/compare/v0.39.0...v0.40.0)

### Features

* show pool browsers in dashboard and API ([fb8d38c](https://github.com/kernel/kernel-python-sdk/commit/fb8d38c8dff3795a549f20f66723d0df1947ae64))

## 0.39.0 (2026-02-25)

Full Changelog: [v0.38.0...v0.39.0](https://github.com/kernel/kernel-python-sdk/compare/v0.38.0...v0.39.0)

### Features

* Add proxy hostname bypass hosts ([24905be](https://github.com/kernel/kernel-python-sdk/commit/24905be21884e5ecefe9e1f631fff271052b5268))

## 0.38.0 (2026-02-25)

Full Changelog: [v0.37.0...v0.38.0](https://github.com/kernel/kernel-python-sdk/compare/v0.37.0...v0.38.0)

### Features

* Neil/kernel 1029 past session search ([657da45](https://github.com/kernel/kernel-python-sdk/commit/657da45a969b52a8497efbcd597fe8b705dab370))


### Chores

* **internal:** add request options to SSE classes ([6287415](https://github.com/kernel/kernel-python-sdk/commit/628741509bbaf2b693afc71cc28ad82a8dc7b231))
* **internal:** make `test_proxy_environment_variables` more resilient ([3345fc6](https://github.com/kernel/kernel-python-sdk/commit/3345fc63467e18401a501a6df0b71dae46f70113))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([6a629ee](https://github.com/kernel/kernel-python-sdk/commit/6a629ee6e943bac9b87154ac440c760765185206))

## 0.37.0 (2026-02-23)

Full Changelog: [v0.36.1...v0.37.0](https://github.com/kernel/kernel-python-sdk/compare/v0.36.1...v0.37.0)

### Features

* Neil/kernel 1017 profile pagination query parameter ([fc068ec](https://github.com/kernel/kernel-python-sdk/commit/fc068ec7dc7b4bbed0d11322f52b49065e7680fd))

## 0.36.1 (2026-02-21)

Full Changelog: [v0.36.0...v0.36.1](https://github.com/kernel/kernel-python-sdk/compare/v0.36.0...v0.36.1)

### Features

* Add version filter to GET /deployments endpoint ([b4cb1ac](https://github.com/kernel/kernel-python-sdk/commit/b4cb1ac6658900c71fb75e16a54da3ad96113eec))

## 0.36.0 (2026-02-21)

Full Changelog: [v0.35.0...v0.36.0](https://github.com/kernel/kernel-python-sdk/compare/v0.35.0...v0.36.0)

### Features

* Add DELETE /deployments/{id} API endpoint ([509a49c](https://github.com/kernel/kernel-python-sdk/commit/509a49ca1ffd55f92309de62cefcc60a1d0fa84c))


### Chores

* **internal:** remove mock server code ([0d315e0](https://github.com/kernel/kernel-python-sdk/commit/0d315e0393c991fc96fc89ddba2792d2abb984c6))
* **test:** update skip reason message ([78129c9](https://github.com/kernel/kernel-python-sdk/commit/78129c999887442f99ca6442a46626ba475a85d0))
* update mock server docs ([e545bce](https://github.com/kernel/kernel-python-sdk/commit/e545bced8ac751eac0dc8c5e7b800d9b06d6d35a))

## 0.35.0 (2026-02-18)

Full Changelog: [v0.34.0...v0.35.0](https://github.com/kernel/kernel-python-sdk/compare/v0.34.0...v0.35.0)

### Features

* GPU pools ([a417ea7](https://github.com/kernel/kernel-python-sdk/commit/a417ea79722eb78dd7b425cf515485f3b18af5b4))

## 0.34.0 (2026-02-18)

Full Changelog: [v0.33.0...v0.34.0](https://github.com/kernel/kernel-python-sdk/compare/v0.33.0...v0.34.0)

### Features

* Add error_code field to ManagedAuthSession and related components ([9d160d7](https://github.com/kernel/kernel-python-sdk/commit/9d160d798b25fc5416a2cce84b2ad8e2fc46f801))
* Allow arbitrary viewport dimensions ([6463d9f](https://github.com/kernel/kernel-python-sdk/commit/6463d9fdb94477867d82fd69630688878c79b182))
* Neil/kernel 873 templates v4 ([c376f63](https://github.com/kernel/kernel-python-sdk/commit/c376f635abf0500b7aa7c40e721255d88e4e4381))


### Chores

* format all `api.md` files ([c4ea333](https://github.com/kernel/kernel-python-sdk/commit/c4ea333ede664dbaa38911b1f97310e0b8a9618f))
* **internal:** fix lint error on Python 3.14 ([96a4f24](https://github.com/kernel/kernel-python-sdk/commit/96a4f241bdf8dffe57c91140bf33f54a2c21a223))

## 0.33.0 (2026-02-11)

Full Changelog: [v0.32.0...v0.33.0](https://github.com/kernel/kernel-python-sdk/compare/v0.32.0...v0.33.0)

### Features

* **auth:** add save_credentials support ([be702dc](https://github.com/kernel/kernel-python-sdk/commit/be702dc9f39f5b4c0424ec29cc4a51c1e0e5773e))
* **auth:** plan-based min health check intervals ([3f6e730](https://github.com/kernel/kernel-python-sdk/commit/3f6e7302524074fa51885551f22f7866874f4f8f))
* Browser API endpoint grouping ([25054a8](https://github.com/kernel/kernel-python-sdk/commit/25054a8a77d7c9964133f545339526243f049469))


### Chores

* **internal:** bump dependencies ([8e144ab](https://github.com/kernel/kernel-python-sdk/commit/8e144ab2740f5d9161123840296f3d8809b0a79d))


### Refactors

* **api:** remove deprecated agent-auth endpoints from stainless.… ([4f7f783](https://github.com/kernel/kernel-python-sdk/commit/4f7f7830489ea83488b06f9723a8e5f472c1ccd4))
* **auth:** simplify proxy configuration in OpenAPI schema ([9a615e4](https://github.com/kernel/kernel-python-sdk/commit/9a615e45804402ce12064c1b078d631197a04585))

## 0.32.0 (2026-02-07)

Full Changelog: [v0.31.1...v0.32.0](https://github.com/kernel/kernel-python-sdk/compare/v0.31.1...v0.32.0)

### Features

* **auth:** add reauth circuit breaker logic ([b65b6b6](https://github.com/kernel/kernel-python-sdk/commit/b65b6b6dc5cf0b0fdbe08bb1010970143c7e3b85))

## 0.31.1 (2026-02-06)

Full Changelog: [v0.31.0...v0.31.1](https://github.com/kernel/kernel-python-sdk/compare/v0.31.0...v0.31.1)

### Chores

* add Managed Auth API planning doc ([f24a387](https://github.com/kernel/kernel-python-sdk/commit/f24a387432ff8e506c143da566e65d5674c7ff6c))

## 0.31.0 (2026-02-06)

Full Changelog: [v0.30.0...v0.31.0](https://github.com/kernel/kernel-python-sdk/compare/v0.30.0...v0.31.0)

### Features

* add batch computer action proxy endpoint ([f316e9b](https://github.com/kernel/kernel-python-sdk/commit/f316e9bf1a47e982af7af6ed8a4e8f701baf50b9))

## 0.30.0 (2026-02-03)

Full Changelog: [v0.29.0...v0.30.0](https://github.com/kernel/kernel-python-sdk/compare/v0.29.0...v0.30.0)

### Features

* Neil/kernel 872 templates v3 ([383d071](https://github.com/kernel/kernel-python-sdk/commit/383d071b2dba88ec884c34ea8453b3c0e9c4a969))

## 0.29.0 (2026-01-30)

Full Changelog: [v0.28.0...v0.29.0](https://github.com/kernel/kernel-python-sdk/compare/v0.28.0...v0.29.0)

### Features

* add support for 1280x800@60 viewport ([1cb6575](https://github.com/kernel/kernel-python-sdk/commit/1cb65752f6aa45fcb2ca1dd55f0eebf9457abfa9))
* **client:** add custom JSON encoder for extended type support ([33604fe](https://github.com/kernel/kernel-python-sdk/commit/33604feb1a07bbca94477c28143052d5c6eff70d))


### Chores

* **ci:** upgrade `actions/github-script` ([4828aba](https://github.com/kernel/kernel-python-sdk/commit/4828aba4349e61686285b57358892825e75286be))

## 0.28.0 (2026-01-22)

Full Changelog: [v0.27.0...v0.28.0](https://github.com/kernel/kernel-python-sdk/compare/v0.27.0...v0.28.0)

### Features

* Allow hot loading profiles into sessions ([34b8809](https://github.com/kernel/kernel-python-sdk/commit/34b880972dcf2820eff77b32f739b4e621781a44))

## 0.27.0 (2026-01-21)

Full Changelog: [v0.26.0...v0.27.0](https://github.com/kernel/kernel-python-sdk/compare/v0.26.0...v0.27.0)

### Features

* **agent-auth:** add 1Password integration for credential providers ([b26d1a3](https://github.com/kernel/kernel-python-sdk/commit/b26d1a35dce7e8b76d916d7bbd869edb0c44c195))
* **dashboard:** add browser replays support for past browsers ([9d81781](https://github.com/kernel/kernel-python-sdk/commit/9d81781970ed6230844d479bc27893453b34a05e))
* Update browser pool org limits ([7fa6d9b](https://github.com/kernel/kernel-python-sdk/commit/7fa6d9b152e051ed7cbadb9b5760a525fdf1f3b2))


### Refactors

* **agentauth:** enhance discover and submit modules with improve… ([570df3a](https://github.com/kernel/kernel-python-sdk/commit/570df3a0cc4b4e48737729442885959e9bf205ba))

## 0.26.0 (2026-01-17)

Full Changelog: [v0.25.0...v0.26.0](https://github.com/kernel/kernel-python-sdk/compare/v0.25.0...v0.26.0)

### Features

* Auth agents auth check URL ([f9e1d38](https://github.com/kernel/kernel-python-sdk/commit/f9e1d38c4e42c1f3f340c8cc15a9311aa1b7f00c))


### Bug Fixes

* **stainless:** use @onkernel/sdk package name for TypeScript SDK ([b8c5cf1](https://github.com/kernel/kernel-python-sdk/commit/b8c5cf1ac94c4febfa41fd379485a60e39742cbc))


### Chores

* **internal:** update `actions/checkout` version ([54be5a5](https://github.com/kernel/kernel-python-sdk/commit/54be5a5b8d6c51b754a845c1a7d7467b89d50a66))

## 0.25.0 (2026-01-16)

Full Changelog: [v0.24.0...v0.25.0](https://github.com/kernel/kernel-python-sdk/compare/v0.24.0...v0.25.0)

### Features

* add MFA options to agent authentication workflow ([bee5904](https://github.com/kernel/kernel-python-sdk/commit/bee59044cb637362349258b9d4e4be3ecdbd344b))
* add WebSocket process attach and PTY support ([3882e32](https://github.com/kernel/kernel-python-sdk/commit/3882e3272b9df5c360212f4d729a9a811f59c809))
* **api:** add IP address logging for residential and custom proxies ([28f7c36](https://github.com/kernel/kernel-python-sdk/commit/28f7c3691edd8825d3e802cb0fc6142b7c6cb28e))
* **api:** manual updates ([820fa05](https://github.com/kernel/kernel-python-sdk/commit/820fa058d07891e1c201cef71ec4e5a6e31d024f))
* **api:** update production repos ([e041fef](https://github.com/kernel/kernel-python-sdk/commit/e041fef21a1b14504fef235e1b6b56bc91853550))
* **client:** add support for binary request streaming ([e73f276](https://github.com/kernel/kernel-python-sdk/commit/e73f276a0be37bcfedbbb964414f4c2290560b8a))
* Support hot swap proxy on a session ([d9dedd2](https://github.com/kernel/kernel-python-sdk/commit/d9dedd21e7211290daf9ee154c038a68b91c3e71))


### Chores

* sync repo ([729aba4](https://github.com/kernel/kernel-python-sdk/commit/729aba4fbc12aee3c63b67941a59dcc9c0d430a4))

## 0.24.0 (2025-12-17)

Full Changelog: [v0.23.0...v0.24.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.23.0...v0.24.0)

### Features

* Enhance AuthAgentInvocationCreateResponse to include already_authenti… ([2db6fed](https://github.com/onkernel/kernel-python-sdk/commit/2db6fed3d39462b8cbde477a8b396fbbde5c63f2))
* Fix browser pool sdk types ([6e0b8a3](https://github.com/onkernel/kernel-python-sdk/commit/6e0b8a39f8ca11297417479994e475c149155967))


### Chores

* **internal:** add missing files argument to base client ([1dce21b](https://github.com/onkernel/kernel-python-sdk/commit/1dce21b40ee87045724d9fbfd6f2ecd6da5ccb2e))
* speedup initial import ([74ccf15](https://github.com/onkernel/kernel-python-sdk/commit/74ccf15f4f7d3d9ab15b9cca92e5ec9f644780fb))

## 0.23.0 (2025-12-11)

Full Changelog: [v0.22.0...v0.23.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.22.0...v0.23.0)

### Features

* [wip] Browser pools polish pass ([2ba9e57](https://github.com/onkernel/kernel-python-sdk/commit/2ba9e5740d0b12605de3b48af06658b8db47ba11))
* enhance agent authentication API with new endpoints and request… ([84a794c](https://github.com/onkernel/kernel-python-sdk/commit/84a794c35f5a454b047d53b37867586f85e2536a))
* Enhance agent authentication with optional login page URL and auth ch… ([d7bd8a2](https://github.com/onkernel/kernel-python-sdk/commit/d7bd8a22d40243c043e14b899dd2006fc0d51a19))
* Enhance AuthAgent model with last_auth_check_at field ([169539a](https://github.com/onkernel/kernel-python-sdk/commit/169539a9b861b90f554b192dc8e457ad17a851a0))


### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([c8d571c](https://github.com/onkernel/kernel-python-sdk/commit/c8d571c785a4488549701aad525357a9fabec69f))


### Chores

* add missing docstrings ([75fa7cb](https://github.com/onkernel/kernel-python-sdk/commit/75fa7cb7b954f8a68cc5eb74ad3196b350e8f9dd))


### Refactors

* **browser:** remove persistence option UI ([57af2e1](https://github.com/onkernel/kernel-python-sdk/commit/57af2e181b716145ff3e11a0d74c04dd332f9e35))

## 0.22.0 (2025-12-05)

Full Changelog: [v0.21.0...v0.22.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.21.0...v0.22.0)

### Features

* Add `async_timeout_seconds` to PostInvocations ([2866021](https://github.com/onkernel/kernel-python-sdk/commit/286602193261f0d1beaad24dd633c3a1b0838654))


### Chores

* **docs:** use environment variables for authentication in code snippets ([eec0be5](https://github.com/onkernel/kernel-python-sdk/commit/eec0be59552f9057179b9597fc336fddd544d4b1))
* update lockfile ([ecee109](https://github.com/onkernel/kernel-python-sdk/commit/ecee109b4d10a786394c9807f82007849b7294d8))

## 0.21.0 (2025-12-02)

Full Changelog: [v0.20.0...v0.21.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.20.0...v0.21.0)

### Features

* Browser pools sdk release ([c2d7408](https://github.com/onkernel/kernel-python-sdk/commit/c2d7408a770ddd34902986015da0bfde3477f586))
* Mason/agent auth api ([b872928](https://github.com/onkernel/kernel-python-sdk/commit/b8729284ba804461749dad0ac4613aea3c6b3ce6))


### Bug Fixes

* ensure streams are always closed ([c82f496](https://github.com/onkernel/kernel-python-sdk/commit/c82f496ba0112b195f65da9498fb22ab65d501fb))


### Chores

* add Python 3.14 classifier and testing ([9a1e7bf](https://github.com/onkernel/kernel-python-sdk/commit/9a1e7bf9c92d64da4a151dd44cc60057c75c63bf))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([038b10d](https://github.com/onkernel/kernel-python-sdk/commit/038b10d52935961c37ebb0806e9b0754b4d53a20))

## 0.20.0 (2025-11-19)

Full Changelog: [v0.19.2...v0.20.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.19.2...v0.20.0)

### Features

* Add pagination to list browsers method and allow it to include deleted browsers when `include_deleted = true` ([0bf4d45](https://github.com/onkernel/kernel-python-sdk/commit/0bf4d4546171f7bc2fad9d225b7fcf2be14a6a71))

## 0.19.2 (2025-11-17)

Full Changelog: [v0.19.1...v0.19.2](https://github.com/onkernel/kernel-python-sdk/compare/v0.19.1...v0.19.2)

### Features

* Feat increase max timeout to 72h ([edaaa14](https://github.com/onkernel/kernel-python-sdk/commit/edaaa1445d9551393ce0e026d70ca565890d70cb))

## 0.19.1 (2025-11-13)

Full Changelog: [v0.19.0...v0.19.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.19.0...v0.19.1)

### Features

* Add support for 1200x800 ([1a8c6b5](https://github.com/onkernel/kernel-python-sdk/commit/1a8c6b5bbd91ddc2ab36b579f2fbd5552864259b))

## 0.19.0 (2025-11-12)

Full Changelog: [v0.18.0...v0.19.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.18.0...v0.19.0)

### Features

* feat hide cursor v2 ([5e694ae](https://github.com/onkernel/kernel-python-sdk/commit/5e694aedf67d142bcf2e4e4a018846236c45af69))
* Remove price gating on computer endpoints ([cbbdaee](https://github.com/onkernel/kernel-python-sdk/commit/cbbdaee2225d593a7abbe04e3bd768476d06340c))


### Bug Fixes

* compat with Python 3.14 ([297d7b3](https://github.com/onkernel/kernel-python-sdk/commit/297d7b3069073d8ea98e67abf123505b1b20b140))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([0e796f3](https://github.com/onkernel/kernel-python-sdk/commit/0e796f368e0eeb3260b3558e89fd26ec32b9567f))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([4d011fd](https://github.com/onkernel/kernel-python-sdk/commit/4d011fd41e10e5aaa49bb2447e27b71c8240e205))
* **internal:** grammar fix (it's -&gt; its) ([fcdf068](https://github.com/onkernel/kernel-python-sdk/commit/fcdf06877b370bf8c2abe047c5dcff7597dfadd9))
* **package:** drop Python 3.8 support ([5dcea22](https://github.com/onkernel/kernel-python-sdk/commit/5dcea220253de47542381b91401965198c3d3dd2))

## 0.18.0 (2025-10-30)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.17.0...v0.18.0)

### Features

* apps: add offset pagination + headers ([54ea6e7](https://github.com/onkernel/kernel-python-sdk/commit/54ea6e79ba21ba5ab33ab14a1bf257a95bf76bb8))


### Bug Fixes

* **client:** close streams without requiring full consumption ([4014c3d](https://github.com/onkernel/kernel-python-sdk/commit/4014c3d53c36627ecd702b8af272a382529aef55))

## 0.17.0 (2025-10-27)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.16.0...v0.17.0)

### Features

* Make country flag optional for DC and ISP proxies ([cd4c025](https://github.com/onkernel/kernel-python-sdk/commit/cd4c025b2e89cbc072a1779418ea1ef234b57026))

## 0.16.0 (2025-10-27)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.15.0...v0.16.0)

### Features

* ad hoc playwright code exec AP| ([4204ad5](https://github.com/onkernel/kernel-python-sdk/commit/4204ad587838ec90c3b54ca2eaf7d768da570a29))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([1130759](https://github.com/onkernel/kernel-python-sdk/commit/1130759ebc7eb511d8788332b59e84d0819f9715))

## 0.15.0 (2025-10-17)

Full Changelog: [v0.14.2...v0.15.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.14.2...v0.15.0)

### Features

* click mouse, move mouse, screenshot ([b63f7ad](https://github.com/onkernel/kernel-python-sdk/commit/b63f7adc7cf0da614a4fc3a9eed491f71f7ec742))
* Phani/deploy with GitHub url ([eb86c27](https://github.com/onkernel/kernel-python-sdk/commit/eb86c27107781172bf740e0af3833eee86b7cb60))

## 0.14.2 (2025-10-16)

Full Changelog: [v0.14.1...v0.14.2](https://github.com/onkernel/kernel-python-sdk/compare/v0.14.1...v0.14.2)

### Features

* Kiosk mode ([1bd1ed2](https://github.com/onkernel/kernel-python-sdk/commit/1bd1ed23b4bc120653e3fb13a670e8598f97d157))

## 0.14.1 (2025-10-13)

Full Changelog: [v0.14.0...v0.14.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.14.0...v0.14.1)

### Features

* Hide and deprecate mobile proxy type ([bee8d86](https://github.com/onkernel/kernel-python-sdk/commit/bee8d86588ce57de073583fa7e94a5ba38f21b9a))
* WIP: Configurable Viewport ([60b9961](https://github.com/onkernel/kernel-python-sdk/commit/60b99616dea9fa4ba823f58c2c18ea9dda60b836))


### Chores

* **internal:** detect missing future annotations with ruff ([b53927c](https://github.com/onkernel/kernel-python-sdk/commit/b53927c4013a34ad6afee95efe5608b56e34755a))

## 0.14.0 (2025-10-07)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.13.0...v0.14.0)

### Features

* WIP browser extensions ([89bac15](https://github.com/onkernel/kernel-python-sdk/commit/89bac15e58e4892e653a9dafeb2d15c88d7fdbb9))

## 0.13.0 (2025-10-03)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.12.0...v0.13.0)

### Features

* Http proxy ([2664172](https://github.com/onkernel/kernel-python-sdk/commit/266417290f174a560ad0f820a22efb3c2eb35a67))
* Update oAPI and data model for proxy status ([014d704](https://github.com/onkernel/kernel-python-sdk/commit/014d704dc98e19579c7a55a618c6e5e52a42edc6))

## 0.12.0 (2025-09-30)

Full Changelog: [v0.11.5...v0.12.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.11.5...v0.12.0)

### Features

* Return proxy ID in browsers response ([2beafcf](https://github.com/onkernel/kernel-python-sdk/commit/2beafcfbd8ee20e83616656b23587d67df9490a9))

## 0.11.5 (2025-09-29)

Full Changelog: [v0.11.4...v0.11.5](https://github.com/onkernel/kernel-python-sdk/compare/v0.11.4...v0.11.5)

### Features

* Add App Version to Invocation and add filtering on App Version ([c703d0b](https://github.com/onkernel/kernel-python-sdk/commit/c703d0bc7b785ff8118b3fc4cb80873c21b7640a))
* Fix my incorrect grammer ([22b2c11](https://github.com/onkernel/kernel-python-sdk/commit/22b2c1138d8739400edc27c245aa744a1d774ec6))

## 0.11.4 (2025-09-25)

Full Changelog: [v0.11.3...v0.11.4](https://github.com/onkernel/kernel-python-sdk/compare/v0.11.3...v0.11.4)

### Features

* getInvocations endpoint ([bb39872](https://github.com/onkernel/kernel-python-sdk/commit/bb39872703bd6ace1e588a54420f29a62140144b))

## 0.11.3 (2025-09-24)

Full Changelog: [v0.11.2...v0.11.3](https://github.com/onkernel/kernel-python-sdk/compare/v0.11.2...v0.11.3)

### Features

* Per Invocation Logs ([8c116b6](https://github.com/onkernel/kernel-python-sdk/commit/8c116b6e8590709dab14961b7e9c038229f5ace5))

## 0.11.2 (2025-09-24)

Full Changelog: [v0.11.1...v0.11.2](https://github.com/onkernel/kernel-python-sdk/compare/v0.11.1...v0.11.2)

### Features

* Add stainless CI ([9c8ccbf](https://github.com/onkernel/kernel-python-sdk/commit/9c8ccbfb59c6e7f9c5b649193ab10580d1d750e9))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([e7e72e6](https://github.com/onkernel/kernel-python-sdk/commit/e7e72e6642f7587af34f51608d3bde4112d1e711))
* improve example values ([2ecd936](https://github.com/onkernel/kernel-python-sdk/commit/2ecd936567bb98eda0edab68fb970668548bbc00))
* **internal:** update pydantic dependency ([45de860](https://github.com/onkernel/kernel-python-sdk/commit/45de860fb92aeeccf5ef44dcb2b5ab4a2b7a0592))
* **types:** change optional parameter type from NotGiven to Omit ([0b85104](https://github.com/onkernel/kernel-python-sdk/commit/0b85104d500907e1f86ad633403fb4c27fb929c4))

## 0.11.1 (2025-09-06)

Full Changelog: [v0.11.0...v0.11.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.11.0...v0.11.1)

### Features

* **api:** add pagination to the deployments endpoint ([e5838f5](https://github.com/onkernel/kernel-python-sdk/commit/e5838f51b9af325700b23d55ff2bb11b6ff3306e))
* **api:** pagination properties added to response (has_more, next_offset) ([5f2329f](https://github.com/onkernel/kernel-python-sdk/commit/5f2329f8712b9d1865cc95dcde06834fe65622ee))
* **api:** update API spec with pagination headers ([f64f55b](https://github.com/onkernel/kernel-python-sdk/commit/f64f55b00b0e0fa19dd2162cd914001381254314))


### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([4818d2d](https://github.com/onkernel/kernel-python-sdk/commit/4818d2d6084684529935c8e6b9b109516a1de373))
* **tests:** simplify `get_platform` test ([cd90a49](https://github.com/onkernel/kernel-python-sdk/commit/cd90a498d24b1f4490583bec64e5e670eb725197))

## 0.11.0 (2025-09-04)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.10.0...v0.11.0)

### Features

* **api:** adding support for browser profiles ([52bcaa1](https://github.com/onkernel/kernel-python-sdk/commit/52bcaa136a1792fd9a9d06f3f81a622a53a89e9a))
* improve future compat with pydantic v3 ([72b0862](https://github.com/onkernel/kernel-python-sdk/commit/72b086280f3742cf34ddb7afe2082c4eee37c80a))
* **types:** replace List[str] with SequenceNotStr in params ([688059b](https://github.com/onkernel/kernel-python-sdk/commit/688059b50a261e84fd1ae125b65a1bd56b6243d2))


### Chores

* **internal:** add Sequence related utils ([e833554](https://github.com/onkernel/kernel-python-sdk/commit/e833554e7f222acf915621d5f0fdd2eef17e0738))

## 0.10.0 (2025-08-27)

Full Changelog: [v0.9.1...v0.10.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.9.1...v0.10.0)

### Features

* **api:** new process, fs, and log endpoints ([48a39b4](https://github.com/onkernel/kernel-python-sdk/commit/48a39b4cc1ab32b4375ad4e33e5f9e4349502072))


### Bug Fixes

* avoid newer type syntax ([9ec7c40](https://github.com/onkernel/kernel-python-sdk/commit/9ec7c40b34b264709b904f36e309624bd1161413))


### Chores

* **internal:** change ci workflow machines ([3a2969d](https://github.com/onkernel/kernel-python-sdk/commit/3a2969d035b9e0bb4fa39dc27de2db6d4edad6dd))
* **internal:** update pyright exclude list ([39439aa](https://github.com/onkernel/kernel-python-sdk/commit/39439aaad72c92aa9f4bb74ac055b929c93b6060))
* update github action ([fff64d0](https://github.com/onkernel/kernel-python-sdk/commit/fff64d001d2c759967f08e7a1932e1fb7d84b126))

## 0.9.1 (2025-08-15)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.9.0...v0.9.1)

### Features

* **api:** add browser timeouts ([a89eff3](https://github.com/onkernel/kernel-python-sdk/commit/a89eff39afa75499d0efe2c54fe12a0a18cdf90e))

### Chores

* **internal:** codegen related update ([024c808](https://github.com/onkernel/kernel-python-sdk/commit/024c80865450277ca40433a7caaff078b5a25486))
* **internal:** update comment in script ([4279b99](https://github.com/onkernel/kernel-python-sdk/commit/4279b9927f99897dde36c07f5dc39ed2680ad261))
* update @stainless-api/prism-cli to v5.15.0 ([e78750e](https://github.com/onkernel/kernel-python-sdk/commit/e78750efdc419051c8db37ac89df111e81fa0401))

## 0.9.0 (2025-08-08)

Full Changelog: [v0.8.3...v0.9.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.8.3...v0.9.0)

### Features

* **api:** browser instance file i/o ([14667cd](https://github.com/onkernel/kernel-python-sdk/commit/14667cdfd06540585ffac570b8963b322cf9ef23))


### Chores

* **internal:** fix ruff target version ([07b55e4](https://github.com/onkernel/kernel-python-sdk/commit/07b55e4a4b65b403b3b6f69b95b221e2020cf30b))

## 0.8.3 (2025-08-01)

Full Changelog: [v0.8.2...v0.8.3](https://github.com/onkernel/kernel-python-sdk/compare/v0.8.2...v0.8.3)

### Features

* **api:** lower default timeout to 5s ([6d43e73](https://github.com/onkernel/kernel-python-sdk/commit/6d43e73a5206d3faa99825d6ee49986a5d5919aa))
* **api:** manual updates ([c6990ba](https://github.com/onkernel/kernel-python-sdk/commit/c6990ba5c9974f96270e1ca86e9d7935d7db03d7))
* **client:** support file upload requests ([79b06da](https://github.com/onkernel/kernel-python-sdk/commit/79b06da326192ceb5edf703576bd25835cbed031))


### Chores

* **project:** add settings file for vscode ([c46aa48](https://github.com/onkernel/kernel-python-sdk/commit/c46aa48e7d07db3317b038c51b3c58a88b2d44d4))

## 0.8.2 (2025-07-23)

Full Changelog: [v0.8.1...v0.8.2](https://github.com/onkernel/kernel-python-sdk/compare/v0.8.1...v0.8.2)

### Features

* **api:** add action name to the response to invoke ([1a485b2](https://github.com/onkernel/kernel-python-sdk/commit/1a485b2ddd3cdbf97fcb67f1d389c07ce0a51d8e))


### Bug Fixes

* **parsing:** ignore empty metadata ([d839a20](https://github.com/onkernel/kernel-python-sdk/commit/d839a20c1bb2c0e35aff6fa59196cec9e725d346))
* **parsing:** parse extra field types ([cb880bc](https://github.com/onkernel/kernel-python-sdk/commit/cb880bc6796acf8e44560580829229fb140586c9))

## 0.8.1 (2025-07-21)

Full Changelog: [v0.8.0...v0.8.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.8.0...v0.8.1)

### Chores

* **api:** remove deprecated endpoints ([348e40a](https://github.com/onkernel/kernel-python-sdk/commit/348e40a5f610769a5ec59d4f4e40b79d166cdf57))

## 0.8.0 (2025-07-16)

Full Changelog: [v0.7.1...v0.8.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.7.1...v0.8.0)

### Features

* **api:** manual updates ([cd2b694](https://github.com/onkernel/kernel-python-sdk/commit/cd2b694c97b354c4eab38ed06eba04bf56218f97))
* clean up environment call outs ([c31b1a2](https://github.com/onkernel/kernel-python-sdk/commit/c31b1a21a86381a5ee8162327e43934be4d661d2))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([b44aeee](https://github.com/onkernel/kernel-python-sdk/commit/b44aeee6397b8a418c65a624c71f8a2c5272fdc2))
* **parsing:** correctly handle nested discriminated unions ([7b25900](https://github.com/onkernel/kernel-python-sdk/commit/7b25900b5e12030c814231b1a212a95b090a977e))


### Chores

* **internal:** bump pinned h11 dep ([352aae2](https://github.com/onkernel/kernel-python-sdk/commit/352aae28c4cf9345c808910e13d7423613a6d80b))
* **package:** mark python 3.13 as supported ([5ddf6d0](https://github.com/onkernel/kernel-python-sdk/commit/5ddf6d0b28a8108a6e0f7de628438c33857cc6dc))
* **readme:** fix version rendering on pypi ([760753f](https://github.com/onkernel/kernel-python-sdk/commit/760753f31a974cac63ee5a8dc39462bbfb925249))

## 0.7.1 (2025-07-08)

Full Changelog: [v0.6.4...v0.7.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.6.4...v0.7.1)

### Features

* **api:** headless browsers ([de0b235](https://github.com/onkernel/kernel-python-sdk/commit/de0b235998be2299459b54df15e83dd9dc8c0b7f))
* **api:** manual updates ([7d0a2bd](https://github.com/onkernel/kernel-python-sdk/commit/7d0a2bd8dd25bac6d688e2b5f5076c916d80f800))


### Bug Fixes

* **ci:** correct conditional ([1167795](https://github.com/onkernel/kernel-python-sdk/commit/116779521b08014f5be7588f1e0a7975c13e8e05))


### Chores

* **ci:** change upload type ([dabede0](https://github.com/onkernel/kernel-python-sdk/commit/dabede0456032d69d0c4b05c740d04002fc900a9))
* **ci:** only run for pushes and fork pull requests ([e9a45fd](https://github.com/onkernel/kernel-python-sdk/commit/e9a45fd655812a9bf2c3edec3cccdbde3ab89f73))
* **internal:** codegen related update ([2c50b08](https://github.com/onkernel/kernel-python-sdk/commit/2c50b08edb7f73a7c20a459f2ffeb52f56583e5f))

## 0.6.4 (2025-06-27)

Full Changelog: [v0.6.3...v0.6.4](https://github.com/onkernel/kernel-python-sdk/compare/v0.6.3...v0.6.4)

### Features

* **api:** add GET deployments endpoint ([ade7884](https://github.com/onkernel/kernel-python-sdk/commit/ade788484f181ebfb516d831ee01aba9b9ef4037))
* **api:** deployments ([681895c](https://github.com/onkernel/kernel-python-sdk/commit/681895c60447b9ac6deaa32cf4031618a242f274))
* **api:** manual updates ([93870c1](https://github.com/onkernel/kernel-python-sdk/commit/93870c158c0b5b638483b0fa94ce1c2b1484db48))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([ab1f806](https://github.com/onkernel/kernel-python-sdk/commit/ab1f806916ffa510799f2780ba1e770baedc0933))

## 0.6.3 (2025-06-25)

Full Changelog: [v0.6.2...v0.6.3](https://github.com/onkernel/kernel-python-sdk/compare/v0.6.2...v0.6.3)

### Features

* **api:** /browsers no longer requires invocation id ([d1ff453](https://github.com/onkernel/kernel-python-sdk/commit/d1ff4534a930e11b12055629dbb98db7d4c63ad5))

## 0.6.2 (2025-06-24)

Full Changelog: [v0.6.1...v0.6.2](https://github.com/onkernel/kernel-python-sdk/compare/v0.6.1...v0.6.2)

### Features

* **api:** add `since` parameter to deployment logs endpoint ([39fb799](https://github.com/onkernel/kernel-python-sdk/commit/39fb79951c1f42c6eb7d07043432179ee132ff2c))
* **client:** add support for aiohttp ([fbe32a1](https://github.com/onkernel/kernel-python-sdk/commit/fbe32a143a69f45cc8f93aab70d8fd555a337a9d))


### Chores

* **tests:** skip some failing tests on the latest python versions ([9441e05](https://github.com/onkernel/kernel-python-sdk/commit/9441e056d0a162b77149d717d83d75b67baf912b))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([f3c0127](https://github.com/onkernel/kernel-python-sdk/commit/f3c0127bb4132bcf19ce2fd3016776c556386ffb))

## 0.6.1 (2025-06-18)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.6.0...v0.6.1)

### Features

* **api:** add delete_browsers endpoint ([1d378d3](https://github.com/onkernel/kernel-python-sdk/commit/1d378d3a505c2bce7453a7da3fc70ce78f8349cf))

## 0.6.0 (2025-06-18)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** update via SDK Studio ([a811017](https://github.com/onkernel/kernel-python-sdk/commit/a81101709db8cb64b4cb6af6b749b55f86c24be6))
* **api:** update via SDK Studio ([0c8937a](https://github.com/onkernel/kernel-python-sdk/commit/0c8937a4d8891357223c41fadcb05a6dd1f359b1))
* **api:** update via SDK Studio ([dff3e39](https://github.com/onkernel/kernel-python-sdk/commit/dff3e3965fc710beadac2410a8a065d81b889d43))
* **api:** update via SDK Studio ([d26c519](https://github.com/onkernel/kernel-python-sdk/commit/d26c519a798d8bf66baaef49af818b4108c3d92a))
* **api:** update via SDK Studio ([ff07935](https://github.com/onkernel/kernel-python-sdk/commit/ff0793585ded6d9ea6c50947b9915f560221ed0f))
* **api:** update via SDK Studio ([fe8d70b](https://github.com/onkernel/kernel-python-sdk/commit/fe8d70b1f0a0725c37c794aeb5a7a466bc13cdf3))
* **api:** update via SDK Studio ([8073db6](https://github.com/onkernel/kernel-python-sdk/commit/8073db60205835e3abb6c494e24bb034283c55f2))
* **api:** update via SDK Studio ([c1cdbcc](https://github.com/onkernel/kernel-python-sdk/commit/c1cdbcc6e555ab5fc7ecc229095ff7d0bf272e1a))
* **api:** update via SDK Studio ([eed8e67](https://github.com/onkernel/kernel-python-sdk/commit/eed8e6769fd4982cadb277aa4c271c211992077a))
* **api:** update via SDK Studio ([7699111](https://github.com/onkernel/kernel-python-sdk/commit/76991114e757c0c054e89d614619e38b2ec7d918))
* **api:** update via SDK Studio ([d51332b](https://github.com/onkernel/kernel-python-sdk/commit/d51332b18af547affb215d9a7596bbbdb7ccff24))
* **api:** update via SDK Studio ([452e83c](https://github.com/onkernel/kernel-python-sdk/commit/452e83c41d808b97e1ff54cdfa79d74abccfc9b5))
* **api:** update via SDK Studio ([496e5cd](https://github.com/onkernel/kernel-python-sdk/commit/496e5cd31745446c16234120f9299be4a9830bb5))


### Bug Fixes

* **client:** correctly parse binary response | stream ([0079349](https://github.com/onkernel/kernel-python-sdk/commit/007934910a1ec8e17a6be821feacef9b42a2c142))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([53d6547](https://github.com/onkernel/kernel-python-sdk/commit/53d65471447af6f764aa48bd708c540215c8fd4a))


### Chores

* **ci:** enable for pull requests ([fb3fba1](https://github.com/onkernel/kernel-python-sdk/commit/fb3fba16b9149449f8327b909210d42ee7744ba4))
* **internal:** update conftest.py ([bcfcef2](https://github.com/onkernel/kernel-python-sdk/commit/bcfcef2eb9cd584ad6ec508956d59b34211d2e14))
* **readme:** update badges ([099868c](https://github.com/onkernel/kernel-python-sdk/commit/099868c0c2fbb92a4b9e97cda89bf4e71781d76f))
* **tests:** add tests for httpx client instantiation & proxies ([235bf24](https://github.com/onkernel/kernel-python-sdk/commit/235bf248a71505c9d5d536f1b6a7120e43b9cedc))
* **tests:** run tests in parallel ([83e4f2c](https://github.com/onkernel/kernel-python-sdk/commit/83e4f2c26f02a7df56917e993af1e1d85ba241e6))

## 0.5.0 (2025-06-03)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** update via SDK Studio ([6bc85d1](https://github.com/onkernel/kernel-python-sdk/commit/6bc85d1fb74d7c496c02c1bde19129ae07892af7))
* **api:** update via SDK Studio ([007cb3c](https://github.com/onkernel/kernel-python-sdk/commit/007cb3cafc3697743131489bfd46651f246c2e87))
* **client:** add follow_redirects request option ([4db3b7f](https://github.com/onkernel/kernel-python-sdk/commit/4db3b7f7a19af62ac986fcf4482cfe0a5454ca50))


### Chores

* **docs:** remove reference to rye shell ([1f9ea78](https://github.com/onkernel/kernel-python-sdk/commit/1f9ea78913d336137e76aa4d8c83e708ee6b9fd6))

## 0.4.0 (2025-05-28)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** update via SDK Studio ([eda6c2c](https://github.com/onkernel/kernel-python-sdk/commit/eda6c2c9ec1f585b8546c629bb661f0f9a9e9c04))

## 0.3.0 (2025-05-22)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** update via SDK Studio ([e87dc0f](https://github.com/onkernel/kernel-python-sdk/commit/e87dc0f7ab8eac43664050e0325fca9225b12c16))
* **api:** update via SDK Studio ([e4b0438](https://github.com/onkernel/kernel-python-sdk/commit/e4b0438d63b71ea30feae04328f32ddbcdd2b15e))
* **api:** update via SDK Studio ([4a8f812](https://github.com/onkernel/kernel-python-sdk/commit/4a8f812a39dcf768ac753c77d1d2d31881d8c4ec))
* **api:** update via SDK Studio ([260f1a2](https://github.com/onkernel/kernel-python-sdk/commit/260f1a2e5e877e91c066935533c376c341612557))


### Chores

* **docs:** grammar improvements ([f0f0e85](https://github.com/onkernel/kernel-python-sdk/commit/f0f0e855505db93ad22cea24ec73acf13b4f8ed5))

## 0.2.0 (2025-05-21)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0...v0.2.0)

### Features

* **api:** update via SDK Studio ([34cef34](https://github.com/onkernel/kernel-python-sdk/commit/34cef341e4ec5e5734f167746ea66664eb4b8474))


### Chores

* **internal:** version bump ([924b2f7](https://github.com/onkernel/kernel-python-sdk/commit/924b2f76f4ffbe5a6c5134efcc9d39d016dcf2a7))

## 0.1.0 (2025-05-21)

Full Changelog: [v0.1.0-alpha.15...v0.1.0](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.15...v0.1.0)

### Features

* **api:** update via SDK Studio ([0950b19](https://github.com/onkernel/kernel-python-sdk/commit/0950b197ae15bd4f5feecaee80a8de3c54a1e900))

## 0.1.0-alpha.15 (2025-05-20)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

* **api:** update via SDK Studio ([085cf7c](https://github.com/onkernel/kernel-python-sdk/commit/085cf7cd9c68bdef67f360a21f9bd6750483001b))
* **api:** update via SDK Studio ([da4cc1f](https://github.com/onkernel/kernel-python-sdk/commit/da4cc1f1aa385482b0557773845119299b46e270))

## 0.1.0-alpha.14 (2025-05-20)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

* **api:** update via SDK Studio ([43ca550](https://github.com/onkernel/kernel-python-sdk/commit/43ca55001379577ccd8f76106ba61d34e4d19579))

## 0.1.0-alpha.13 (2025-05-20)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Features

* **api:** update via SDK Studio ([c528c7b](https://github.com/onkernel/kernel-python-sdk/commit/c528c7b45adac371fddfdc2792a435f814b03d67))

## 0.1.0-alpha.12 (2025-05-19)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** update via SDK Studio ([7ae75cc](https://github.com/onkernel/kernel-python-sdk/commit/7ae75cc86e63a349ba4cd0d3e7a5e9814865766e))
* **api:** update via SDK Studio ([6359d12](https://github.com/onkernel/kernel-python-sdk/commit/6359d1225c4859929868fd58b67bbe00146951de))

## 0.1.0-alpha.11 (2025-05-19)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

* **api:** update via SDK Studio ([16afb5a](https://github.com/onkernel/kernel-python-sdk/commit/16afb5a7a1da33771aca73685dc32b0a1e90ce2d))
* **api:** update via SDK Studio ([08c35c8](https://github.com/onkernel/kernel-python-sdk/commit/08c35c8662ad34c76936c9dbeac7057a74e4a0df))

## 0.1.0-alpha.10 (2025-05-19)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **api:** update via SDK Studio ([a382570](https://github.com/onkernel/kernel-python-sdk/commit/a382570e96f3bae625cb176e746038fcdf0e8e73))


### Chores

* **ci:** fix installation instructions ([c897375](https://github.com/onkernel/kernel-python-sdk/commit/c8973750a1ae58f7c8eee588bbe874862dbbb46d))
* **ci:** upload sdks to package manager ([03d0f7f](https://github.com/onkernel/kernel-python-sdk/commit/03d0f7f19be9614f5a81bd5c31117febd68ec5e9))
* **internal:** codegen related update ([49143bd](https://github.com/onkernel/kernel-python-sdk/commit/49143bdcb6635ae79b1c4c5fddc9017d8d81b4d7))

## 0.1.0-alpha.9 (2025-05-14)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** update via SDK Studio ([472443c](https://github.com/onkernel/kernel-python-sdk/commit/472443c0fc689a2a1e6e5177fc74ca78e556a0d6))

## 0.1.0-alpha.8 (2025-05-12)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** update via SDK Studio ([68c2cc8](https://github.com/onkernel/kernel-python-sdk/commit/68c2cc821cf9c31f8e5e054ba69780cbba2449db))

## 0.1.0-alpha.7 (2025-05-11)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** update via SDK Studio ([2810c5c](https://github.com/onkernel/kernel-python-sdk/commit/2810c5c0e0e0e89e03a00b27fb1d2ab355f3a8ff))

## 0.1.0-alpha.6 (2025-05-11)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** update via SDK Studio ([d2d465e](https://github.com/onkernel/kernel-python-sdk/commit/d2d465ee112484eb9acd1b5f8714bc5650f2b4de))

## 0.1.0-alpha.5 (2025-05-10)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** update via SDK Studio ([8bceece](https://github.com/onkernel/kernel-python-sdk/commit/8bceece9fb86d9dbc0446abd1018788ff4fbda80))

## 0.1.0-alpha.4 (2025-05-10)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([d93116e](https://github.com/onkernel/kernel-python-sdk/commit/d93116e633eb9503647acfbe3e9769f33fdd19ed))

## 0.1.0-alpha.3 (2025-05-10)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Bug Fixes

* **package:** support direct resource imports ([679b117](https://github.com/onkernel/kernel-python-sdk/commit/679b11723a5699be2b6b50ccce2b84a88d1e0a7b))
* **tests:** skip broken binary tests for now ([69638c0](https://github.com/onkernel/kernel-python-sdk/commit/69638c0d0da19a74a91e182a209c3de06985e112))

## 0.1.0-alpha.2 (2025-05-09)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/onkernel/kernel-python-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([fb257f7](https://github.com/onkernel/kernel-python-sdk/commit/fb257f70bd5bb606766adc0f27e96b7a8d537680))

## 0.1.0-alpha.1 (2025-05-08)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/onkernel/kernel-python-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([e093d2c](https://github.com/onkernel/kernel-python-sdk/commit/e093d2cd1058d442533e4783184ae63ee7007230))


### Chores

* update SDK settings ([87f35dd](https://github.com/onkernel/kernel-python-sdk/commit/87f35dd263016821b8691906afea82ba45d68c99))
* update SDK settings ([1553626](https://github.com/onkernel/kernel-python-sdk/commit/1553626491d7fcffa12ca52e9e9b0d468ab8151a))
