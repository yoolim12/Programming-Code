t = int(input())
a1 = []
b1 = []

for n in range(t):
    a,b = map(int, input().split())
    a1.append(a)
    b1.append(b)

for n in range(t):
    print(a1[n]+b1[n])
