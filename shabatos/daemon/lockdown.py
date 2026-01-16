"""Lockdown utilities for ShabatOS."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class LockdownPlan:
    block_network: bool
    mute_notifications: bool
    allowlist_apps: Iterable[str]
    denylist_apps: Iterable[str]


def enable_lockdown(plan: LockdownPlan) -> None:
    """Apply lockdown actions.

    This function currently logs intended actions. Replace with real
    implementations (nftables, systemd, etc.) as the project grows.
    """

    logging.info("Lockdown enabled: block_network=%s", plan.block_network)
    if plan.mute_notifications:
        logging.info("Notifications muted")
    logging.info("Allowlist apps: %s", ", ".join(plan.allowlist_apps))
    logging.info("Denylist apps: %s", ", ".join(plan.denylist_apps))


def disable_lockdown() -> None:
    """Disable lockdown actions."""

    logging.info("Lockdown disabled")
