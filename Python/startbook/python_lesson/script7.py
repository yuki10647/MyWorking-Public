#7-A
def eval(m, f, r):
    if m == -1 or f == -1:
        grade = "F"
    else:
        if m + f >= 80:
            grade = "A"
        elif 65 <= m + f < 80:
            grade = "B"
        elif 50 <= m + f < 65:
            grade = "C"
        elif 30 <= m + f < 50:
            if r >= 50:
                grade = "C"
            else:
                grade = "D"
        else:
            grade = "F"
    return grade
for i in range(1000):
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    else:
        grade = eval(m, f, r)
    print(grade)
#7-B
import itertools
for i in range(10000):
    n, x = map(int,input().split())
    if n == 0 and x == 0 :
        break
    else:
        all_list = list(range(1,n + 1))
        c = itertools.combinations(all_list,3)
        c_list = list(c)
        num = 0
        for i in c_list:
            if sum(i) == x:
                num += 1
        print(num)
#7-C
r, c = map(int, input().split())
list = []
list2= []
for i in range(r):
    list1 = [int(i) for i in input().split()]
    list.append(list1)
for i in list:
    for j in i:
        print(j, end=' ')
    print(sum(i))
sum1 = 0
for i in range(c):
    sum = 0
    for k in list:
        sum += k[i]
    sum1 += sum
    print(sum, end=' ')
print(sum1)
#7-D
n, m, l= map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)] 
b = [list(map(int, input().split())) for i in range(m)]
c = [[0] * l for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
for i in range(n):
    for j in range(l):
        if j != 0:
            print(" ", end='')
        print(c[i][j], end='')
    print()