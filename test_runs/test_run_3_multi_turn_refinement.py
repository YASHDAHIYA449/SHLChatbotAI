import requests
import json
url = "http://127.0.0.1:8000/chat"
messages = [
    {
        "role": "user",
        "content": "Hiring Java developers"
    },
    {
        "role": "assistant",
        "content": "What seniority level are you hiring for?"
    },
    {
        "role": "user",
        "content": "Mid-level developers with backend API experience"
    }
]
payload = {
    "messages": messages
}
response = requests.post(url, json=payload)
print(json.dumps(response.json(), indent=2))