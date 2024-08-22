def percentage(discount : int):
    def shopping_process():
        # why does this flag an error when i use non local instead of global
        quantity_p = quantity_s = quantity_x = 0
        print(f"we have   PS5 - 500 \n XBOX - 600 \n SWITCH - 4000 \n")
        
        def carting():
            nonlocal quantity_p,quantity_x,quantity_s
            continue_carting = False
            while not continue_carting:
                cart = input("Pls enter the name of the exact product you wish to purchase ").lower()
        
                if cart == "ps5":
                    quantity_p += int(input("enter the qunatity you wish to purchase "))
                elif cart == "xbox":
                    quantity_x += int(input("enter the qunatity you wish to purchase "))
                elif cart == "switch":
                    quantity_s += int(input("enter the qunatity you wish to purchase "))
                else:
                    print("invalid input")
                    go_agian = input("Are you sure you want to continue ").lower()
                    if go_agian == "yes":
                        carting()
                    else:
                        print(f"you cant continue from here")
                        continue_carting = True
                # check this line very well
                ask_again = input("do you wish to order more? ").lower()
                if ask_again == "yes":
                    carting()
                else:
                    continue_carting = True

        carting()
    
        ps5 = 500
        xbox = 600
        switch = 4000

        norm_cp_p = quantity_p * ps5
        norm_cp_s = quantity_s * switch
        norm_cp_x = quantity_x * xbox

        total_cp = norm_cp_p + norm_cp_s + norm_cp_x
        the_discount = (discount/100) * total_cp
        discounted_cp = total_cp - the_discount

        print(f"You purchased {quantity_p} ps5 - {norm_cp_p} \n {quantity_s} swhitch - {norm_cp_s} \n {quantity_x} xbox - {norm_cp_s}")
        print(f"your total was {total_cp} buh After adding up your discount you get it at {discounted_cp}")  

        return"thank you for using our mall"
    # this return statement very very important!!
    return shopping_process

ask = float(input("Enter preferred discount "))
function_1 = percentage(ask)
shoping = function_1()
