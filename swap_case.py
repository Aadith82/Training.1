Is=input("enter a string :")
Os=''
for i in Is:
    if i.isupper():
        o=i.lower()
    elif i.islower():
        o=i.upper()
    else:
        o=i
    Os+=o
    
print(Os)
