import requests
import json
url = "http://127.0.0.1:8000/chat"
messages = [
    {
        "role": "user",
        "content": "Need assessments for leadership hiring"
    },
    {
        "role": "assistant",
        "content": "I recommend OPQ32r and Global Skills Assessment."
    },
    {
        "role": "user",
        "content": "What is the difference between OPQ32r and Global Skills Assessment?"
    }
]
payload = {
    "messages": messages
}
response = requests.post(url, json=payload)
print(json.dumps(response.json(), indent=2))