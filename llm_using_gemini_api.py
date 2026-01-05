!pip install groq


import os
from google.colab import userdata

# Load the API key from Colab Secrets
os.environ["GEMINI_API_KEY"] = userdata.get('GEMINI_API_KEY')


import os
from google import genai
from google.colab import userdata # <-- Import Colab's user data utility

# 1. Load the Secret into the Environment
# This line fetches the value from your Colab Secret named 'GEMINI_API_KEY'
# and sets it as the environment variable that the genai.Client() will read.
os.environ["GEMINI_API_KEY"] = userdata.get("GEMINI_API_KEY")

# 2. Initialize the Client
# The client will now automatically find the key from the environment variable.
client = genai.Client()

# 3. Start a persistent chat session
chat = client.chats.create(model="gemini-2.5-flash")

def ask_bot(prompt):
    response = chat.send_message(prompt)
    return response.text

print("Gemini Chatbot Ready! Type 'quit' to exit.\n")

# Main chat loop
while True:
    user = input("You: ")

    if user.lower() == "quit":
        print("Bot: Bye!")
        break

    print("Bot:", ask_bot(user))
