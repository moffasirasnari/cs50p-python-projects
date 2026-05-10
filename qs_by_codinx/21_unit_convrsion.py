#unit conversion
#Enter reverse to reverse converter
conversions =[["cm-ft",0.03,30.48,"cm","ft"],
              ["km-miles",0.62,1.6,"km","mile"],
              ["usd-inr",94,0.011,"USD","INR"]]
# 1st(not 0th) index of 1st list is for cm-ft conversion,2nd index is for ft-cm
#same for others

def main():
    n=0
    print("Converters Available:>")
    for i in conversions:
        print(f"{n+1}-->{i[0]}") #prints list of converters
        n+=1
    #take input to choose converter
    convt=take_input(f"converter?(typer their s.no.)")
    print("(can enter rev to reverse converter)")
    unit_convtr(convt)

def take_input(s): #take input untill integer
    while True:
        try:
            num = int(input(f"Enter {s}: "))
            if num<= len(conversions):
                return num
            else: 
                print("Enter valid input!")
                continue  
        except ValueError:
            print("Enter valid input!")
            continue


def unit_convtr(s): #one func for all conversions:)
    while True:
        num = input(f"Enter value({conversions[s-1][3]}): ").strip().lower()
        if num == "rev":
            try:
                num =int(input(f"Enter value({conversions[s-1][4]}): "))
                num = num*conversions[s-1][2]
                return print(f"{num}{conversions[s-1][3]}")
            except ValueError:
                print("Enter valid input!")
                continue
                
        else:
            try:
                num2 = int(num)*(conversions[s-1][1])
                return print(f"{num2}{conversions[s-1][4]}")
            except ValueError:
                print("Enter valid input!")
                continue


main()
