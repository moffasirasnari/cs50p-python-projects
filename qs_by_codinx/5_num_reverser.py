#reversing a four digit number
num= input("Enter a four digit number: ")

def main():
    reverse_num=[]
    for i in range(len(num)):
        n=len(num)-1-i
        reverse_num.append(num[n])
    reverse_num=''.join(reverse_num)
    if check(reverse_num) == True:
        print(reverse_num)

def check(x):
    for i in range(len(num)):
        if num[i] == x[len(x)-1-i]:
            continue
        else : return False
    return True
main()

