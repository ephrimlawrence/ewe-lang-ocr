#! /usr/bin/sh

dir="$1"
prefix="$2"


for f in $(ls "$dir"); do
    echo $f
done
