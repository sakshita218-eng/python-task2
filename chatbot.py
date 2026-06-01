import sys

def get_chatbot_response(user_input: str) -> tuple[str, bool]:
    """
    Returns a response matching the user's input and a boolean indicating
    whether the conversation should terminate.
    """
    # Normalize input: trim whitespace and convert to lowercase for flexible matching
    cleaned = user_input.strip().lower()
    
    # Check for empty input
    if not cleaned:
        return "I'm listening! Please type something.", False
        
    # Check for goodbye commands to end the chat
    if cleaned in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a wonderful day!", True
        
    # Greeting intents
    if cleaned in ["hello", "hi", "hey", "hola", "greetings"]:
        return "Hi! How can I help you today?", False
        
    # Well-being intents
    elif cleaned in ["how are you", "how are you doing", "how's it going", "how do you do"]:
        return "I'm fine, thanks! How are you doing?", False
        
    # Identity intents
    elif "your name" in cleaned or "who are you" in cleaned:
        return "I am a simple rule-based chatbot. You can call me Chatty!", False
        
    # Help instructions
    elif cleaned in ["help", "what can you do", "commands"]:
        return ("Here are some things you can ask me:\n"
                " - Greetings (e.g., 'hello', 'hi')\n"
                " - Well-being (e.g., 'how are you')\n"
                " - My name (e.g., 'what is your name')\n"
                " - To end the chat, type 'bye', 'exit', or 'quit'"), False
                
    # Other simple conversation builders
    elif "weather" in cleaned:
        return "I can't check the weather right now, but I hope it's nice and sunny!", False
    elif "thank" in cleaned:
        return "You're very welcome!", False
        
    # Default fallback response for unrecognized inputs
    else:
        return "I'm sorry, I didn't quite catch that. Could you try rephrasing? Type 'help' for options.", False

def run_chatbot():
    """
    Starts and runs the interactive chatbot command-line interface.
    """
    print("=" * 50)
    print("         Welcome to the Basic Chatbot!         ")
    print("  Type 'help' to see what I can do, or 'bye' to exit. ")
    print("=" * 50)
    
    while True:
        try:
            # Prompt the user for input
            user_input = input("\nYou: ")
            
            # Get the chatbot response and the exit status flag
            response, should_exit = get_chatbot_response(user_input)
            
            # Print the chatbot's response
            print(f"Chatbot: {response}")
            
            # If the user input triggered the exit response, break the loop
            if should_exit:
                break
                
        except (KeyboardInterrupt, EOFError):
            # Gracefully handle Ctrl+C or Ctrl+D
            print("\nChatbot: Goodbye! (Session ended)")
            break

if __name__ == "__main__":
    run_chatbot()
