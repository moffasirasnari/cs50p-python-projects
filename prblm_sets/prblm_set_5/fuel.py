#fuel in fraction to percentage calculator
#if  fuel <=1% return E
#if fuel >= 99% return F
#handle Valueerror & division by zero error

def main():
    while True:
        fraction= input("Fraction: ")
        try:
            percentage=convert(fraction)
            print(gauge(percentage))
        except (ValueError,ZeroDivisionError): #this is how you handle errors from all fns by raising
                                            #error there and handling them here
            continue
def convert(fraction):
        try:
            x,y=fraction.split("/") #splitting numbers
            x,y = int(x),int(y)
        except (ValueError,AttributeError):
            raise ValueError #this error will be handeled in main

        if y==0:
            raise ZeroDivisionError  #similarly this & others
        if x>y or x<0 or y<0:
            raise ValueError

        return round((int(x)/int(y))*100)

def gauge(percentage):
    if percentage<= 1:
        return "E"
    elif percentage>=99:
        return "F"
    else: return f"{percentage}%"

if __name__=="__main__":
    main()
