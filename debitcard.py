"""
card_no = input("enter your card number with 4 spaces ")
split = card_no.split(" ")

# count = 0
# for i in card:
#     count += 1
#     card[count] = "****"
split[0] = "****"
split[1] = "****"
split[2] = "****"
joined = "".join(split)
print(joined)

card = input("pls enter your card number with spaces included ").replace(" ","")
output = "" #this is mostly used when you want to replace value of a sequence
count = 0
for i in card:
    if len(card)>15:
            count += 1
            if count<=12 :
                output += "#"
            else:
                output += i

    else :
        print("you enter the wrong amount of  digits.")
        break
print(output)


"""
card = input("pls enter card number with spaces after each 4 digits! ").replace(" ","")
print(card)
output = ""
count = 0
for i in card:
    count += 1
    if len(card) == 16:
        if count < 13:
            output += "#"
        elif count>12 :
            # -1 one was added because it counts 0-15 not 1-16 
            output += card[count-1]
else:
    print("incorrect input")
           # card[count] = "*" 'str' object does not support item assignment

print(output)









