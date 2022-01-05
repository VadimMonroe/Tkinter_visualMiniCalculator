from tkinter import *
from tkmacosx import Button


root = Tk()

class Block:
    def __init__(self, master):
        self.ent = Entry(master, width=20, bg='red', border=1)
        self.ent2 = Entry(master, width=20, bg='blue', border=1)
        self.ent3 = Entry(master, width=20, bg='cyan', border=1, text='Введите')
        self.ent4 = Entry(master, width=20, bg='cyan', border=1, text='Введите')
        self.lab = Label(master, width=20, height=3, bg='white', fg='black', border=0)

        self.but = Button(master, width=150, height=50, bg='yellow', text="+")
        self.but['command'] = self.plus
        self.but2 = Button(master, width=150, height=50, bg='yellow', text="-")
        self.but2['command'] = self.minus
        self.but3 = Button(master, width=150, height=50, bg='yellow', text="*")
        self.but3['command'] = self.multiplication
        self.but4 = Button(master, width=150, height=50, bg='yellow', text="/")
        self.but4['command'] = self.divide
        self.but5 = Button(master, width=150, height=50, bg='yellow', text="Сделать 16-ричным")
        self.but5['command'] = self.ten_six
        self.but6 = Button(master, width=150, height=50, bg='yellow', text="Из 16-ричного")
        self.but6['command'] = self.six_ten

        self.ent.pack()
        self.ent2.pack()


        self.lab.pack()

        self.but.pack()
        self.but2.pack()
        self.but3.pack()
        self.but4.pack()

        self.ent3.pack()

        self.but5.pack()
        self.but6.pack()

    def plus(self):
        a = self.ent.get()
        b = self.ent2.get()
        self.lab['text'] = int(a) + int(b)

    def minus(self):
        a = self.ent.get()
        b = self.ent2.get()
        self.lab['text'] = int(a) - int(b)

    def multiplication(self):
        a = self.ent.get()
        b = self.ent2.get()
        self.lab['text'] = int(a) * int(b)

    def divide(self):
        a = self.ent.get()
        b = self.ent2.get()
        self.lab['text'] = int(a) / int(b)

    def ten_six(self):
        a = self.ent3.get()
        result = ''
        first = int(a)
        while first != 0:
            second = first - first // 16 * 16
            if second == 10:
                second = 'A'
            elif second == 11:
                second = 'B'
            elif second == 12:
                second = 'C'
            elif second == 13:
                second = 'D'
            elif second == 14:
                second = 'E'
            elif second == 15:
                second = 'F'

            result = str(result) + str(second)
            first = first // 16
        result = result[::-1]
        self.lab['text'] = result

    def six_ten(self):
        a = self.ent3.get()
        x = len(a) - 1
        result = 0
        for i in a:
            if i == 'A':
                i = 10
            elif i == 'B':
                i = 11
            elif i == 'C':
                i = 12
            elif i == 'D':
                i = 13
            elif i == 'E':
                i = 14
            elif i == 'F':
                i = 15

            if x == 0:
                result = result + int(i)
            else:
                result = result + (int(i) * (16 ** x))
            x -= 1
        self.lab['text'] = result

first_block = Block(root)

root.mainloop()
