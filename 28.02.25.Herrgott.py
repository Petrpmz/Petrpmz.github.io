#A

from tkinter import *
import random
from tkinter import messagebox

hlavni = Tk()
hlavni.geometry("600x450")
x=0
y=0

def Nahoda():
    global x,y
    x=random.randint(0,520)
    y=random.randint(0,370)
    frame.place(anchor="nw", x=x, y=y)

def info():
    messagebox.showinfo("O programu","Petr Herrgott")

def F1(udalost):
    messagebox.showinfo("O programu","Petr Herrgott")

def Reset(udalost):
    frame.place(x=0,y=0)

menu = Menu(hlavni)
hlavni.config(menu=menu)


hlavni_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=hlavni_menu)
hlavni_menu.add_command(label="Náhoda", command=Nahoda)
hlavni_menu.add_command(label="O programu", command=info)
hlavni_menu.add_command(label="Konec", command=hlavni.destroy)


frame=Frame(hlavni, width=80, height=80,bg="Blue",)
frame.place(anchor="nw", x=x, y=y)


hlavni.bind("<F1>", F1)
frame.bind("<Button-1>", Reset)

mainloop()