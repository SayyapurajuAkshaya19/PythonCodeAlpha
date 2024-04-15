import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you!', 'I am good, thanks for asking!']],
    ['what is your name?', ['My name is ChatBot.', 'I am called ChatBot.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']],
    ['what are you doing?', ['I am chatting with you!', 'Just chatting with you!','I am here to help you!']]
]

# Creating a Chatbot with the defined pairs
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Welcome to the chatbot! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

