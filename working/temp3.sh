#!/bin/bash

sudo systemctl stop auto-cpufreq.service
sudo systemctl disable auto-cpufreq.service
sudo auto-cpufreq --install
sudo systemctl start auto-cpufreq.service
sudo systemctl enable auto-cpufreq.service

