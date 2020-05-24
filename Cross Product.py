from tkinter import *
import math

root = Tk()
root.title("Cross Product Calculator") #Title of window
Label(root, text="Vector 1").grid(row=0, column=0)
Label(root, text="Vector 2").grid(row=3, column=0)

def doPrint(i_value, j_value, sign_j, k_value, sign_k): #Puts the answer in a new window
    answer = Tk()
    answer.title("Answer")

    answer_label = Label(answer, text=str(i_value) + "i" + sign_j + str(abs(j_value)) + "j" + sign_k + str(abs(k_value)) + "k").grid(row=0, column=0) #i, j, k notation

    alternate_label = Label(answer, text="<" + str(i_value) + ", " + str(j_value) + ", " + str(k_value) + ">").grid(row=1, column=0) #Position vector notation

def make_entry(): #Creats entries and the labels that go along with them
    components = {1:"i", 3:"j", 5:"k"}
    for index in components: #Creates the i, j, k labels
        Label(root, text=components[index]).grid(row = 1, column = index) 
        Label(root, text=components[index]).grid(row = 4, column = index)
    for a in range(1, 7): #creates entries on multiple rows
        if a > 3:
            num = a - 3
            column_var = (num) * 2
            exec ("v%s=Entry(root)" % num, globals())
            exec ("v%s.grid(row=4, column=column_var)" % num)
            exec ('v%s.insert(0,"0")' % num)
        else:
            column_var = a * 2
            exec ("u%s=Entry(root)" % a, globals()) 
            exec ("u%s.grid(row=1, column=column_var)" % a)
            exec ('u%s.insert(0,"0")' % a)

def square_root(list): #Computes expressions with square roots 
    for entry in list: #Iterates through the list containing the entries
        for text in entry.get(): #Iterates through all of the characters in the values in each entry
            if text == "√":
                entry_value = entry.get() #get method gets value from entry
                before_root = ""
                for z in entry.get():
                    if z == "√":
                        entry_value = entry_value.replace("√","")
                        break
                    else:
                        before_root = before_root + z
                        entry_value = entry_value.replace(z,"",1)
                entry_number = float(math.sqrt(float(entry_value))) #Square root of the radicand
                if before_root != '':
                    entry_number = entry_number * float(before_root) #Multiply number to the square root of radicand
                entry.delete(0,"end") #deletes whatever is in the entry
                entry.insert(0,entry_number) #puts the value that was calculated by the function within the entry
    

def calculate():
    for entry in [u1, u2, u3, v1, v2, v3]:
        if entry.get() == '': #If the entry is empty, put insert the value of 0 so the program doesn't crash
            entry.insert(0, "0")

    square_root([u1, u2, u3, v1, v2, v3])
    final_vector = Vector(u1, u2, u3, v1, v2, v3) #creates the vector

make_entry()

Button(root, text="Calculate", height=1, width=6, command = calculate).grid(row=6, column=0)#button that triggers the calculate process

Button(root, text="Clear", height=1, width=6, command = make_entry).grid(row=7, column=0) #button that remakes the entries (thus resetting them)

    
def Vector(u1, u2, u3, v1, v2, v3):
    i = float(u2.get()) * float(v3.get()) - float(u3.get()) * float(v2.get()) #Using cross product formula (determinants of 3x3 matrix of vectors)
    j = float(u3.get()) * float(v1.get()) - float(u1.get()) * float(v3.get())
    k = float(u1.get()) * float(v2.get()) - float(u2.get()) * float(v1.get())
    if j >= 0: #Sign that goes before the j component of the cross product
        j_sign = " + "
    else:
        j_sign = " - "
    if k >= 0: #Sign that goes before the k component of the cross product
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
