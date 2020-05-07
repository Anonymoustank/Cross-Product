from tkinter import *

import math

root = Tk()

root.title("Cross Product Calculator")

v = Label(root, text="Vector 1").grid(row=0, column=0) #the labels are labels for the entries I defined in the for loops below

components = {1:"i", 3:"j", 5:"k"}
for index in components:
    Label(root, text=components[index]).grid(row = 1, column = index)
    Label(root, text=components[index]).grid(row = 4, column = index)

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

list = [u1, u2, u3, v1, v2, v3]


def doPrint(i_value, j_value, sign_j, k_value, sign_k):
    answer = Tk()
    answer.title("Answer")
    answer_label = Label(answer, text=str(i_value) + "i" + sign_j + str(abs(j_value)) + "j" + sign_k + str(abs(k_value)) + "k").grid(row=0, column=0) #i, j, k notation
    alternate_label = Label(answer, text="<" + str(i_value) + ", " + str(j_value) + ", " + str(k_value) + ">").grid(row=1, column=0) #Position vector notation

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
    
    final_vector = Vector(u1, u2, u3, v1, v2, v3) #creates the vector

    
button = Button(root, text="Calculate", command = calculate).grid(row=6, column=0) #button that triggers the calculate process

    
def Vector(u1, u2, u3, v1, v2, v3):
    i = float(u2.get()) * float(v3.get()) - float(u3.get()) * float(v2.get())
    j = float(u3.get()) * float(v1.get()) - float(u1.get()) * float(v3.get())
    k = float(u1.get()) * float(v2.get()) - float(u2.get()) * float(v1.get())
    if j >= 0:
        j_sign = " + "
    else:
        j_sign = " - "
    if k >= 0:
        k_sign = " + "
    else:
        k_sign = " - "
    def convert_int(element):
        if element - int(element) == 0.0:
            return int(element)
        else:
            return element
    i = convert_int(i)
    j = convert_int(j)
    k = convert_int(k)
    doPrint(i, j, j_sign, k, k_sign)


root.mainloop()
