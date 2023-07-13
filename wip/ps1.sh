#!/bin/bash

BLACK="\e[1;30m"
RED="\e[1;31m"
GREEN="\e[1;32m"
YELLOW="\e[1;33m"
BLUE="\e[34m"
PURPLE="\e[1;35m"
CYAN="\e[1;36m"
WHITE="\e[1;37m"
LTBLACK="\e[1;90m"
LTRED="\e[1;91m"
LTGREEN="\e[1;92m"
LTYELLOW="\e[93m"
LTBLUE="\e[1;94m"
LTPURPLE="\e[95m"
LTCYAN="\e[1;96m"
LTWHITE="\e[1;97m"
RESET="\e[0m"

export PS1="\[${LTRED}\]\t \[${LTPURPLE}\]WD= \[${YELLOW}\][\w]\n\[${GREEN}\]\u\[${YELLOW}\]@\[${LTBLUE}\]\h\[${RESET}\] \$ "

