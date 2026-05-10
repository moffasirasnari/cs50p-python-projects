#Guess the no. game
#sys will gen a random no.
#player will have 3 chances to guess it
#if guess, +5 points & game continues
#if cant guess in all 3 chances , game ends

import random , sys 

name = input("Enter your name: ").strip().capitalize()
print(f"Hello,{name} :)\n"
"Rules : 1. You'll have 3 chances to guess the no.\n"
"        2. Correct guess = 5 poinst\n"
"        3. Wrong guess = Game ends\n"
"Let's start the game :)")
Points = 0
while True :
    sys_guess = random.randint(1,10)
    print(f"random no. is {sys_guess}")
    for i in range(3) :
        player_guess = int(input("Guess the number: "))
        
        
        total_poinst = Points
        if player_guess== sys_guess:
            Points = Points + 5
            print(f"Hurrah! You guessed it, Total points: {Points}")
            break 
        else :
            print("Sorry,Try again")
            continue   
    #if guessed in any of 3 chances then total_points != points
        #as for loops breaks and moves out without updating total_points
    #if not guessed in any of 3 chances then total_points = points     
    if total_poinst == Points:
        print("Bad Luck, Game's Over\n"
          f"Total points: {Points}")
        break
    else :
        response= input("Want to continue? (y/n)" ).strip().lower()
        if response == "y" or response == "yes":
            continue 
    #move back to while loop , syst will guss again and game continues
        else :
            print(f"Total points: {Points}")
            break
        
