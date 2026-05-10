#a program that takes a command line arg for no. of bitcoin user want to buy
#if that arg can't be converted into float > exit
#if no arg , print missing command line arg
#if wrong arg , prnint command line arg is not a number
#output total cost upto 4 decimal places
import requests , sys,os
from decimal import Decimal
#sys.argv= [os.path.basename(__file__),"2"] #auto arg assigning
try:
    #check for correct arg
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        try:
            qnt = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)

    #access API
    api_key = "629c70a77c109b7dff9d0b343029c1a025566d1f51fc895ccd07d83c2dbc1470"
    cost = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
    #converting response in json text format
    cost = cost.json()

    #get current price of 1 bitcoin
    #there's dict called data with a key "priceUsd"
    price = Decimal(cost["data"]["priceUsd"]) #get bitcoin cost in float value
    #print(price)
    total_cost = Decimal(f"{price*Decimal(qnt):.4f}")

    #print output
    print(f"${total_cost:,}")



    #print(json.dumps(cost.json(),indent=2))


except requests.RequestException:
    sys.exit()
