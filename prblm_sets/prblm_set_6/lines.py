#a programs that executes ecatly one cli arg
#can be name or path of a python file
#it outputs the no. of lines of codes in that file
#lines must exclude the comments and blanks lines
#sys.exit if file does not exist,not end with .py or >1CLI arg
import sys

#checking file for conditions of validity
def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not file_name.endswith(".py"):
        sys.exit("Not a python file")


    print(num_line(file_name))

#check no. of lines
def num_line(s):
    try:
        with open(s,"r") as file:
            #lines = file.read()  #wrong only returns whole file as a single str
            lines = file.readlines()
            #remeb there are to fn readline reads only one line at a time,
            #readlines loads all lines as a list

    except FileNotFoundError:
        sys.exit("File does not exist")

    total_num_line = 0
    for line in lines:
        if line.startswith("#") or line.isspace():
            continue

       #checking for comments after spaces
        elif line.strip().startswith("#"):
            continue
        total_num_line+=1
    
    return total_num_line

if __name__=="__main__":
    main()
