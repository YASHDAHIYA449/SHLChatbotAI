import requests
import json

url = "http://127.0.0.1:8000/chat"

messages = [
    {
        "role": "user",
        "content": "I'm not really sure what kind of assessment I need. We just want to hire good people."
    }
]

response = requests.post(
    url,
    json={"messages": messages}
)

data = response.json()

print("\n" + "="*60)
print(" UNCERTAIN USER TEST ")
print("="*60)

print("\nAssistant Reply:\n")
print(data["reply"])

print("\nRecommended Assessments:\n")

if data["recommendations"]:
    for idx, rec in enumerate(data["recommendations"], start=1):
        print(f"{idx}. {rec['name']}")
        print(f"   Type : {rec['test_type']}")
        print(f"   URL  : {rec['url']}\n")
else:
    print("No recommendations.")

print(f"\nEnd Of Conversation: {data['end_of_conversation']}")
print("="*60)