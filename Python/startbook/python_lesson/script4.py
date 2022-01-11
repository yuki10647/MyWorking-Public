#4-A
def cal(a, b):
    d = a // b
    r = a % b
    f = float(a / b)
    return d, r, f
n, m = map(int,input().split())
d, r, f = cal(n, m)
print(f"{d} {r} {f:.5f}")
#4-B
import math
def circle(r):
    area = r * r * math.pi
    around = 2 * r * math.pi
    return area, around
r = float(input())
area, around = circle(r)
print(f"{area:.6f} {around:.6f}")
#4-C
def cal(a, op, b):
    a = int(a)
    b = int(b)
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    elif op == "/":
        r = a / b
        r = int(r)
    return r
for i in range(10000):
    a, op, b = input().split()
    if op == "?":
        break
    else:
        r = cal(a, op, b)
    print(r)
#4-D
def l(n):
    list = [int(i) for i in input().split()]
    return list
n = int(input())
list = l(n)
a = min(list)
b = max(list)
c = sum(list)
print(a, b, c)