
print("===================================")
print("   Welcome to DecodeLabs AI Chatbot")
print("===================================")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("Bot: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("Bot: I am the DecodeLabs Rule-Based AI Chatbot.") 

    elif "favourite colour" in user_input or "favorite color" in user_input:
        print("Bot: I would choose blue! It reminds me of the sky.")  

    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot: You're welcome! Happy to help.")

    elif "python" in user_input:
        print("Bot: Python is a programming language used to build applications and AI projects.")

    elif "artificial intelligence" in user_input or user_input == "ai":
        print("Bot: Artificial Intelligence helps machines perform tasks that normally require human intelligence.")

    elif "project" in user_input:
        print("Bot: My project is a Rule-Based AI Chatbot developed using Python.")

    elif "help" in user_input:
        print("Bot: You can ask me about Python, AI, my name, or my project.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    elif user_input == "":
        print("Bot: Please type a message.")

    else:
        print("Bot: Sorry, I don't understand that yet. Please try another question.")
