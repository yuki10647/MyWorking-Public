import tkinter as tk

current_number = 0   # 押された数字のボタンを保存
first_term = 0       # 数字を保存
second_term = 0      # 数字を保存
result = 0           # 計算結果を保存
operation = 0        # 符号判定


# １つ目の数字の保存と符号判定変数の代入
def do_plus():
    global current_number
    global first_term
    global operation
    first_term = current_number
    current_number = 0
    operation = 1

def do_minus():
    global current_number
    global first_term
    global operation
    first_term = current_number
    current_number = 0
    operation = 2

def do_multi():
    global current_number
    global first_term
    global operation
    first_term = current_number
    current_number = 0
    operation = 3

def do_divide():
    global current_number
    global first_term
    global operation
    first_term = current_number
    current_number = 0
    operation = 4

# 計算処理
def do_eq():
    global second_term
    global result
    global current_number
    global operation
    second_term = current_number
    if operation==1:
        result = first_term + second_term
    elif operation==2:
        result = first_term - second_term
    elif operation==3:
        result = first_term * second_term
    else:
        result = first_term // second_term
    current_number = 0

class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self['bg'] = "lightgreen"
        b1 = tk.Button(self, text='1', font=20, width=3, bg='pink', command= lambda:self.key(1))     # 各ボタン
        b2 = tk.Button(self, text='2', font=20, width=3, bg='magenta', command= lambda:self.key(2))
        b3 = tk.Button(self, text='3', font=20, width=3, bg='pink', command= lambda:self.key(3))
        b4 = tk.Button(self, text='4', font=20, width=3, bg='magenta', command= lambda:self.key(4))
        b5 = tk.Button(self, text='5', font=20, width=3, bg='yellow', command= lambda:self.key(5))
        b6 = tk.Button(self, text='6', font=20, width=3, bg='magenta', command= lambda:self.key(6))
        b7 = tk.Button(self, text='7', font=20, width=3, bg='pink', command= lambda:self.key(7))
        b8 = tk.Button(self, text='8', font=20, width=3, bg='magenta', command= lambda:self.key(8))
        b9 = tk.Button(self, text='9', font=20, width=3, bg='pink', command= lambda:self.key(9))
        b0 = tk.Button(self, text='0', font=20, width=3, bg='green', command= lambda:self.key(0))
        bc = tk.Button(self, text='C', font=20, width=3, bg='green', command= self.clear)
        bp = tk.Button(self, text='+', font=20, width=3, bg='green', command= self.plus)
        be = tk.Button(self, text='=', font=20, width=3, bg='green', command= self.eq)
        bmi = tk.Button(self, text='-', font=20, width=3, bg='green', command= self.minus)
        bmu = tk.Button(self, text='*', font=20, width=3, bg='green', command= self.multi)
        bd = tk.Button(self, text='//', font=20, width=3, bg='green', command= self.divide)

        b1.grid( row=4, column=0)
        b2.grid( row=4, column=1)
        b3.grid( row=4, column=2)
        b4.grid( row=3, column=0)
        b5.grid( row=3, column=1)
        b6.grid( row=3, column=2)
        b7.grid( row=2, column=0)
        b8.grid( row=2, column=1)
        b9.grid( row=2, column=2)
        b0.grid( row=5, column=0)
        bc.grid( row=1, column=0)
        be.grid( row=5, column=3)
        bp.grid( row=4, column=3)
        bmi.grid(row=3, column=3)
        bmu.grid(row=2, column=3)
        bd.grid( row=1, column=3)

        self.e = tk.Entry(self)
        self.e.grid(row=0, column=0, columnspan=4)

    # 表示関数
    def key(self, n):
        global current_number
        current_number = current_number * 10 + n
        self.show_number(current_number)

    def clear(self):
        global current_number
        current_number = 0
        self.show_number(current_number)

    def plus(self):
        do_plus()
        self.show_number(current_number)

    def minus(self):
        do_minus()
        self.show_number(current_number)

    def multi(self):
        do_multi()
        self.show_number(current_number)

    def divide(self):
        do_divide()
        self.show_number(current_number)

    def eq(self):
        do_eq()
        self.show_number(result)

    # 表示関数の元
    def show_number(self, num):
        self.e.delete(0, tk.END)
        self.e.insert(0, str(num))


# ここからメイン関数
root = tk.Tk()
f = MyFrame(root)
f.pack()
f.mainloop()
