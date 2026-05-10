# converting camel case in snake case
# camel_case: 1 no space btw the words
#             2 excep first letter of first words
#                all other's first letter in capital
# snake_case: 1 all letter in lower case
#             2 separated by _
# eg: first_name ,prefferd_first_name

# taking input in camel case and splitting all letters
camel_case = input("camelcase: ").strip()

print("snake_case: ",end="" )
# loop in the str until found a capital letter
for letter in camel_case:
    if letter.isupper():
        # split the word and add an_ and make it lower case
        print("_"+letter.lower(),end="")

    else  :print(letter,end="")
