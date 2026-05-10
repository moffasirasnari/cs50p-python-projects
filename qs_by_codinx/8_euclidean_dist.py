#finding euclidean distance between two points
#euclidean distnce = straight line distance btw 2 pointw
#user exit-> ctrl+d
#handles eoferror,valueerror,typeerror
import sys

def main():
    while True:
        try:
            coordinate1=input("Enter 1st coordinates(x,y,z): ")
            x,y,z=coordinate1.split(",")
            x,y,z=int(x),int(y),int(z)
        except EOFError:
            print("")
            sys.exit()
        except (ValueError,TypeError):
            print("Enter valid coordinates,\n"
                  "numbers sep with commas,\n "
                  "with all three coordinates")
            continue
        while True:
            try:
                coordinate2=input("Enter 2nd coordinates(p,q,r): ")
                p,q,r=(coordinate2.split(","))
                p,q,r=int(p),int(q),int(r)

            except EOFError:
                print("")
                sys.exit()
            except (ValueError,TypeError):
                print("Enter valid coordinates,\n"
                    "numbers sep with commas,\n "
                    "with all three coordinates")
                continue
            break
        break
    distance_ = round(distance(x,y,z,p,q,r),2)

    print(f"Distance is {distance_} units")
def distance(x,y,z,p,q,r):
    return (((p-x)**2 + (q-y)**2 + (r-z)**2)**(1/2))

main()
