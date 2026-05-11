import requests
import json
url = "http://127.0.0.1:8000/chat"
payload = {
    "messages": [
        {
            "role": "user",
            "content": "Recommend assessments for ASP.NET and C# backend engineers"
        }
    ]
}
response = requests.post(url, json=payload)
data = response.json()
print(json.dumps(data, indent=2))
print("\nVERIFY URL GROUNDING:\n")
for rec in data.get("recommendations", []):
    print(rec["name"])
    print(rec["url"])
    print()
