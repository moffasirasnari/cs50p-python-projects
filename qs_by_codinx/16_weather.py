#output weather based on infor given by user

def main():
    temp = take_input("temperature")
    humd = take_input("humidity")

    if temp >=30 and humd<=90:
        print("Hot and Humid")
    elif temp >=30 and humd<90:
        print("Hot")
    elif temp <30 and humd>=90:
        print("Cool and Humid")
    elif temp <30 and humd<90:
        print("Cool")
   
    
def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue

main()