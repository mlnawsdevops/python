# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

# my jira url
url = "https://mlnpublicact365.atlassian.net/rest/api/3/issue"

# Jira profile -> acct settings -> security -> create API TOKEN
API_TOKEN = "YOUR_JIRA_TOKEN"

auth = HTTPBasicAuth("mlnpublicact365@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# description, issueType, reporter, 
payload = json.dumps( {
  "fields": {
   
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Masthan Babu Bathala",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    
    "issuetype": {
      "id": "10050"
    },

    "project": {
      "key": "MLNDEVOPS"
    },

    "summary": "BHP Coal mining",    
    
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