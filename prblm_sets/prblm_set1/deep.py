#asking user ans to great question of life..


answer = input("What is the answer of the great Question of life,the Universe, and Everything? ").lower().strip()

#using match
match answer :
    case "forty two" | "forty-two" | "42" :

        print("Yes")
    case _:   # _ used to denote other except upper strings
        print("No")


