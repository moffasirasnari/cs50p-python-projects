#rock,paper,scissor game
#there Will be 6 rounds
#if tie -> there will be special round
import random

game = ["rock","paper","scissor"]
print("Rock, Paper, Scissor Game..")
name = input("Enter your name: ").strip().capitalize()
print(f"Hello,{name} :) \n"
      "There will be 6 round ,A special round in case of Tie\n"
      "Let's Start the game")
user_score = 0
syst_score = 0
for _ in range(6) :
    i = random.randint(0,2)
    syst_guess = game[i]
    print(f"(computer guess:{syst_guess})" )
    user_response = input("Rock, Paper, Scissor....").strip().lower()
    
    
    if syst_guess == "rock" and user_response== "paper":
            user_score +=1
            print("Hurrah!, You Won it \n"
                  "Computer score : Your score \n"
                  f"{syst_score}  : {user_score}")
    
    elif syst_guess == "paper" and user_response== "scissor":
            user_score +=1
            print("Hurrah!, You Won it \n"
                  "Computer score : Your score \n"
                  f"{syst_score}  : {user_score}")
            
    elif syst_guess == "scissor" and user_response== "rock":
            user_score +=1
            print("Hurrah!, You Won it \n"
                  "Computer score : Your score \n"
                  f"{syst_score}  : {user_score}")   
    elif syst_guess == user_response:
        print("Same: ")
        continue
    else :
        syst_score +=1
        print(f"You Lost (Computer guess was {syst_guess})\n"
              "Computer score : Your score \n"
              f"{syst_score}  : {user_score}")
        
if user_score == syst_score:
    print("Game Over \n"
          "Computer score : Your score \n"
          f"{syst_score}  : {user_score} \n"
          "Oh no!, It's a Tie!\n"
          "SPECIAL ROUND!")
    user_response = input("Rock, Paper, Scissor....").strip().lower
    i = random.randint(0,2)
    syst_guess = game[i]
    print(f"(computer guess:{syst_guess})" )
    if syst_guess == user_response:
         user_score +=1
         print("Hurrah!, You won \n"
              "Computer score : Your score \n"
              f"{syst_score}  : {user_score}")
    else :
        print(f"Oh no!, You lost (Computer guess was {syst_guess})\n"
              "Computer score : Your score \n"
              f"{syst_score}  : {user_score}")
        

else :
     print("Oh no!, You lost"
              "Computer score : Your score \n"
              f"{syst_score}  : {user_score}")
    