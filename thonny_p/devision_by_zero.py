#divide by zero
#exception handling
#saves programme from just crashing ->ends properly (huge impact in apps,web)
def spam(divide_by):
    try :
        return 42 / divide_by
    except ZeroDivisionError: #will run when this error accursd
        print("invalid input")
        
    
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))