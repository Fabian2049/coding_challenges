transactions = [200, 455.23, -306.5, 25000, -642.21, -133.9, 79.97, 1300, 5000, 3400, -150, -790, -3210, -1000, 8500, -30]
sum = 0
for i in transactions:
    if i < 0:
        sum += i
        print(f"You have been debited with ${abs(i)}")
    else:
        sum += i
        print(f"You have been credited with ${i}")
    print(f"Your account balance is ${sum}")
    print("\n")



