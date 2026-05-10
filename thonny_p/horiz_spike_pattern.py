#spike horizontal pattern maker
import time,sys
space = 0
try:
    while True:
        for i in range(1,20):
            print("-"*i)
            time.sleep(0.1)
        for i in range(19,1,-1):
            print("-"*i)
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
