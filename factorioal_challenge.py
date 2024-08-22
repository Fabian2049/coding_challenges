def factorial (number):
    # number = int(input("enter input \n"))
    factori_al = 1
    while number > 1:
        # notice how the multiplication happens before the decrement, there factori_al is already 4 before
        #first decrement
        factori_al *= number
        number -= 1
    print("number is :", factori_al)   
        
    if number == 0:
            print(f"your factorial is 1")


user_in_put = int(input("pls enter a non-negative integer \n"))
factorial(user_in_put)
