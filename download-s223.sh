#!/bin/bash

# if 223standard directory does not exist, clone the repo
if [ ! -d "223standard" ]; then
  git clone https://bas-im.emcs.cornell.edu/223/223standard.git
fi
# otherwise, update the repo
pushd 223standard
git pull
popd

# remove the old s223/ folder
rm -rf s223

# copy inference, extensions, collections, models, validation, vocab folders to s223/
mkdir s223
cp -r 223standard/inference 223standard/extensions 223standard/collections 223standard/models 223standard/validation 223standard/vocab s223
