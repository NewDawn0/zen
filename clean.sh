#!/usr/bin/env bash
ZEN_FILES=(
    "zen/.mypy_cache"
    "zen/.pytest_cache"
    "zen/__pycache__"
    "zen/api/__pycache__/"
    "zen/components/__pycache__/"
    "zen/tests/__pycache__/"
    "zen/userConfig/__pycache__/"
    "zen/utils/__pycache__/"
    "zen/utils/globals/__pycache__/"
    "zen/build"
    "build"
    "zen.egg-info"
    "$HOME/.config/zen/__pycache__/"
)
for file in ${ZEN_FILES[@]}; do
    rm -rf "$file"
done
