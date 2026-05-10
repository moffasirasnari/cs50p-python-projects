#oldest age finder
age=input("Enter three ages").split()
int_age=[]
for i in range(3):
    n = int(age[i])
    int_age.append(n)
int_age.sort()
print(int_age[-1])



