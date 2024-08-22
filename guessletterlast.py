import random
word_list = ["bannann","feiinnoal","repititive","anxiouslly","credibiblityyyyald"]

def chosen_func ():
    choosen = random.choice(word_list)
    return choosen

def user_display():
    chosen_main = chosen_func()
    harsh_display = list(len(chosen_main) * "*")
    harsh_display[0] = chosen_main[0]
    harsh_display = "".join(harsh_display)
    return harsh_display

def play_game ():
    word = chosen_func()
    display = user_display()
    print(f"Welcome to guess_letter game, you have 5 trials,\n this is the word you are to guess!  {display} \n")
    trials = 5
    first_timer = 1
    guessed = False
    guessed_before = []
    while not guessed and trials != 0:
        user_input = input("Pls enter the correct character required to fill the gap  \n")
        if user_input in guessed_before:
            print("YOU HAVE GUESSED THIS LETTER BEFORE")
        elif user_input.isalpha() == True and len(user_input) == 1:
            guessed_before.append(user_input)
            if user_input in word:
                index_of_userinput = [i for i,letter in enumerate(word) if user_input == letter]
                for index in index_of_userinput:
                    new_display = list(display)
                    new_display[index] = word[index]
                    new_display = "".join(new_display)
                print(f"You Guessed Correctly!!, your current progress is {new_display} ")
                if "*" not in new_display:
                    guessed = True
            else:
                trials  -= 1
                print(f"Sorry the letter you entered was not part of the word, you have {trials} left")

                if trials == 0:
                    print("You have exhausted all your trials")
        
        else:
            if first_timer == 1:
                print("Incorrect input pls enter a valid input")
                first_timer -= 1
            else:
                print("Incorrect input pls enter a valid input")
                trials -= 1
                print(f"You have {trials} left ")

play_game()

    