#input a str
#remove all vowles from it
#output str without vowels
def main():

    user_input = input("Input: ")
    output = vowel_remover(user_input)
    print("Output:",output)


def vowel_remover(word):
    vowel = ["a","e","i","o","u"]
    for letter in vowel:
        if letter in word:
            word =word.replace(letter,"")
        elif letter.capitalize() in word :
            word=word.replace(letter.capitalize(),"")
    return word
main()
