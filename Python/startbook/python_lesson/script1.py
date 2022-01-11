#AOJ.Lesson-ITP1
#https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all


#1-A
print('Hello World')
#1-B
va1 = input()
x = int(va1)
print(x**3)
#1-C
val = input()
a, b = [int(i) for i in val.split()]
print(a * b, a * 2 + b * 2)
#1-D
val = input()
a = int(val)
b = a // 3600
c = a - b * 3600
d = c // 60
e = c % 60
print(str(b) + ':' + str(d) + ':' + str(e))