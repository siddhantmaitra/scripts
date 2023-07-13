#!/bin/env bash 



batstatus=$(on_ac_power; echo $?);

if [[ $batstatus -eq 0 ]] 
then 
	echo charging
else
	echo discharging
fi


