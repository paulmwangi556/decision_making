print("enter marks")
a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
average=int(a+b+c+d+e)/5
if (average>=70 and average<=100):
    print("A")
elif (average>=60 and average<=69):
    print("B")
elif (average>=50 and average<=59):
    print("C")
elif (average>=40 and average<=49):
    print("D")
else:
    print("fail")