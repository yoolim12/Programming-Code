#a=input()
#b=input()
#print(int(a)*int(b[2]))
#print(int(a)*int(b[1]))
#print(int(a)*int(b[0]))
#print(int(a)*int(b))

a,b=map(int, input("A,B를 입력하시오(1<=A,B<=10000): ").split())

while a<1 or a>10000 or b<1 or b>10000:
    if (a<1 or a>10000) and (b<1 or b>10000):
        a,b=map(int, input("A,B를 입력하시오(1<=A,B<=10000): ").split())

    elif a<1 or a>10000:
        a=int(input("A를 입력하세요(1<=A<=10000): "))

    elif b<1 or b>10000:
        b=int(input("B를 입력하세요(1<=B<=10000): "))

c=a+b
d=a-b
e=a*b
f=a/b
g=a%b

print(c)
print(d)
print(e)
print(f)
print(g)

