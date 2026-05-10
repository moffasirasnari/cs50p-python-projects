# tell no. of dog and chickens from no. of legs and heads
import sys
def main():
    heads = take_input("no. of Heads")
    legs = take_input("no. of Legs")

    #let dogs=x , chickens=y
    #eq1  4x+2y = legs , eq2: x+y=heads
    try: #to check if no. of chikens is not a fractional no.
        y = (4*heads-legs)/2      

        #1st learn OOP then complt :> will learn to check if y is decimal or not


        x= heads-y   #if y= int then x also int
    except ValueError:
        print("Not possible! ")  
        sys.exit()
    print(f"Dogs= {round(x)}\n"
          f"Chickens= {round(y)}")




def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue


main()