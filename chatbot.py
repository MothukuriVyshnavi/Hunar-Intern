def chatbot():
    print("SimpleBot: Hello! I’m SimpleBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("SimpleBot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("SimpleBot: I'm just a bunch of code, but I'm functioning properly!")
        
        elif "your name" in user_input:
            print("SimpleBot: I'm SimpleBot, your friendly chatbot.")

        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"SimpleBot: The current time is {now.strftime('%H:%M:%S')}.")

        elif "date" in user_input:
            from datetime import datetime
            today = datetime.today()
            print(f"SimpleBot: Today is {today.strftime('%B %d, %Y')}.")

        elif "help" in user_input:
            print("SimpleBot: I can respond to greetings, tell you the time, date, and more!")

        elif "bye" in user_input or "exit" in user_input:
            print("SimpleBot: Goodbye! Have a great day!")
            break

        else:
            print("SimpleBot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()