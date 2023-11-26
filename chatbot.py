import re
def rule_based_chatbot(user_input):
    user_input = user_input.lower()
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am just a computer program, but thanks for asking!',
        r'your name|who are you': 'I am a rule-based chatbot.',
        r'bye|goodbye': 'Goodbye! Have a great day!',
    }

    
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break
    response = rule_based_chatbot(user_input)
    print("Bot:", response)
