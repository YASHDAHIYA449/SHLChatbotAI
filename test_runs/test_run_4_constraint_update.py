import requests
import json
url = "http://127.0.0.1:8000/chat"
messages = [
    {
        "role": "user",
        "content": "Hiring backend developers"
    },
    {
        "role": "assistant",
        "content": "What technologies are required?"
    },
    {
        "role": "user",
        "content": "Node.js and cloud infrastructure"
    },
    {
        "role": "assistant",
        "content": "I recommend Node.js (New) and Linux Programming (General)."
    },
    {
        "role": "user",
        "content": "Actually also include personality assessments"
    }
]
payload = {
    "messages": messages
}
response = requests.post(url, json=payload)
print(json.dumps(response.json(), indent=2))