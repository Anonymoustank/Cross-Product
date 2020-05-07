from tkinter import *

import math

root = Tk()

root.title("Cross Product Calculator")

v = Label(root, text="Vector 1").grid(row=0, column=0) #the labels are labels for the entries I defined in the for loops below

a = Label(root, text="i").grid(row=1, column=1) 

b = Label(root, text="j").grid(row=1, column=3)

c = Label(root, text = "k").grid(row=1, column=5)

for i in range(1, 7): #both for loops created the entries where you can put in values
    if i > 3:
        num = i - 3
        column_var = (num) * 2
        exec ("v%s=Entry(root)" % num)
        exec ("v%s.grid(row=4, column=column_var)" % num)
        exec ('v%s.insert(0,"0")' % num)
    else:
        column_var = i * 2
        exec ("u%s=Entry(root)" % i) 
        exec ("u%s.grid(row=1, column=column_var)" % i)
        exec ('u%s.insert(0,"0")' % i)




v_prime = Label(root, text="Vector 2").grid(row=3, column=0)

d = Label(root, text="i").grid(row=4, column=1)

e = Label(root, text = "j").grid(row=4, column=3)

f = Label(root, text = "k").grid(row=4, column=5)

list = [u1, u2, u3, v1, v2, v3]


def doPrint(i, j, j_sign, k, k_sign):
    answer = Tk()
    answer.title("Answer")
    answer_label = Label(answer, text=str(i) + "i" + j_sign + str(abs(j)) + "j" + k_sign + str(abs(k)) + "k").grid(row=0, column=0) #i, j, k notation
    alternate_label = Label(answer, text="<" + str(i) + ", " + str(j) + ", " + str(k) + ">").grid(row=1, column=0) #Position vector notation

def calculate():
    for i in list:  #following lines (until final_vector is defined) convert square root symbols to sqrt() for the computer to handle
        for y in i.get(): #i.get() is referring to the value contained in the entry
            if y == "√":
                entry_value = i.get()
                before_root = "" #refers to all of the values before the square root (that will eventually be multiplied to the square root)
                for z in i.get():
                    if z == "√":
                        entry_value = entry_value.replace("√","")
                        break
                    else:
                        before_root = before_root + z
                        entry_value = entry_value.replace(z,"",1)
                entry_number = float(math.sqrt(float(entry_value)))
                print(before_root)
                entry_number = entry_number * float(before_root)
                i.delete(0,"end") #deletes whatever is in the entry
                i.insert(0,entry_number) #puts the value within the entry
    final_vector = Vector(float(u2.get())*float(v3.get()) - float(u3.get())*float(v2.get()), float(u3.get())*float(v1.get()) - float(u1.get())*float(v3.get()), float(u1.get())*float(v2.get()) - float(u2.get())*float(v1.get())) #creates the vector
    
    final_vector.i = final_vector.convert_int(final_vector.i) #convert the values to an int if there's nothing after the decimal place of the float
    final_vector.j = final_vector.convert_int(final_vector.j)
    final_vector.k = final_vector.convert_int(final_vector.k)

    doPrint(final_vector.i, final_vector.j, final_vector.j_sign, final_vector.k, final_vector.k_sign) #print the final vector in a new tkinter window
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
    def convert_int(self, element):
        if element - int(element) == 0.0:
            return int(element)
        else:
            return element
    


root.mainloop()
