#leap year checker
#divisible by 4 but not 100
#but also divisible by 400
year = int(input("Enter the year: "))

if (year % 4==0 and year % 100 !=0) or year % 400 ==0 :
    print("It's a Leap year :) ")
else : print("It's not a Leap year")
