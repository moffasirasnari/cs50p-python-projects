#inputs for names to user (assume user will enter atleast on name)
#until presses control d (EOFError)
#print Afieu,adieu,to {names}
#seperate two names with one and
#three names with 2-commas & one and
name_list =[]
def main():
    name_list = name()
    print()
    goodbye(name_list)


def name():
    try:
        while True:
            name = input("Name: ")
            name_list.append(name)
    except EOFError:
        return name_list


def goodbye(s):
    run_once = True
    if len(s)==1:
        print(f"Adieu, adieu, to {s[0]}")
    elif len(s)==2:
        print(f"Adieu, adieu, to {s[0]} and {s[1]}") #cuz in only 2 names there should be no comma before "and"
        #eg: Rohan and Mohan not Rohan, and Mohan
    else:
        for i in range(len(s)):
            if i< len(s)-1:
                if run_once == True:
                    print(f"Adieu, adieu, to ",end="")
                print(f"{s[i]}, ",end="")
                run_once = False
            else: print(f"and {s[i]}",)
        #eg: Rohan, Mohan, and Sohan
main()
