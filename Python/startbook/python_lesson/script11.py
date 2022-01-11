#11-A
class dice:
    def __init__(self, label):
        self.a, self.b, self.c, self.d, self.e, self.f = label
    def play(self, op):
        if op == "N":
            self.a, self.b, self.e, self.f = self.b, self.f, self.a, self.e
        elif op == "S":
            self.a, self.b, self.e, self.f = self.e, self.a, self.f, self.b
        elif op == "E":
            self.a, self.c, self.d, self.f = self.d, self.a, self.f, self.c
        elif op == "W":
            self.a, self.c, self.d, self.f = self.c, self.f, self.a, self.d
    def pri(self):
        print(self.a)
label = list(map(int, input().split()))
oplist = list(input())
d = dice(label)
for op in oplist:
    d.play(op)
d.pri()
#11-B(コピーしただけ)
class Dice:
    def __init__(self):
        self.u=1
        self.w=2
        self.s=3
        self.e=4
        self.n=5
        self.d=6
        self.dic={"W":0,"S":1,"E":2,"N":3}
    def __init__(self,u,w,s,e,n,d):
        self.u=u
        self.w=w
        self.s=s
        self.e=e
        self.n=n
        self.d=d
        self.dic={"W":0,"S":1,"E":2,"N":3}
    def rot(self,way):
        if isinstance(way,str):
            way=self.dic[way]
        if(way==0):
            c=self.u
            self.u=self.e
            self.e=self.d
            self.d=self.w
            self.w=c
        elif way==1:
            c=self.u
            self.u=self.n
            self.n=self.d
            self.d=self.s
            self.s=c
        elif way==2:
            c=self.u
            self.u=self.w
            self.w=self.d
            self.d=self.e
            self.e=c
        else :
            c=self.u
            self.u=self.s
            self.s=self.d
            self.d=self.n
            self.n=c
import random
u,s,e,w,n,d=map(int,input().split())
dice=Dice(u,w,s,e,n,d)
q=int(input())
for i in range(q):
    a,b=map(int,input().split())
    while True:
        dice.rot(random.randint(0,3))
        if(dice.u==a and dice.s==b):
            print(dice.e)
            break
#11-C
class dice:
    def __init__(self, label):
        self.a, self.b, self.c, self.d, self.e, self.f = label
    def play(self, op):
        if op == "N":
            self.a, self.b, self.e, self.f = self.b, self.f, self.a, self.e
        elif op == "S":
            self.a, self.b, self.e, self.f = self.e, self.a, self.f, self.b
        elif op == "E":
            self.a, self.c, self.d, self.f = self.d, self.a, self.f, self.c
        elif op == "W":
            self.a, self.c, self.d, self.f = self.c, self.f, self.a, self.d
    def li(self):
        return [self.a, self.b, self.c, self.d, self.e, self.f]
label = list(map(int, input().split()))
dice_base = dice(label)
label2 = list(map(int, input().split()))
for op in 'EEESEEESEEENEEENEEESEEEN':
    if dice_base.li() == label2:
        print("Yes")
        break
    dice_base.play(op)
else:
    print("No")

#11-D
class dice:
    def __init__(self, label):
        self.a, self.b, self.c, self.d, self.e, self.f = label
    def play(self, op):
        if op == "N":
            self.a, self.b, self.e, self.f = self.b, self.a, self.f, self.e
        elif op == "S":
            self.a, self.b, self.e, self.f = self.e, self.a, self.f, self.b
        elif op == "E":
            self.a, self.c, self.d, self.f = self.d, self.a, self.f, self.c
        elif op == "W":
            self.a, self.c, self.d, self.f = self.c, self.f, self.a, self.d
    def li(self):
        return [self.a, self.b, self.c, self.d, self.e, self.f]
    def com(self, label):
        for op in 'EEESEEESEEENEEENEEESEEE':
            if self.li() == label:
                return True
            self.play(op)
        else:
            return False
n =int(input())
L = []
for i in range(n):
    label = list(map(int, input().split()))
    d = dice(label)
    for d in L:
        if d.com(label):
            break
    else:
        L.append(dice(label))
        continue
    print("No")
    break
else:
    print("Yes")