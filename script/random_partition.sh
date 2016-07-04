#!/bin/bash

cd `dirname $0`
. ../conf/configure

train_file_path=$NetflixTrainningData
result=$NetflixResult

for((i=2;i<=56;i+=2));do 
echo 'start partition';
date +%s;
echo 'User block partition is '$i;
echo 'Item block partition is '$i;
python ../src/Main.py $train_file_path $i $i;
echo "end partition";
date +%s;
done;
