#Guess the number game :
#player will have 5 chances
#system will gen a random number each time
#is guessed = 5 points , else 0
#print total points
import random
name = input("Enter your name: ").strip().capitalize()
print(f"Hello,{name} :)\n"
"Rules : 1. You'll have 5 chances\n"
"        2. Correct guess = 5 poinst\n"
"        3. Wrong guess = 0 points\n"
"Let's start the game :)")
Points = 0
for i in range(5) :
    
    player_guess=int(input("Guess the no. btw 1 to 10 : "))
    sys_guess = random.randint(1,10)
    if player_guess == sys_guess:
        Points = Points + 5
        print(f"Hurrah! You are Correct , Total points ={Points}")
        continue
    else  :
        print("Nope!, Bad Luck\n"
              f"Actuall no.={sys_guess}")
    
print("That's the game, Turn over\n"
      f"your total score is {Points}\n"
      "Thank's for playing :)")