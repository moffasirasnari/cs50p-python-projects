#take input 3 angles
#check if can form a triangle i.e total angle==180 degree

def main():
    i = 0
    angle1= get_angle(i)
    angle2= get_angle(i)
    angle3= get_angle(i)

    if (angle1 +angle2 +angle3)== 180:
        print("Triangle can be formed :) ")
    else : print("Triangle Can't be formed ")

def get_angle(i):
    i +=1
    while True:
        try:
            return int(input(f"Enter Angle {i}: "))
        except ValueError:
            print("Enter Valid Angle: ")
            continue

main()
