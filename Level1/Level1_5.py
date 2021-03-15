a,b=map(int, input("A,B를 입력하시오(0<A,B<10): ").split())

while a<=0 or a>=10 or b<=0 or b>=10:
    if (a<=0 or a>=10) and (b<=0 or b>=10):
        a,b=map(int, input("A,B를 입력하시오(0<A,B<10): ").split())

    elif a<=0 or a>=10:
        a=int(input("A를 입력하세요(0<A<10): "))

    elif b<=0 or b>=10:
        b=int(input("B를 입력하세요(0<B<10): "))

c=a+b

print(c)
