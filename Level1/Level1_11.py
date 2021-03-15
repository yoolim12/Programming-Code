a=int(input())
b=int(input())

one = b%10
ten = int(((b%100)-(b%10))/10)
hun = int(b/100)

c=a*one
d=a*ten
e=a*hun

print(c)
print(d)
print(e)
print(a*b)
