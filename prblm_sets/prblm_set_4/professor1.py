# prompt for level 1,2,or 3 (used to determine no. of digits in x,y)
# a calculator that will gen 10 diff math problem
# in format only addn x + y ,(x,y= non -ve)
# x,y should be gen in pairs
# if ans false = print EEE & reprompt(three trials per qs)
# if all 3 wrong = output correct ans & continue
# print score out of 10 .
import random

score = []


def main():
    level = get_level()  # get level of game
    for i in range(10):  # print 10 diff math qs
        x, y = generate_number(level)
        ans = x + y
        ans_check(ans, x, y)
    final_score = score.count(
        "T"
    )  # count final score by counting T(true) in list score
    print(f"Score: {final_score}")


def ans_check(ans, x, y):
    i = 0
    while i < 3:  # gives 3 attempt per qs
        user_ans = input(f"{x} + {y} = ")  # take user answer
        try:
            if ans == int(user_ans):
                score.append("T")  # adds T in score for Correct ans
                return
            else:
                i += 1
                print("EEE")  # for wrong nueric value
                continue
        except ValueError:  # exception also accounts for 1 wrong ans
            i += 1
            print("EEE")
            continue
    print(f"{x} + {y} = {ans}")
    score.append("F")  # if all wrong ans then add F in score
    return


def get_level():  # returns level of game
    while True:
        try:
            level = int(input(f"Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_number(level):  # gen random x,y based on level
    if level == 1:
        x, y = random.randint(0, 9), random.randint(0, 9)
        return x, y
    elif level == 2:
        x, y = random.randint(10, 99), random.randint(10, 99)
        return x, y
    else:
        x, y = random.randint(100, 999), random.randint(100, 999)
        return x, y


main()
