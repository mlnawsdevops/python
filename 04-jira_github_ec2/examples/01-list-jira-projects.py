# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mlnpublicact365.atlassian.net/rest/api/3/project"

API_TOKEN = "YOUR_JIRA_TOKEN"

auth = HTTPBasicAuth("mlnpublicact365@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# converting json to dictionary 
data=response.json()

# print(data)

for item in data:
    print(item["name"])

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))