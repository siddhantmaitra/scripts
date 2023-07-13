#!/bin/bash
#Find the most used commands in history
history | awk '{print }' | sort | uniq -c | sort -nr | head -10
