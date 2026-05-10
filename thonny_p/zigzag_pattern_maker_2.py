#zigzag pattern - other method
import time,sys
indent = 0
indent_increasing =True #tells that inden value is inc

try: #to prevent crash on ctrl+c
    while True:
        print(" "*indent + "********")
        time.sleep(0.1)
        if indent_increasing:  #truthy/falsey method , run if true
            indent +=1
            if indent == 20:
                indent_increasing=False
        elif not indent_increasing:
            indent -= 1
            if indent == 0:
                indent_increasing= True
                continue
            
except KeyboardInterrupt:
    sys.exit()
        
