#!/bin/bash

# Read the value of ID from /etc/os-release
ID=$(grep -oP '(?<=^ID=).+' /etc/os-release | tr -d '"')

# Read the value of ID_LIKE from /etc/os-release
ID_LIKE=$(grep -oP '(?<=^ID_LIKE=).+' /etc/os-release | tr -d '"')

# Check if either ID or ID_LIKE contains "arch"
if [[ "$ID" == "arch" || "$ID_LIKE" == *"arch"* ]]; then
    echo "This system is based on Arch Linux."
else
    echo "This system is not based on Arch Linux."
fi

