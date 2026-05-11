import requests
import json
url = "http://127.0.0.1:8000/chat"
messages = [
    {
        "role": "user",
        "content": "Need coding assessment for Java developers"
    },
    {
        "role": "assistant",
        "content": "I recommend Java 8 (New) and OPQ32r."
    },
    {
        "role": "user",
        "content": "Perfect, thank you"
    }
]
payload = {
    "messages": messages
}
response = requests.post(url, json=payload)
print(json.dumps(response.json(), indent=2))