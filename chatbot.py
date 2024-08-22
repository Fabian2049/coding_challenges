import random
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "Hey",
    "How is your day",
    "Hello, Talk to you later",
    "wassup",
    "Be right back"
]
print("HEYY THERER I AM YOUR PERSONAL CHATBOT..LETS TALK \n")
talk = input("Type anything .....\n")
answer = random.choice(conversation)
if talk.lower() == answer.lower():
    change_answer = random.choice(conversation)
    print(change_answer)
else:
    print(answer)



# while len(talk) >= 1:
#     answer = random.choice(conversation)
#     print(answer)
#     talk = input("Type anything ..")


# write your code below