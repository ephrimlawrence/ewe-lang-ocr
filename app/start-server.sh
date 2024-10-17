#!/usr/bin/sh

set -e

# export TESSDATA_PREFIX=$(pwd)

echo $TESSDATA_PREFIX
echo "Starting server..."
TESSDATA_PREFIX=$(pwd) ../venv/bin/uvicorn main:app --reload
