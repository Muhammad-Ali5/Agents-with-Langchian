import requests

API_URL = "http://127.0.0.1:8000/chat/"

print("🔗 Connected to Gemini Chatbot via FastAPI!")
print("💬 Type your message below. Type 'exit' or 'quit' to end.\n")

while True:
    user_input = input("🧍‍♂️ You: ")

    # Exit condition
    if user_input.strip().lower() in ["exit", "quit"]:
        print("👋 Goodbye sweetheart!")
        break

    try:
        # Send POST request to FastAPI
        res = requests.post(API_URL, data={"question": user_input})

        # Handle valid response
        if res.status_code == 200:
            print("Gemini:", res.json()["answer"], "\n")
        else:
            print(" Error:", res.json(), "\n")

    except Exception as e:
        print("Request failed:", e, "\n")
