a=input()
v="AEIOUaeiou"
count=0
for i in a:
    if(i in v):
        count=count+1
if(count>0):
    print("Total number of vowels:",count)
else:
    print("No vowels were found.")
