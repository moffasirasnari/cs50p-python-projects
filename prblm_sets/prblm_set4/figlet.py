#implement a program that:
#Expects zero or two command-line arguments
#Zero if the user would like to output text in a random font.
#Two if the user would like to output text in a specific font,
# in which case the first of the two should be -f or --font,
# and the second of the two should be the name of the font.
#Prompts the user for a str of text.
#Outputs that text in the desired font.
import pyfiglet, sys

def main():
    if len(sys.argv)==1: #if user gave no argument
        font = input("Input: ")
        print(pyfiglet.figlet_format(font))

    elif len(sys.argv)==2 or sys.argv[1] not in ["-f","--font"]: 
            sys.exit(2)

    elif len(sys.argv)==3 and sys.argv[1] in ["-f","--font"]: #user must give two arguments (len=3)
        if sys.argv[2] not in pyfiglet.FigletFont.getFonts(): #checking if font exists in module
            sys.exit(1)
        font = input("Input: ")
        print(pyfiglet.figlet_format(font,font=sys.argv[2]))


main()

