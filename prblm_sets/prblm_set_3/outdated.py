#input in format MM/DD/YYYY 9/8/1636 or September 8, 1636
#utput that same date in YYYY-MM-DD format
# If the user’s input is not a valid date in either format, prompt the user again
#Assume that every month has no more than 31 days
#no need to validate whether a month has 28, 29, 30, or 31 days.
month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ")
        try: #try for x/y/z format
            # if not in / format, in mm(name) dd, yyyy format == value error
            m,d,y= date.split("/")
            #checking is all digits else continue
            if m.isdigit() and d.isdigit() and y.isdigit():
                d,m = int(d),int(m)
                if m<= 12 and d<= 31 :
                    print(f"{y}-{m:02}-{d:02}")
                    break
                else : continue
            else : continue
        #if not then try mm(name) dd, yyyy format
        except ValueError:
            if date[0].isalpha() and "," in date:  #checks if mm dd format or dd(not alphabet) mm format
                m,d,y=date.split()
                d=int(d.replace(",",""))
                if m.capitalize() in month and d<= 31:
                    m=month.index(m.capitalize()) + 1
                    print(f"{y}-{m:02}-{d:02}")
                    break
            else : continue
main()
