#fuel in fraction to percentage calculator
#if  fuel <=1% print E
#if fuel >= 99% print F
#handle Valueerror & division by zero error

def main():
    while True:
        fraction= input("Fraction: ")
        try:
            x,y=fraction.split("/") #splitting numbers 
            percentage = round((int(x)/int(y))*100)
            if int(x)>int(y) or int(x)<0:
                continue
            break
        except (ZeroDivisionError,ValueError):
            pass
    if percentage<= 1:
        print("E")
    elif percentage>=99:
        print("F")
    else: print(f"{percentage}%")
main()

