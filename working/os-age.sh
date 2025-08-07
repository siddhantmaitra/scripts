#!/bin/sh

set -euo pipefail

VAR=$(df --output=source / | tail --lines=1)

sudo  tune2fs -l $VAR | grep 'Filesystem created'

