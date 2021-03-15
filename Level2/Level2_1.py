a,b = map(int, input().split())

while (a < -10000 or a > 10000) or (b < -10000 or b > 10000):
    a,b = map(int, input().split())

if a > b:
    print(">")

elif a < b:
    print("<")

else:
    print("==")
