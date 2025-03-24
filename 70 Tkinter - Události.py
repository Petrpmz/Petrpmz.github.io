# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 10:00:12 2013

@author: Radek
"""
""" 
from tkinter import *

hlavni = Tk()

def LevyKlik(udalost):
    print ("Klikl jsi na frame na pozici:", udalost.x, udalost.y)

def Najeti(udalost):
    print ("Najel jsi na frame")
#    print udalost

def Klavesa(udalost):
    print ("Stiskl jsi ", udalost.char)
#    print (udalost)

def Pohyb(udalost):
    print (udalost.x, udalost.y)

def F1(udalost):
    print ("Stiskl jsi F1")
    
vstup = Entry(hlavni)
vstup.bind("<Key>", Klavesa)
vstup.bind("<F1>",F1)
vstup.pack()
  
ramec = Frame(hlavni, width=100, height=100,bg="red")
ramec.bind("<Button-1>", LevyKlik)
ramec.bind("<Enter>", Najeti)
ramec.bind("<B1-Motion>",Pohyb)
ramec.pack()

hlavni.mainloop() """

"""
1) Vložte do hl. okna frame, který bude reagovat na
   pravé tlačítko myši a vždy si nastaví náhodnou
   barvu pozadí.
2) Při stisku levého tlačítka se nastaví bílé pozadí.
3) Vytvořte program s jedním tlačítkem, které se po
   najetí myši přesune na náhodné místo v okně (musíme
   použít funkci place()).
"""   
# from tkinter import *
# import random
# hlavni = Tk()

# def nahodna_barva():
#     return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# def Pravy(udalost):
#     nova_barva = nahodna_barva()
#     ramec.config(bg=nova_barva)
#     print("nastavena barva:",nova_barva)
# def Levy(udalost):
#     nova_barva = "white"
#     ramec.config(bg=nova_barva)
#     print("nastavena barva:",nova_barva)

# ramec = Frame(hlavni, width=100, height=100,bg="white")
# ramec.bind("<Button-3>", Pravy)
# ramec.bind("<Button-1>", Levy)
# ramec.pack()

# hlavni.mainloop()



# from tkinter import *
# hlavni = Tk()
# hlavni.geometry("1800x700")


# def Najeti(udalost):
#     ramec.place(anchor="nw",x=random.randint(100,1700),y=random.randint(50,650),width=200,height=10)
#     print ("Najel jsi na Tlačítko")
#     print(udalost)


# ramec = Button(hlavni,bg="green",text="Tlačítko")
# ramec.bind("<Enter>", Najeti)
# ramec.place(x=900, y=350,width=200, height=10)


# hlavni.mainloop()


from tkinter import *
hlavni = Tk()
hlavni.geometry("1800x700")

def Pohyb(udalost):
    ramec.place(anchor="nw",x=(udalost.x),y=(udalost.y),width=200,height=10)

ramec = Button(hlavni,bg="green",text="Tlačítko")
ramec.place(x=900, y=350,width=200, height=10)

hlavni.bind("<B1-Motion>",Pohyb)

hlavni.mainloop()






