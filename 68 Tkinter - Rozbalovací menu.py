# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 10:35:54 2013

@author: Radek
"""

""" 
from tkinter import *
from tkinter import messagebox
hlavni = Tk()

#vytvoření jednotlivých menu
HorniMenu=Menu(hlavni)
MenuSoubor=Menu(HorniMenu,tearoff=0)
VnoreneMenu = Menu(MenuSoubor,tearoff=0)

def Soubor():
    messagebox.showinfo("Soubor","Tato část není naprogramována!")

#vytvoření jedné rozbalovací nabídky a připojení do hl. menu 
MenuSoubor.add_command(label="Otevřít",command=Soubor)
MenuSoubor.add_command(label="Uložit",command=Soubor)
MenuSoubor.add_cascade(label="Další menu", menu = VnoreneMenu)
MenuSoubor.add_separator()
MenuSoubor.add_command(label="Konec",command=hlavni.destroy)


VnoreneMenu.add_command(label="Položka1",command=Soubor)
VnoreneMenu.add_command(label="Položka2",command=Soubor)
VnoreneMenu.add_command(label="Položka3",command=Soubor)

HorniMenu.add_cascade(label="Soubor", menu=MenuSoubor)

#zobrazení hlavního menu
hlavni.config(menu=HorniMenu)

mainloop()
 """
"""
Úkol:
1) Vytvořte program ukázky jazyků s rozbalovacím menu
   o dvou položkách:

   Soubor
    - Anglicky
    - Německy
    - Španělsky
    - Konec
    
   Nápověda
    - O aplikaci
    - O autorovi
   
"""    
from tkinter import *
from tkinter import messagebox
hlavni = Tk()

HorniMenu=Menu(hlavni)
MenuSoubor=Menu(HorniMenu,tearoff=0)
Nápoveda=Menu(HorniMenu,tearoff=0)

def Soubor():
    messagebox.showinfo("Soubor","Tato část není naprogramována!")

MenuSoubor.add_command(label="Anglicky")
MenuSoubor.add_command(label="Německy")
MenuSoubor.add_cascade(label="Španělsky")
MenuSoubor.add_command(label="Konec", command=hlavni.destroy)

Nápoveda.add_command(label="O aplikaci")
Nápoveda.add_command(label="O autorovi")

HorniMenu.add_cascade(label="Soubor", menu=MenuSoubor)
HorniMenu.add_cascade(label="Nápověda", menu=Nápoveda)

hlavni.config(menu=HorniMenu)

mainloop()
