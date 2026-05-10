#take three digit
#add square of each digits

def main():
    x = take_input("1st digit")
    z = take_input("2nd digit")
    y = take_input("3rd digit")
    
    square_sum = x**2 + y**2 + z**2
    print(square_sum)

def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue
main()