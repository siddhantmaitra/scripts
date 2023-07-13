#!/bin/bash

IFS=';' read updates security_updates < <(/usr/lib/update-notifier/apt-check 2>&1)
echo $updates
echo $security_updates
#add --human-readable to apt-check to get sentences.
