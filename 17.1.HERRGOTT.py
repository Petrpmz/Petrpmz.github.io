from tkinter import *

hlavni = Tk()
hlavni.geometry("600x480")

v = StringVar()
v.set("Label")  

def paste():
    v.set(lab3.get())  

lab2 = Label(hlavni, text="Zadej text:", font=("Arial", 15))
lab2.grid(row=11, column=0)

lab3 = Entry(hlavni, textvariable=v, font=("Arial", 10))
lab3.grid(row=11, column=1)

lab4 = Button(hlavni, text="Vlož text", font=("Arial", 15), command=paste)
lab4.grid(row=11, column=2)

for i in range(4):
    for y in range(10):
        lab = Label(hlavni, textvariable=v, font=("Arial", 15))
        lab.grid(row=y, column=i)

mainloop()




