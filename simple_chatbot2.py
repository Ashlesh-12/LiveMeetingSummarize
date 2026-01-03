print("Chatbot: Hi! I am your chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ['hi', 'hello', 'hey']:
        print("Chatbot: Hello! How can I help you?")

    elif user in ['how are you?', 'how are you', 'how r u']:
        print("Chatbot: I am fine! Thank you. How are you?")

    elif user.startswith("my name is"):
        name = user.replace("my name is", "").strip().title()
        print(f"Chatbot: Nice to meet you, {name}!")

    elif user in ["what is your name?", "your name?", "who are you?"]:
        print("Chatbot: I am a simple Python chatbot created by you!")

    elif user in ['thanks', 'thank you', 'thank u']:
        print("Chatbot: You're welcome!")

    elif user in ["what can you do?", "help", "help me"]:
        print("Chatbot: I can reply to basic messages like greetings, questions, and more!")

    elif user in ["tell me a joke", "joke"]:
        print("Chatbot: Why don’t programmers like nature? It has too many bugs!")

    elif user == 'bye':
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: I am sorry, I don't understand.")
