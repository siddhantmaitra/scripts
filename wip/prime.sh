#!/bin/env bash 

printf "Enter a Number: "
read n
i=1
c=0
while [ $i -le $n ]
do
	if [ `expr $n % $i` -eq 0 ]
	then
		c=`expr $c + 1`
	fi
	i=`expr $i + 1`
done
if [ $c -eq 2 ]
then
	printf "$n is a prime number\n"
else
	printf "$n is NOT a prime number\n"
fi
