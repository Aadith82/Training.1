n=int(input())
rn=0
while(n!=0):
    d=n%10
    rn=rn*10+d
    n=n//10
print(rn)
