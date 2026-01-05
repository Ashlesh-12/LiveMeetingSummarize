!pip install groq
import os
from google.colab import userdata

# Load the API key from Colab Secrets
os.environ["GROQ_API_KEY"] = userdata.get('GROQ_API_KEY')



from groq import Groq
import os

# Initialize the Groq client using the environment variable
# Groq() automatically looks for the GROQ_API_KEY environment variable.
client = Groq()

def ask_bot(prompt):
    # Sends the user's prompt to the Groq API for completion
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", # Use a currently available Groq model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print("AI Chatbot Ready! Type 'quit' to exit.")

# Main chat loop
while True:
    # Use the input function to interact in the Colab cell
    user = input("You: ")

    if user.lower() == "quit":
        print("Bot: Bye!")
        break

    print("Bot:", ask_bot(user))
