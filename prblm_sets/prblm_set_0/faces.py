# code that converts :) to smily emoji and :( to sad one

def convert(phrase):
    print(phrase.replace(":)","🙂").replace(":(","🙁"))


def main():
    user_input=input("give input ")
    convert(user_input)

main()



