#swordfish
#password $ name checker
while True :
    name = input("What's your name? ").strip().lower()
    if name == "jonsina":
        print(f"Welcome", name.capitalize())
        password = input("Enter the password: ")
        if password == "fish":
            print("Access Granted :)")
            break
    continue         