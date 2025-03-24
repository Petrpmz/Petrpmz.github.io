# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 11:49:29 2013

@author: Radek
"""

# from tkinter import *

# hlavni=Tk()
# hlavni.geometry("250x100")
# hodnota=StringVar()
# hodnota.set(0)

# def Nastav():
#     l["text"]=hodnota.get()
    
# w = Spinbox(hlavni, from_=-50, to=1000, increment=2,textvariable=hodnota,command=Nastav)
# w.pack()

# l=Label(text="0",font="Arial 20")
# l.pack()

# hlavni.mainloop()
gfhfgh
"""
Úkol:
1) Pomocí Spinboxu zkuste měnit velikost písma u Labelu.
"""
from tkinter import *

hlavni=Tk()
hlavni.geometry("250x100")
hodnota=StringVar()
hodnota.set(0)

def Nastav():
    l["font"]= ("Arial",hodnota.get())
    
w = Spinbox(hlavni, from_=5, to=45, increment=5,textvariable=hodnota,command=Nastav)
w.pack()

l=Label(text="Label",font="Arial 5")
l.pack()

hlavni.mainloop()
"""
Navíc:
Vytvořte dokumentaci (výpis programu s komentářem, vývojový diagram, závěr).    
"""


