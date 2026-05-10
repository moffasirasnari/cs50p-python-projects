#game having moves (up,down,right,left )
#take input from user and store it in a list
#make a feature of undoing the move-->rm the move from list
#print the history at users will/input= end/stop/history


def main():
    history = []
    print("Welcome to the game✨\n"+
          "You can move up, down, right & left ")
    while True: #created an infinte loop
        move = input("Enter the move? ").strip().lower()

        match move :       #works same as if but can equate with multiple values
            #undo feature
            case "undo":
                history.pop()
                undone = history.pop()
                print(f"undone: {undone}")

            #ending the game and showing history
            case "stop" | "end": #like here no need of and, or
                print("Thank You for playing. ")
                print(history)
                break

            #printing history
            case "history":
                print(history)

            #storing moves
            case "up" |"down" |"right" |"left":
                 history.append(move)
            case _:
                print("wrong move! ")



main()
