#!/bin/env sh

set -eu pipefail

#gh repo list --no-archived --json sshUrl -q '.[].sshUrl' 
#gh repo list --no-archived --json sshUrl -q '.[].sshUrl' | xargs -n 1 git clone

if [ -z "${GITHUB_API_TOKEN-}" ]; then
	echo "GITHUB_API_TOKEN is unset or empty" >&2
	exit 1
else
    echo "GITHUB_API_TOKEN is set to: $GITHUB_API_TOKEN"
fi

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_API_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/users/siddhantmaitra/repos | jq '.[].ssh_url'
