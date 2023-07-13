#!/bin/bash 

stopwatch () {
	printf "Stopwatch started at $(date +"%T")\n"
	echo 
	local start=$SECONDS 
	read -p "Press enter to exit..." 

	((final=$SECONDS-$start)) 

	hours=$((final / 3600))
	seconds=$((final % 3600)) 
	minutes=$((seconds / 60))
	seconds=$((seconds % 60))

	printf "Stopped at $(date +"%T")"
	printf "\nTime elapsed:\n $hours hrs $minutes mins $seconds secs => $final seconds \n" 

}

stopwatch

	
