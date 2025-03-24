# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:01:49 2013

@author: Radek
"""
"""
https://www.geeksforgeeks.org/hide-and-unhide-the-window-in-tkinter-python/

Množství otevřených oken je možno regulovat pomocí zašednutí 
tlačítka.
"""
from tkinter import *

hlavni=Tk()
hlavni.minsize(300,150)
hlavni.title("Hlavní okno")

def ZavriOkno():
    global okno
    okno.destroy()
    tlac["state"]="normal"
    
def ZobrazOkno():
    global okno
    okno=Toplevel()
    okno.minsize(300,100)
    okno.title("Vedlejší okno")
    tlac["state"]="disabled"
    okno.protocol("WM_DELETE_WINDOW",ZavriOkno)


    tlZavriOkno=Button(okno,text="Zavři toto okno",command=ZavriOkno)
    tlZavriOkno.pack()   
    tlZavriAplikaci=Button(okno,text="Zavři celou aplikaci",command=hlavni.destroy)
    tlZavriAplikaci.pack() 

    
tlac = Button(hlavni, text="Zobraz podokno",command=ZobrazOkno)
tlac.pack()

mainloop()

"""
Úkoly:
1) Umožněte uživateli otevřít z hlavního okna 2 podokna. Jedno bude 
   zelené a druhé červené. Zajistěte, aby nešlo otevřít více než 1
   vedlejší okno od každého druhu.
"""


from tkinter import *

hlavni=Tk()
hlavni.minsize(300,150)
hlavni.title("Hlavní okno")

def Okno1():
    global okno
    okno=Toplevel(bg="red")
    okno.minsize(300,100)
    okno.title("ČERVENÉ okno")
    tlac["state"]="disabled"
    tlac2["state"]="normal"

    
def Okno2():
    global okno
    okno=Toplevel(bg="green")
    okno.minsize(300,100)
    okno.title("ZELENÉ okno")
    tlac2["state"]="disabled"
    tlac["state"]="normal"


    
tlac = Button(hlavni, text="ČERVENÉ",command=Okno1)
tlac.pack()
tlac2 = Button(hlavni, text="ZELENÉ",command=Okno2)
tlac2.pack()

mainloop()







