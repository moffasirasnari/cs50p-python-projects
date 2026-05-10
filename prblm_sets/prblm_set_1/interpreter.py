# math interpreter or calculater
exprsn = input("Expression: ")
# expression will be in form like 1 + 1

#split will assign 1st value to x 2nd to y and 3rd to z
x, y, z = exprsn.split(" ")

x= float(x)
z= float(z)

if y == "+":
    p= round(x + z,1)
    print(p)
elif y== "-":
    p = round(x - z,1)
    print(p)
elif y == "*":
    p = round(x * z,1)
    print(p)

else :
    p = round(x / z,1)
    print(p)
