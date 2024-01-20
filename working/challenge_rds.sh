# This was a mock challenge from ankush of realdevsquad, which I found on twitter

#!/bin/bash

cookie="connect.sid=s%3AbnzyRMq632t7l_ToorgS4GdKP94nZCCJ.fJqUwA%2FDjqBvG3v6wO5zZXurZhfB%2Bh%2FjRCxWzD4FZ6I"

json_response=$(curl -s -X GET \
     -H "Cookie: $cookie" \
     https://exam.ankush.wiki/challenges)

if [ $? -eq 0 ]; then
    count=$(echo "$json_response" | jq -r '.data[].name | scan("(?i)version")' | wc -w)

    echo "Number of words matching 'version' in the 'name' field: $count"

    curl -X POST \
         -H "Content-Type: application/json" \
         -H "Cookie: $cookie" \
         -d "{\"count\": $count}" \
         https://exam.ankush.wiki/challenges
else
    echo "Error: Failed to retrieve data from the server."
fi

