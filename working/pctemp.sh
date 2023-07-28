#!/bin/env bash

update_interval=5  # Set the update interval in seconds

while true; do
    # Capture the temperature output
    temperature_output=$(paste <(cat /sys/class/thermal/thermal_zone*/type) <(cat /sys/class/thermal/thermal_zone*/temp) | column -s $'\t' -t | sed 's/\(.\)..$/.\1°C/')
    
    # Clear the screen
    tput clear

    # Print the temperature output
    echo "Temperature of Computer:"
    echo "$temperature_output"

    # Calculate the countdown based on update_interval
    secs_remaining=$update_interval
    while [ $secs_remaining -gt 0 ]; do
        echo "Updating in $secs_remaining secs"
        sleep 1
        tput cuu1     # Move cursor up one line
        tput el       # Clear the line
        secs_remaining=$((secs_remaining - 1))
    done
done
