#asks for input of items,one per line
#handel ctrl+d:EOFError
#output users grocery list in :
#all uppercase
#alphabatically ordered
#prefixing each item with no. of time user entered it (Qntity)
grocery_list = {}

def main():
    while True:
        try:
            grocery = input().strip().upper()
        except EOFError: #is user uses ctrl+d to exit
            break
        list_maker(grocery)

    output(grocery_list)


def list_maker(item):
    quantity = 1

    if item in grocery_list.keys():
        quantity= quantity+1
        grocery_list[item] = quantity #increase quantity of existing item
        return grocery_list

    grocery_list[item] = quantity #adds new item and its quantity(1)
    return grocery_list


def output(list):

    for i in sorted(grocery_list): #sorts list alphabatically
        print(grocery_list[i],i)  #prints result quantity with item name

main()

