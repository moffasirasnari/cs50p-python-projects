# modified in cs50p req format... earlier code was also corect
# improved version
import random


def main():
    score = 0  # no need to store in list
    # call get level
    lvl = get_level()
    # get the score
    for i in range(10):
        x, y = generate_number(lvl)

        ans = x + y
        for j in range(3):  # no need that while loop
            try:
                user_ans = int(input(f"{x} + {y} = "))
                if user_ans == ans:
                    score += 1
                    break
                else:
                    raise ValueError  # no need of double writing same code
            except ValueError:
                print("EEE")  # both else and sception are addressed here
                pass
        if j == 2:
            print(f"{x} + {y} = {ans}")
            continue
    # print
    print(f"Score: {score}")


def get_level():  # returns level of game
    while True:
        try:
            level = int(input(f"Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_number(level):  # gen random x,y based on level
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
