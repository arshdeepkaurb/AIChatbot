#Rule Based AI Python ChatBot 

import datetime
import time

name= input("Hello, enter your name : ")
presentHour= datetime.datetime.now().hour

if 5 <= presentHour <= 11: 
    print("Good morning, ", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon, ", name)
elif 17 <= presentHour <= 20:
    print("Good evening, ", name)
else:
    print("Good night, ", name)



print("Hello! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "Hello": "Hi, welcome. How can I help you?",
    "How are you?": "I am very fine. Thank you",
    "Who are you?": "I am smart AI chatbot",
    "Motivate me": "Keep going. Every bug of your project makes you a better developer",
    "Happy": "Great to hear that",
    "Sad": "Ohh sad. This too shall pass",
    "What are functions?": "Functions in Python are reusable blocks of code designed to perform a specific task."
} 

# Method/Function to get response of ChatBot 

def getResponseOfBot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I am not able to tell that yet. I will learn that soon."    
    

# Take user input 


while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break