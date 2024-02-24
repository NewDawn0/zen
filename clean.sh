#!/usr/bin/env bash
TO_CLEAN=(".mypy_cache" ".pytest_cache" "__pycache__" "api/__pycache__/" "components/__pycache__/" "tests/__pycache__/" "userConfig/__pycache__/" "utils/__pycache__/")
for file in ${TO_CLEAN[@]}; do
    rm -rf "$file"
done
