#Coke Machine
#price of 1 coke 50 cents
#can only accept 25,10,5 cents coin
coins_acceptable=[25,10,5]
amount_due= 50
while True:

    print("Amount Due:",amount_due)
    payment= int(input("Insert Coin: "))
    #checks if coin is acceptable or not
    if payment in coins_acceptable:
        #calculates remaining amnt
        amount_due = amount_due-payment
        if amount_due <0:
            #calculate owed amnt
            print("Change Owed:",(-1)*amount_due)
            break

        elif amount_due==0:
                print("Change Owed:",amount_due)
                break


