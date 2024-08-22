def restart():            
        start = input("Do you wish to start again !! Y/N ").upper()
        if start == "Y" or start == "YES":
            game()
        elif start == "N" or start == "NO":
            print("it was nice having you!!")
        else:
            print("invalid response")
            restart()
def game():
    print("GUESS THE NUMBER!!! \n")
    print("INSTRUCTION !!: Guess any numbrt from 1 - 20")
    chances = list(5*"#")
    remains = 5 
    guessed = False
    mistake = 1 
    while not guessed and mistake < 6:
        number = int(input("Enter number."))
        remains -= 1
        chances[mistake-1] = "_"
        if number in range(1,21):
            if number == 15 :
                guessed = True 
                # print(f"Congratulations you guessed correctly !!!")
            elif number <= 10:
                mistake += 1
                print("You guessed too low ")
                print(f"you where wrong you have {remains} chances left {chances}")
            elif number >15 :
                mistake += 1
                print("You guessed too high")
                print(f"you where wrong you have {remains} chances left {chances}")
            elif number>=11 :
                mistake += 1
                print("You are very close")
                print(f"you where wrong you have {remains} chances left {chances}")
        else:
            mistake += 1
            print(f"Number you entered is out of range, ou have {remains} chances left {chances} ")
    if guessed:
        print(f"Congratulations you guessed correctly !!!\n")
        restart()          
       
    else:
        print("you exhauste all your trials !!")
        restart()

    return remains,guessed,mistake

# re_game = 

r,g,m = game()

print(r)
print(g)
print(m)




