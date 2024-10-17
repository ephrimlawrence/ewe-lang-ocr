#!/usr/bin/sh
set -e

# clear training dir
rm --recursive --verbose tesstrain/data/eng-ground-truth/*.*

# copy data set to training dir
cp --recursive --verbose --force training_data/special-alphabet/ewe-*/* tesstrain/data/eng-ground-truth
cp --recursive --verbose --force training_data/special-alphabet/sentence/* tesstrain/data/eng-ground-truth

cd tesstrain;

make tesseract-langdata

make training MODEL_NAME=eng

# copy the final model
cp --verbose --force data/eng.traineddata .

echo "Training completed!";
