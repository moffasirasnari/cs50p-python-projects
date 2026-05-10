#zigzag pattern maker
import sys, time

space_increasing = True
stars = ["*","*","*","*","*","*","*"]
try :
    while True :
        for i in range(5):
            stars.insert(0," ")
            print("".join(stars))
            time.sleep(0.1)
        for i in range(5):
            stars.pop(0)
            print("".join(stars))    
            time.sleep(0.1)
        continue
except KeyboardInterrupt:
    sys.exit()
    
