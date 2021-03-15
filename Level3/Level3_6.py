import sys

n = int(sys.stdin.readline())

while n < 0 and n > 100000:
    n = int(sys.stdin.readline())

for i in range(n,0,-1):
    print(i)
