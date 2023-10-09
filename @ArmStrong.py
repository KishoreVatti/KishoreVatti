'''s=str(371)
w=0
for i in s:
    e=int(i)
    w=w+(e**3)
s=int(s)

if w==s:
    print("Yes")
else:
    print("NO")'''
'''def ArmStrong(Number):
    s=str(Number)
    re=0
    for i in s:
        w=int(i)
        re=re+(w**3)
   
    if Number==re:
        print("S")
    else:
        print("NO")
        
Number=int(input())
ArmStrong(Number)'''
s=371
temp=s
w=0
while temp>0:
    di=temp%10
    w+=di**3
    temp=temp//10
if s==w:
    print("S")
else:
    print("NO")

