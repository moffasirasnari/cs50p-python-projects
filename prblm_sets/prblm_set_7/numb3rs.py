#a programme that validates the IPv4 address
#its in format #.#.#.# 
# # is a number btw 0-255 inclusive
import sys,re
def main():
    print(validate(input("IPv4 Address: "))) 

    # if valid:= re.search(r"(?:[0-9]\.){3}",ip): #{n} = n total repitions checked
    #     print("True")

    # else: print("False")



def validate(ip):

    valid= re.search(r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})",ip) #{n} = n+1 total repitions checked
    print(valid.groups())
   
    
    # else: print("False")
main()