import requests
import json

url = "http://127.0.0.1:8000/chat"

messages = [
    {
        "role": "user",
        "content": "Need an assessment for hiring"
    },
    {
        "role": "assistant",
        "content": "What kind of role are you hiring for?"
    },
    {
        "role": "user",
        "content": "I don't want to answer questions. Just recommend something."
    }
]

response = requests.post(
    url,
    json={"messages": messages}
)

print("\nSTATUS CODE:", response.status_code)
print("\nRAW RESPONSE:\n")
print(response.text)

data = response.json()

print("\n" + "="*60)
print(" USER REFUSES QUESTIONS TEST ")
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