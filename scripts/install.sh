#!/usr/bin/env bash
set -euo pipefail

PREFIX=${PREFIX:-/opt/shabatos}

sudo mkdir -p "$PREFIX"
sudo cp -R shabatos "$PREFIX/"
sudo cp -R systemd /etc/systemd/system/shabatos

sudo systemctl daemon-reload
sudo systemctl enable --now shabatosd.timer

echo "ShabatOS installed to $PREFIX"
