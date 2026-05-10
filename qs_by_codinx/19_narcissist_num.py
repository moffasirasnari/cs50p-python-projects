#cheking narcissist number for 4 digit number input
#narcissist num = sum of (digits to power no. of digit=no. itself

def main():
    num= take_input("a four digit number")
    sum_num=0
    for i in range(4):
        sum_num += int(str(num)[i])**4 
    if sum_num ==num:
        print("It's a narcissist number: ")
    else : print("It's not narcissist number: ")


def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue

main()