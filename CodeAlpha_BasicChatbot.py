
# CodeAlpha Internship
# Project: Basic Chatbot
# Created by: Madhavi

def chatbot():

    print("--------------------------------")
    print("   WELCOME TO MY CHATBOT")
    print("--------------------------------")

    print("Bot: Hello! I am your chatbot.")
    print("Bot: You can ask me simple questions.")
    print("Bot: Type 'bye' to exit.")

    while True:

        user = input("\nYou: ").lower().strip()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I am fine, thank you!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created by Madhavi.")

        elif user == "thank you":
            print("Bot: You are welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand.")

# Start the chatbot
chatbot()
