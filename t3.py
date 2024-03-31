import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind.",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you later :)"]
    ],
]

# Create a chatbot
def chatbot():
    print("Hi, I'm ChatBot! How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    chatbot()
