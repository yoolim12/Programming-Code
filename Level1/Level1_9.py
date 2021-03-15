a,b=map(int, input().split())

while (a<1 or a>10000) or (b<1 or b>10000):
    a,b=map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)