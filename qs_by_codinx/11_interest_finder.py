#simple interest finder

def main():
    p = take_input("Principal(rupees)")
    r = take_input("Rate(%)")
    t = take_input("Time(years)")
    simple_interest = round((p*r*t)/100,1)
    print(f"Your simple interest is {simple_interest}Rs")

def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue

main()        