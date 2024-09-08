#! /usr/bin/sh

dir="$1"
prefix="$2"


for f in $(ls "$dir"); do
    mv -v "$dir$f" "$dir${prefix}_$f"
    # echo $f
done
