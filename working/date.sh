#!/bin/env bash 

echo "Enter start date: "
read start 
echo "Enter the end date: " 
read end 

while ! [[ $start > $end ]]; do
    echo $start
    start=$(date -d "$start + 1 day" +%F)
done
