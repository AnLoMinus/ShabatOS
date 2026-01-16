"""Command-line interface for ShabatOS."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import yaml

from shabatos.daemon.lockdown import LockdownPlan, disable_lockdown, enable_lockdown


def load_lockdown_plan(config_path: Path) -> LockdownPlan:
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    lockdown = data.get("lockdown", {})
    return LockdownPlan(
        block_network=bool(lockdown.get("block_network", True)),
        mute_notifications=bool(lockdown.get("mute_notifications", True)),
        allowlist_apps=lockdown.get("allowlist_apps", []),
        denylist_apps=lockdown.get("denylist_apps", []),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="ShabatOS control")
    parser.add_argument(
        "--config",
        default="/opt/shabatos/config/shabatos.yaml",
        help="Path to shabatos.yaml",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("enable", help="Enable Shabbat mode")
    subparsers.add_parser("disable", help="Disable Shabbat mode")
    subparsers.add_parser("status", help="Print current status (placeholder)")

    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    config_path = Path(args.config)
    if args.command == "enable":
        plan = load_lockdown_plan(config_path)
        enable_lockdown(plan)
    elif args.command == "disable":
        disable_lockdown()
    elif args.command == "status":
        logging.info("Status: placeholder (no state storage yet)")


if __name__ == "__main__":
    main()
