#input cost price and selling price
#determine if it's loss and profit
#also show percentage loss / profit

def main():
    cost_price = take_input("Cost Price")
    selling_price = take_input("Selling Price")

    profit_loss_checker(cost_price,selling_price)

def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s} (In Rupees): "))
        except ValueError:
            print("Enter only numbers: ")
            continue

def profit_loss_checker(x,y):
    if x > y :
        print("It's a Loss: ")
        loss = x-y 
        loss_percent= round((loss/x)*100,1)
        print(f"You'll lose {loss} rupees, i.e {loss_percent}% loss")
        return
    elif x<y:
        print("It's a profit: ")
        profit = y-x 
        profit_percent= round((profit/x)*100,)
        print(f"You'll profit {profit} rupees, i.e {profit_percent}% profit")
        return
    else: 
        print("No loss, No profit.")
        return
    

main()