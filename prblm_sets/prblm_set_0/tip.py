# tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#the input of user is expected to be start with $ sign
def dollars_to_float(d):
     value=d.replace("$","")
     value=float(value)
     return value

#the input of user is expected to be start with % sign
def percent_to_float(p):
    value=p.replace("%","")
    value=float(value)
    value =value / 100
    return value



main()
