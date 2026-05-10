#volume of milk cylinder finder
#also cost of milk finder(1L = 40rs)
#v = pi*r**2*h
def main():
    r = take_input("radius(cm)")
    h = take_input("height(cm)")
    v = round(3.14*(r**2)*h,1)
    # 1 cm cube = 1ml
    v_in_litre = v/1000
    print(f"Total volume is {v}ml, i.e {v_in_litre}L")
    #1l milk = 40Rs
    cost = round(v_in_litre*40)
    print(f"Cost of milk is {cost}Rs")
def take_input(s):
    while True:
        try:
            return int(input(f"Enter {s}: "))    
        except ValueError:
            print("Enter valid input!")
            continue
main()