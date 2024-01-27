#!/bin/bash

DIR="/home/sid/programs/practice/exercism"

cd $DIR

TIMESTAMP=$(date)

if [[ $(git status -s) ]]
then
    git add .

    git commit -m "Auto-commit on logout: $TIMESTAMP"

    git push origin main 
else
    COMMITS_TODAY=$(git log --since="midnight" --pretty=format:"%h" | wc -l)

    if [[ $COMMITS_TODAY -gt 0 ]]
    then
        echo "Number of commits made today in exercism: $COMMITS_TODAY"
    else
        echo "No commits were made today in exercism"
    fi
fi

