from tkinter import *

import math

root = Tk()

root.title("Cross Product Calculator")

v = Label(root, text="Vector 1").grid(row=0, column=0)

a = Label(root, text="i").grid(row=1, column=0)

b = Label(root, text="j").grid(row=1, column=2)

c = Label(root, text = "k").grid(row=1, column=4)

u1 = Entry(root)
u1.grid(row=1,column=1)
u1.insert(0,"0")
u2 = Entry(root)
u2.grid(row=1, column=3)
u2.insert(0,"0")
u3 = Entry(root)
u3.grid(row=1, column=5)
u3.insert(0,"0")

v_prime = Label(root, text="Vector 2").grid(row=3, column=0)

d = Label(root, text="i").grid(row=4, column=0)

e = Label(root, text = "j").grid(row=4, column=2)

f = Label(root, text = "k").grid(row=4, column=4)

v1 = Entry(root)
v1.grid(row=4, column=1)
v1.insert(0,"0")
v2 = Entry(root)
v2.grid(row=4, column=3)
v2.insert(0,"0")
v3 = Entry(root)
v3.grid(row=4, column=5)
v3.insert(0,"0")

list = [u1, u2, u3, v1, v2, v3]

def calculate():
    for i in list:
        for y in i.get():
            if y == "√":
                x = i.get().replace("√", "")
                z = str(math.sqrt(float(x)))
                i.delete(0,"end")
                i.insert(0,z)
    final_vector = Vector(float(u2.get())*float(v3.get()) - float(u3.get())*float(v2.get()), float(u3.get())*float(v1.get()) - float(u1.get())*float(v3.get()), float(u1.get())*float(v2.get()) - float(u2.get())*float(v1.get()))
    answer = Tk()
    answer.title("Answer")
    answer_label = Label(answer, text=str(final_vector.i)+"i + " + str(final_vector.j) + "j + " + str(final_vector.k) + "k").grid(row=0, column=0)

button = Button(root, text="Calculate", command = calculate).grid(row=6, column=0)


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    


root.mainloop()
