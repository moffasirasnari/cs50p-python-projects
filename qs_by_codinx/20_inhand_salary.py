#calc inhand salary after deducting
#HRA=10% , DA=5%, PF=3%
#assuming tax is done on remaining amnt after deducting upper things
#if salary 5-10lakh, -10%
#          11-20l,   -20%
#          >20 -30%
 
def main():
    s = take_input("Annual salary(in Lakhs)")

    s = s - (s/10 +s/20 +(3*s/100))
    if s<=5:
        print(f"In-Hand salary {round(s,1)} Lakhs")
    elif  s<=10:
        print(f"In-Hand salary {round(s-s/10,1)} Lakhs")
    elif  s<=20:
        print(f"In-Hand salary {round(s-s/5,1)} Lakhs")
    else:
        print(f"In-Hand salary {round(s-3*s/10,1)} Lakhs")


def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue
main()