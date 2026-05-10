#standard compound interest calculator
# assuming interest compound anually only
# formula used == A = P (1 + R/100)^T
#Compound interest = A-P

def main():
    p = take_input("Principal amount")
    r = take_input("Rate(annually)")
    t = take_input("Time(years)")
    compound_interest = round(p*((1 + r/100)**t))
    print(compound_interest)

def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue
main()