#report making of user's preferred spacecraft

def main():
    spacecraft = [{"name":"voyager1","distance":"500",
                  "condition":"all sensor fine"},
                  {"name":"voyager2","distance":"200",
                  "condition":"just in contact"}]
    #take user's input and convert in required format
    users_input= input("Name of spacecraft? ").strip().lower().replace(" ","")
    #to get a dictionary from the list spacecraft
    for i in spacecraft:
        #if users_input matches value of key("name") in any dictionary
        if users_input == i["name"]:
                #sends that dictionary to report()
                print(report(i))

                user_input = input("Want another ?.(y/n) ").strip().lower()
                if user_input in ["yes","y"]:
                        continue
                else :
                      print("OK,Good Bye! ")


        else :
              print("No data found! ")

def report(dict):
        return f"""
==============Report====================

   Name:{dict.get("name")}
   Distance:{dict.get("distance" , "Unkown")} AU
   condition:{dict.get("condition", "Unknow")}

========================================
"""
#.get("1","2") checks the value of key(1) if not found gives value(2)





main()


