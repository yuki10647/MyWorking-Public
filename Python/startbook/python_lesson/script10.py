#10-A
import math
x1, y1, x2, y2 = map(float, input().split())
dis2 = (x2 - x1)**2 + (y2 - y1)**2
print(math.sqrt(dis2))
#10-B
import math
a, b, C = map(int, input().split())
S = a * b * math.sin(C*math.pi/180) / 2
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C*math.pi/180))
L = a + b + c
h = 2 * S / a
print(S)
print(L)
print(h)
#10-C
import math
while True:
    n = int(input())
    if n == 0:
        break
    stu = list(map(int, input().split()))
    #ここがrange(n)になる。
    sum = 0
    for s in stu:
        sum += s
    ave = sum / n
    a=0
    for s in stu:
        dif = s - ave
        a += dif**2
    var = a / n
    dev = math.sqrt(var)
    print(f'{dev:.5f}')
#10-D
import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
#もしくはrange(n)
d1 = 0.0
d2 = 0.0
d3 = 0.0
d_inf = 0.0
for i in range(n):
    dif = abs(x[i]-y[i])
    d1 += dif
    d2 += math.pow(dif, 2)
    d3 += math.pow(dif, 3)
    d_inf = max(d_inf, dif)
d2 = math.pow(d2, 1/2.0)
d3 = math.pow(d3, 1/3.0)
print(f'{d1:.6f}')
print(f'{d2:.6f}')
print(f'{d3:.6f}')
print(f'{d_inf:.6f}')
#ミンコフスキー距離
#マンハッタン距離
#ユークリッド距離
#チェビシェフ距離