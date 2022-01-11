#9-A
W = input().lower()
ans = 0
while True:
    T = input()
    if T == "END_OF_TEXT":
        break
    ans += T.lower().split().count(W)
print(ans)
#9-B
for i in range(10000):  
    word = input()
    if word == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        front = word[0:h]
        back = word[h:]
        word = back + front
    print(word)
#9-C
n = int(input())
T_point = 0
H_point = 0
for i in range(n):
    T_card, H_card = input().split()
    if T_card < H_card:
        H_point += 3
    elif T_card > H_card:
        T_point += 3
    elif T_card == H_card:
        T_point += 1
        H_point += 1
print(T_point, H_point)
#9-D
word = input()
q = int(input())
for i in range(q):
    com = list(input().split())
    ord = com[0]
    if ord == "print":
        a = int(com[1])
        b = int(com[2])
        print(word[a:b+1])
    elif ord == "reverse":
        a = int(com[1])
        b = int(com[2])
        f = word[:a]
        m = word[a:b+1]
        b = word[b+1:]
        m = m[::-1]
        word = f + m + b
    elif ord == "replace":
        a = int(com[1])
        b = int(com[2])
        c = com[3]
        f = word[:a]
        m = c
        b = word[b+1:]
        word = f + m + b