import random

greetings = ['hello', 'hi', 'Hi', 'hey!','hey']

questions = ['how are you', 'how are you?', 'How are you?',
            'how are you doing', 'how are you doing?',
            'How are you doing?']
responses = ['Okay',"I'm fine"]

farewells = ['goodbye', 'bye', 'farewell']

while True:
    
    userInput = input(">>> ")
    if userInput in greetings:
        print(random.choice(greetings))
    elif userInput in questions:
        print(random.choice(responses))
    elif userInput in farewells:
        print(random.choice(farewells))
        exit()
    else:
        print("I did not understand what you said")
