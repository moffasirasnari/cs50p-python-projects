# money based on greeting

greeting = input("Greeting: ").strip().lower()
#if greeting starts with hello
if greeting.startswith("hello"):
    print("$0")
#if it starts with h
elif greeting.startswith("h"):
    print("$20")
#if no greeting is given
else : print("$100")


