n = int(input())
total = 0

while n < 1 or n > 10000:
    n = int(input())

for i in range(1,n+1):
    total += i

print(total)
