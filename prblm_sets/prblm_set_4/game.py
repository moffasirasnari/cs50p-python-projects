#prompt for a level n(+ve) else again rpompt
#randomly gen a number btw 1,n inclusive
#user guess if not +ve --> ask again
#if guess<n = "Too small!"
#if guess>n = "Too large!"
#guess = n "Just right!"

import random , sys
def main():
    level = take_input("Level")
    sys_guess =random.randint(1,level)

    while True:
        guess =take_input("Guess")
        if guess == sys_guess:
            print("Just right!")
            sys.exit()
        elif guess > sys_guess:
            print("Too large!")
        else:
            print("Too small!")


def take_input(s):
    while True:
        try:
            level= int(input(f"{s}:"))
            if level >0:
                return level
            else : continue
        except ValueError:
            continue

main()
