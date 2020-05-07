from tkinter import *

import math

root = Tk()

root.title("Cross Product Calculator")

v = Label(root, text="Vector 1").grid(row=0, column=0) #the labels are labels for the entries I defined in the for loops below

a = Label(root, text="i").grid(row=1, column=1) 

b = Label(root, text="j").grid(row=1, column=3)

c = Label(root, text = "k").grid(row=1, column=5)


for i in range(1, 4): #both for loops created the entries where you can put in values
    column_var = i * 2
    exec ("u%s=Entry(root)" % i) 
    exec ("u%s.grid(row=1, column=column_var)" % i)
    exec ('u%s.insert(0,"0")' % i)

for i in range(1, 4):
    column_var = i * 2
    exec ("v%s=Entry(root)" % i)
    exec ("v%s.grid(row=4, column=column_var)" % i)
    exec ('v%s.insert(0,"0")' % i)

v_prime = Label(root, text="Vector 2").grid(row=3, column=0)

d = Label(root, text="i").grid(row=4, column=1)

e = Label(root, text = "j").grid(row=4, column=3)

f = Label(root, text = "k").grid(row=4, column=5)

list = [u1, u2, u3, v1, v2, v3]

def calculate():
    for i in list:  #following lines (until final_vector is defined) convert square root symbols to sqrt() for the computer to handle
        for y in i.get():
            if y == "√":
                x = i.get()
                before_root = ""
                for z in i.get():
                    if z == "√":
                        x = x.replace("√","")
                        break
                    else:
                        before_root = before_root + z
                        x = x.replace(z,"",1)
                z = float(math.sqrt(float(x)))
                print(before_root)
                z = z * float(before_root)
                i.delete(0,"end")
                i.insert(0,z)
    final_vector = Vector(float(u2.get())*float(v3.get()) - float(u3.get())*float(v2.get()), float(u3.get())*float(v1.get()) - float(u1.get())*float(v3.get()), float(u1.get())*float(v2.get()) - float(u2.get())*float(v1.get())) #creates the vector
    
    final_vector.i = final_vector.convert_int(final_vector.i) #convert the values to an int if there's nothing after the decimal place of the float
    final_vector.j = final_vector.convert_int(final_vector.j)
    final_vector.k = final_vector.convert_int(final_vector.k)

    final_vector.doPrint() #print the final vector in a new tkinter window

button = Button(root, text="Calculate", command = calculate).grid(row=6, column=0) #button that triggers the calculate process


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        if self.j >= 0:
            self.j_sign = " + " #finds out what sign to put in front of each element of the vector in i, j, k form
        else:
            self.j_sign = " - "
        if self.k >= 0:
            self.k_sign = " + "
        else:
            self.k_sign = " - "
        self.j = abs(self.j)
        self.k = abs(self.k)
    def convert_int(self, element):
        if element - int(element) == 0.0:
            return int(element)
        else:
            return element
    def doPrint(self):
        answer = Tk()
        answer.title("Answer")
        answer_label = Label(answer, text=str(self.i) + "i" + self.j_sign + str(self.j) + "j" + self.k_sign + str(self.k) + "k").grid(row=0, column=0) #i, j, k notation
        alternate_label = Label(answer, text="<" + str(self.i) + ", " + str(self.j) + ", " + str(self.k) + ">").grid(row=1, column=0) #Position vector notation
root.mainloop()
