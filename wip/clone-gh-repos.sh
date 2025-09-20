#!/bin/env sh

set -eu pipefail

USER_NAME=siddhantmaitra

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
  "https://api.github.com/users/${USER_NAME}/repos" \
  | jq  '.[] | select(.archived == false and (.topics | any(. == "experiment") | not)) | .ssh_url'
