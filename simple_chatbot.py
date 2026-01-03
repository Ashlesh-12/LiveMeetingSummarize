print("Chatbot: Hi! I am your chatbot. Type 'bye to exit.")
while True:
    user=input("You: ")
    if user.lower()=='hi':
        print("Chatbot: Hello! How can I help you?")
    elif user.lower()=='how are you?':
        print("Chatbot: I am fine! Thank you")
    elif user.lower()=='bye':
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot: I am sorry, I don't understand.")