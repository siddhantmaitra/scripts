#!/bin/bash 

echo "Enter the deadline:"
read end

start=$(date +%H%M)

gap=$((10#$end - 10#$start))

echo $gap
