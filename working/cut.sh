#!/bin/bash
input=dates.txt 
while IFS= read -r line
do
  echo "$line"
done < "$input"

