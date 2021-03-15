import sys

t = int(sys.stdin.readline())

while t < 0 or t > 1000000:
    t = int(sys.stdin.readline())

for n in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
