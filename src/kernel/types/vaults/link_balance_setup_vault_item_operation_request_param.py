# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LinkBalanceSetupVaultItemOperationRequestParam"]


class LinkBalanceSetupVaultItemOperationRequestParam(TypedDict, total=False):
    """
    Get the Link page where the user sets up Link balance, adds money to it, and chooses an approval threshold for this wallet's Link client. Kernel does not yet create spend requests under that approval policy, so cards from this wallet still require the user's approval even when they are paid from the balance. Available on connected Link wallets. Kernel first reads Link's user info and returns 409 unless Link reports eligible_for_balance as true, which depends on both the user and the wallet's Link client. Both amounts are suggestions the page prefills; the user makes the final choice. Send only what needs to change: desired_balance_amount to ask for money to be added, desired_transaction_limit to set or change the threshold, or both for first-time setup.
    """

    type: Required[Literal["link_balance_setup"]]

    desired_balance_amount: int
    """Balance, in cents, the user should end up with.

    The page prefills the amount to add to reach it and skips adding money when the
    balance already covers it. Whole dollars only. Link refuses links that ask the
    user to add more than $150 at once.
    """

    desired_transaction_limit: int
    """Approval threshold, in cents, to prefill.

    Link skips approval only for spend requests created under its approval policy,
    which Kernel cards do not use yet. Whole dollars, at most $500 because a single
    spend request cannot exceed $500. When set the page always shows the threshold
    step; when omitted it skips it.
    """
