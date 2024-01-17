import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://manpreet026.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("pearlajs12@gmail.com", "ATATT3xFfGF0Nd2mpXMrG8Lnp64k2Xl45gimPmqcnk0UUqcJPs4tvsZHeI9XuaFvONXvU06wOEAZkAC1W7O0L3ucoRIYJqSQ9QFZtvgY9h36RjGIYaHDgafW4fygclHbvphwdV73wpa-sKx1rl4_lGfBE1lLwsPVqLPCKG7ybHxTHfzSBBTxSns=5C0E279A")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
output=json.loads(response.text)

name=output[0]["name"]
print(name)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))