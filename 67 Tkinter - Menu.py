# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:21:14 2013

@author: Radek
"""

from tkinter import *
from tkinter import messagebox
hlavni = Tk()
hlavni.minsize(width=350,height=80)

HorniMenu=Menu(hlavni)
MaleMenu=Menu(hlavni)

def Soubor():
    messagebox.showinfo("Soubor","Tato část není naprogramována!")
    
HorniMenu.add_command(label="Soubor",command=Soubor)
HorniMenu.add_command(label="Nastavení",command=Soubor)
HorniMenu.add_command(label="Nápověda",command=Soubor)
HorniMenu.add_command(label="Konec",command=hlavni.destroy)

MaleMenu.add_command(label="Soubor",command=Soubor)
MaleMenu.add_command(label="Konec",command=hlavni.destroy)

hlavni.config(menu=HorniMenu)

def ZmenMenu():
    hlavni.config(menu=MaleMenu)  

b1=Button(hlavni,text="Menu1",command=lambda:(hlavni.config(menu=HorniMenu)))
b1.pack()
b2=Button(hlavni,text="Menu2",command=ZmenMenu)
b2.pack()

# print(b1["command"])
# print(b2["command"])

mainloop()

"""
Úkol:
1) Vytvořte v aplikaci horní menu s položkami Červená, Zelená a 
   Konec. První dvě položky nastaví barvu na pozadí okna,
   poslední ukončí aplikaci.
"""
     
from tkinter import *
from tkinter import messagebox
hlavni = Tk()
hlavni.minsize(width=350,height=80)
hlavni["bg"]="white"
MaleMenu=Menu(hlavni)

def cerv():
    hlavni["bg"]="red"
def zel(): 
    hlavni["bg"]="green"


MaleMenu.add_command(label="Červená",command=cerv)
MaleMenu.add_command(label="Zelená",command=zel)
MaleMenu.add_command(label="Konec",command=hlavni.destroy)

hlavni.config(menu=MaleMenu)



mainloop()
























































import tkinter as tk
from tkinter import messagebox, Menu
import random


def nahoda():
    max_x = 520  
    max_y = 370 
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    frame.place(x=x, y=y)

def o_programu():
    messagebox.showinfo("O programu", "Autor: Jan Novák")

def na_frame(event):
    frame.place(x=0, y=0)

def klavesa_f1(event):
    o_programu()

root = tk.Tk()
root.title("Svislé menu")
root.geometry("600x450")


frame = tk.Frame(root, width=80, height=80, bg="blue")
frame.place(x=0, y=0)


frame.bind("<Button-1>", na_frame)


menu = Menu(root)
root.config(menu=menu)


hlavni_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=hlavni_menu)
hlavni_menu.add_command(label="Náhoda", command=nahoda)
hlavni_menu.add_command(label="O programu", command=o_programu)
hlavni_menu.add_command(label="Konec", command=root.quit)

root.bind("<F1>", klavesa_f1)

root.mainloop()