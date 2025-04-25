#!/usr/bin/env bash
cd "$(dirname "$0")"


source "./.venv/bin/activate"
cage python3 ./game/main.py
