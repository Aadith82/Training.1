import math as m
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
if((s-a)*(s-b)*(s-c)>0):
    area=(s*(s-a)*(s-b)*(s-c))
    ans=m.sqrt(area)
    print("The area of the triangle is: {:.2f}".format(ans))
else:
    print("Invalid Triangle")