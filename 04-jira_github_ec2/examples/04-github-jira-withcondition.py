import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

@app.route("/createJIRA", methods=["POST"])
def createJIRA():

    # Read GitHub webhook payload
    github_payload = request.json

    print("========== GITHUB PAYLOAD ==========")
    print(json.dumps(github_payload, indent=4))
    print("====================================")

    # Validate comment field
    if "comment" not in github_payload:
        return "No comment found in payload"

    comment = github_payload["comment"]["body"]

    print("Received Comment:", repr(comment))

    # Check for /jira command
    if comment.strip().lower().startswith("/jira"):

        print("Condition Matched. Creating Jira Ticket...")

        url = "https://mlnpublicact365.atlassian.net/rest/api/3/issue"

        API_TOKEN = "YOUR_JIRA_TOKEN"

        auth = HTTPBasicAuth(
            "mlnpublicact365@gmail.com",
            API_TOKEN
        )

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields": {

                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": "Created from GitHub comment",
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

                "summary": "Issue created from GitHub webhook"
            }
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return json.dumps(
            response.json(),
            sort_keys=True,
            indent=4
        )

    else:

        print("Condition Failed")

        return "Comment does not start with /jira"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)