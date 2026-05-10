#a programmer that shows the selected menu in a tabular format
#using tabulate package

import sys
from tabulate import tabulate

#checking file for conditions of validity
def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")


    print(tabular_menu(file_name))


def tabular_menu(s):
    try:
        with open(s,"r") as file:
            menu = file.readlines()
            #header = file.readline().rstrip().split(",")
            #it's wrong as the pointer in file is already reached at end
            #due to readlines which red all line already thus readline returns blank list
            #python reads file sequencially
            header = menu[0].rstrip().split(",")  #no need if csv already has a header
    except FileNotFoundError:
        sys.exit("File does not exist")
    table=[]
    for line in menu:
        table.append(line.rstrip().split(","))
    table.pop(0)
    # print(header)
    return tabulate(table,header,tablefmt="grid")

if __name__=="__main__":
    main()
