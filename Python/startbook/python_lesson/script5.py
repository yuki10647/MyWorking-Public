#5-A
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:break
    for i in range (a):
        print('#'*b)
    print()
#5-B
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:break
    f=[[0 for i in range(b)]for j in range(a)]
    for i in range(a):
        for j in range(b):
            if i==0 or i==a-1 or j==0 or j==b-1:
                f[i][j]=1
    for i in range(a):
        for j in range(b):
            if f[i][j]==1:
                print('#',end='')
            else :
                print('.',end='')
        print()
    print()
#5-C
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    f = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            a = i + j
            if a % 2 == 0:
                f[i][j] = 1
    for i in range(H):
        for j in range(W):
            if f[i][j] == 1:
                print("#", end = "")
            else:
                print(".", end = "")
        print()
    print()
#5-D
x = int(input())
print(" ", end = " ")
for i in range(1, x+1):
    if i % 3 == 0:
        print(i, end = " ")
    elif "3" in str(i):
        print(i, end = " ")