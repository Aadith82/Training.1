no=int(input())
n=no
rn=0
while(no!=0):
    d=no%10
    rn=rn*10+d
    no=no//10
if(n==rn):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
