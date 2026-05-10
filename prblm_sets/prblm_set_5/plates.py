#Number plate checker
#plates must start with at least two letters.
#plates may contain a maximum of 6 characters (letters or numbers)
#and a minimum of 2 characters
#Numbers cannot be used in the middle of a plate; they must come at the end
#The first number used cannot be a ‘0’
#No periods, spaces, or punctuation marks are allowed.
import string
def main():
    plate = input("Plate: ")
    if is_valid(plate)==True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #length must be btw 2 and 6
     if not 2<=len(s)<=6:
         return False
    #first two elem must be str
     elif not s[:2].isalpha():
         return False
     #check is whole str is made of letters
     elif s.isalpha():
          for i in range(len(s)):
               #these should not be present in str
               return s[i]!="_" and s[i]!=" " and  s[i] not in string.punctuation

     #str is alphanumeric

     run_once = True #to check if first number is 0 or not
     if s[-1].isdigit(): #checks if last elment is digit or not
          for i in range(2,len(s)-1):
               #now if any elment in str is digit then the next one must be digit
               if s[i].isdigit() :
                    if run_once==True and s[i]=="0":
                         return False
                    elif s[i+1].isdigit() :
                         run_once=False
                         continue
                    else: return False
               elif s[i].isalpha() :
                    continue
          return True


     else: return False
               #so, str is alphanumeric but last elment i not digit->invalid


if __name__=="__main__":
     main()

