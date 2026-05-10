#programme that takes 3 cla
#both csv file
#1st- name of file to read(assumed to in order name,house)
#2nd-file to write data in format(first,last,house)
#assume each student have both first & last name
import sys,csv

#checking file for conditions of validity
def main():
    try:#taking CLA
        old_file = sys.argv[1]
        new_file = sys.argv[2]

    except IndexError:
        sys.exit("Too few command-line arguments")

    if len(sys.argv)>3: # for >2 CLA
        sys.exit("Too many command-line arguments")
    #checking for file type
    elif (not old_file.endswith(".csv") and
    not new_file.endswith(".csv")):
        sys.exit("Not a CSV file")

    data = old_file_data(old_file)
    create_new_file(new_file,data)

def old_file_data(s):
    try: #getting the old file
        with open(s,"r") as file:
           old_file = file.readlines() #would be better if had used dictreader->each row as sep dict.
    except FileNotFoundError:
        sys.exit("File does not exist")

    # print(old_file)
    new_file_data=[]  #will store the data of old file formatted for new file
    #adding heading on first line
    new_file_data.append(["first","last","house"])
    for i in old_file:
        if i != old_file[0] : #leaving the heading
            #removing comman & splitting name
            last,first,house = i.rstrip().strip().replace('"','').split(",")
            first = first.strip() #removig the leading whitespaces
            new_file_data.append([first,last,house])
    return new_file_data



def create_new_file(new,data): #creating new req format file

    with open(new,"w",newline="") as file: #creating new file if not exist
        #newlinw ->this will stop csv from adding a new line.
        new_file = csv.DictWriter(file,fieldnames=["first","last","house"]) #assigning columns name

        for i in data:
            new_file.writerow({"first":i[0],"last":i[1],"house":i[2]})
            #here python is adding new line but also csv is also adding a new
            #resulting in a blank line.

if __name__=="__main__":
    main()
