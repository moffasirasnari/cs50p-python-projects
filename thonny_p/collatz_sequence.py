#collatz sequence
#take input an int
#define collatz
#if int = even return //2
#if int = odd return 3*int +1
#keep calling colltz until get 1 (will eventually get 1 with any int)
import sys
def main():
    try:
        num = int(input("Enter a number: "))
        while True:
            print(collatz(num),'',end="")
            num = collatz(num)
            if collatz(num) == 1:
                print(collatz(num))
                break 
    except  (ValueError,KeyboardInterrupt):
        sys.exit()

def collatz(number):
    if number % 2 ==0:
        return number//2
    else :
        return 3*number +1
main()    
    
