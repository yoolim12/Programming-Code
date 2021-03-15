a, b, c = map(int, input("A,B,C를 입력하세요(2<=A,B,C<=10000): ").split())

#d = map(int, input("A,B,C를 입력하세요(2<=A,B,C<=10000): ").split())
#f = list(d)

#for e in d:
 #   print(e)

#for e in f:
 #   if e < 2 or e >10000:
  #      while e < 2 or e > 10000:
   #         d = map(int, input("A,B,C를 입력하세요(2<=A,B,C<=10000): ").split())
    #        f = list(d)
     #       if e >= 2 and e <= 10000:
      #          break

while (a < 2 or a > 10000) or (b < 2 or b > 10000) or (c < 2 or c > 10000):
    a, b, c = map(int, input("A,B,C를 입력하세요(2<=A,B,C<=10000): ").split())

#while a,b,c < 2 or a,b,c > 10000 :
 #   a,b,c = map(int, input("A,B,C를 입력하세요(2<=A,B,C<=10000): ").split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
