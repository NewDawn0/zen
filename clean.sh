#!/usr/bin/env bash
ZEN_FILES=(".mypy_cache" ".pytest_cache" "__pycache__" "api/__pycache__/" "components/__pycache__/" "tests/__pycache__/" "userConfig/__pycache__/" "utils/__pycache__/" "utils/globals/__pycache__/" "build")
CLEAN_FILES=("build" "zen.egg-info")
for file in ${ZEN_FILES[@]}; do
    rm -rf "zen/$file"
done

for file in ${CLEAN_FILES[@]}; do
    rm -rf "$file"
done
