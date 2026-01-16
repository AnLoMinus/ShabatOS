"""ShabatOS daemon: schedules and enforces Shabbat Mode."""

from __future__ import annotations

import argparse
import logging
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

from shabatos.daemon.lockdown import LockdownPlan, disable_lockdown, enable_lockdown


@dataclass(frozen=True)
class ModeConfig:
    auto: bool
    pre_shabbat_minutes: int
    exit_after_minutes: int


@dataclass(frozen=True)
class EmergencyConfig:
    enabled: bool
    pin_hash: str
    allow_network_minutes: int


@dataclass(frozen=True)
class AppConfig:
    mode: ModeConfig
    lockdown: LockdownPlan
    emergency: EmergencyConfig


def load_config(config_path: Path) -> AppConfig:
    data: dict[str, Any] = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    mode = data.get("mode", {})
    lockdown = data.get("lockdown", {})
    emergency = data.get("emergency", {})

    return AppConfig(
        mode=ModeConfig(
            auto=bool(mode.get("auto", True)),
            pre_shabbat_minutes=int(mode.get("pre_shabbat_minutes", 60)),
            exit_after_minutes=int(mode.get("exit_after_minutes", 1200)),
        ),
        lockdown=LockdownPlan(
            block_network=bool(lockdown.get("block_network", True)),
            mute_notifications=bool(lockdown.get("mute_notifications", True)),
            allowlist_apps=lockdown.get("allowlist_apps", []),
            denylist_apps=lockdown.get("denylist_apps", []),
        ),
        emergency=EmergencyConfig(
            enabled=bool(emergency.get("enabled", True)),
            pin_hash=str(emergency.get("pin_hash", "")),
            allow_network_minutes=int(emergency.get("allow_network_minutes", 20)),
        ),
    )


def run_scheduler(config: AppConfig) -> None:
    """Placeholder scheduler loop.

    TODO: Replace with location-based schedule and precise Shabbat times.
    """

    logging.info("Scheduler started. Auto=%s", config.mode.auto)
    next_transition = datetime.now() + timedelta(minutes=config.mode.pre_shabbat_minutes)

    while True:
        now = datetime.now()
        if now >= next_transition:
            logging.info("Entering Shabbat Mode (placeholder)")
            enable_lockdown(config.lockdown)
            time.sleep(config.mode.exit_after_minutes * 60)
            disable_lockdown()
            next_transition = now + timedelta(days=7)
        time.sleep(30)


def main() -> None:
    parser = argparse.ArgumentParser(description="ShabatOS daemon")
    parser.add_argument(
        "--config",
        default="/opt/shabatos/config/shabatos.yaml",
        help="Path to shabatos.yaml",
    )
    parser.add_argument("--once", action="store_true", help="Run one cycle")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    config_path = Path(args.config)
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    config = load_config(config_path)

    if args.once:
        enable_lockdown(config.lockdown)
        disable_lockdown()
        return

    run_scheduler(config)


if __name__ == "__main__":
    main()
