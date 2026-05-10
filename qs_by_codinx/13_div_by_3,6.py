#check is divisible by 3 and 6 or not


def main():
    number  = take_input("number") 
    div_checker(number)
    
def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue

def div_checker(s):
    sum = 0
    for  i in str(s):
        sum += int(i)
    if sum % 3 ==0 and s % 2 ==0 :
        return print("Divisible by both 3 & 6 :)")
    elif sum % 3 ==0:
        return print("Only divisible by 3 ")
    else :
        return print("Not divisible by any")
    
main()    
