import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://manpreet026.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("pearlajs12@gmail.com", "ATATT3xFfGF02r4ilsn6UIMHMJUw8fyaegcUnr4cE7RxxvKAvmzOPvDBtCsykBzoTneAh3UL1AIq7exFIi-ThoEfpSidvevYqEfUwoysydXAL54YQkKLs47lhVbhP_BtefcZ5ETqsCDjUJV00h5VWTyUEGDu2uUg7C5SZ013vs0V2mWK7q2IGHk=CDB4E79E")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "PEAR"
    },
    "issuetype": {
      "id": "10007"
    },
    "summary": "FIRST JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

