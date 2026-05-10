def main():
    x = get_int("whats x? ")
    print(f"x is {x}")

def get_int(s):
    while True:
        try:
            return int(input(s))

        except ValueError:
            pass


main()
