#install emjoi module package
#get input inform of ":name of emoji:"
#convert that name into corrosponding emoji
import emoji

def main():
    name = take_input("Input: ")

    emoji_ = emoji.emojize(name,language= "alias")
    print(emoji_)


def take_input(s):
    name = input(s).strip()
    return name


main()
