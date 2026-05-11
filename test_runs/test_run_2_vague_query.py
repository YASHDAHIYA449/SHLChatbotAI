import requests
import json

url = "http://127.0.0.1:8000/chat"

payload = {
    "messages": [
        {
            "role": "user",
            "content": "Need an assessment"
        }
    ]
}

response = requests.post(url, json=payload)

print(json.dumps(response.json(), indent=2))