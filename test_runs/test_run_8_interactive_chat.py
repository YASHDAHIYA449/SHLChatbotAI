import requests

url = "http://127.0.0.1:8000/chat"

messages = []

while True:

    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = requests.post(
        url,
        json={"messages": messages}
    )

    data = response.json()

    print("\nAssistant:")
    print(data["reply"])

    print("\nRecommendations:")

    for rec in data["recommendations"]:
        print(f"- {rec['name']}")

    print()

    assistant_memory = data["reply"]

    if data["recommendations"]:

        assistant_memory += "\n\nRecommended Assessments:\n"

        for rec in data["recommendations"]:
            assistant_memory += f"- {rec['name']}\n"

    messages.append({
        "role": "assistant",
        "content": assistant_memory
    })