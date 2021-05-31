# x 값이 몇 이하인지는 안 주어지고, 그냥 자연수라는 것만 주어졌을 경우
x = int(input())
count = 0

def hansu(num):
    global count
    s = str(num)
    numlist = []

    if num < 100:
        count += 1
    else:
        c = 0
        for i in range(len(s)):
            a = int(s[i])
            numlist.append(a)
        if num < 1000 and numlist[2] - numlist[1] == numlist[1] - numlist[0]:
            count += 1
        else:
            for i in range(len(s)-2):
                if numlist[i+1] - numlist[i] == numlist[i+2] - numlist[i+1]:
                    c += 1
            if c == len(s)-2:
                count += 1

for numbers in range(1, x+1):
    hansu(numbers)

print(count)

"""
x가 1000이하인 경우

x = int(input())
count = 0

for num in range(1, x+1):
    if num < 100:
        count += 1
    elif num < 1000:
        if (num // 100) - ((num % 100) // 10) == ((num % 100) // 10) - ((num % 100) % 10):
            count += 1
    else:
        count += 0

print(count)"""

"""
다른 분의 좋은 풀이

hansu = 0
N = int(input())
for i in range(N+1):
    cut = list(map(int,str(i)))
    if i < 100:
        hansu = i
    elif cut[0]-cut[1]==cut[1]-cut[2]:
        hansu+=1
print(hansu)"""