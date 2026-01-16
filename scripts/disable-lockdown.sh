#!/usr/bin/env bash
set -euo pipefail

CONFIG_PATH=${CONFIG_PATH:-/opt/shabatos/config/shabatos.yaml}

/usr/bin/python3 /opt/shabatos/cli/shabatosctl.py --config "$CONFIG_PATH" disable
