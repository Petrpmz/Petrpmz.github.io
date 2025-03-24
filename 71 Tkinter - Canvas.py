# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 12:04:24 2013

@author: Radek
"""
"""
Objekt Canvas - malířské plátno
- umožňuje nám vykreslovat vektorové objekty
- u objektů můžeme měnit všechny jejich vlastnosti
- objekty jsou uloženy někde uvnitř canvasu a každý má své číslo (celé)
- začínají se číslovat od 1
"""
from tkinter import *
import random

#hlavni = Tk()

# platno = Canvas(hlavni,width=300, height=300)
# platno.pack()

# # def Zmena(udalost):
# #     barvy=["red","green","blue","brown","orange","yellow","white","gray"]
# #     platno.itemconfig(obdelnik,fill=random.choice(barvy)) #změna vlastností
# #     # platno.move(obdelnik,20,20)          #posun o daný vektor
# #     platno.coords(obdelnik, 10,10,40,30) #změna souřadnic objektu
# #     # platno.delete(3)                     #smazání objektu
  
# # elipsa=platno.create_oval(0,0,100,50,fill="green",outline="orange")  
# # cara1=platno.create_line(0, 0, 200, 100,fill="yellow")
# # cara2=platno.create_line(0, 100, 200, 0, fill="red", dash=(20, 4))
# # obdelnik=platno.create_rectangle(50, 25, 150, 75, dash=(4, 4))
# # platno.delete(cara2)                     #smazání objektu


# # print(elipsa, cara1, cara2, obdelnik) #ukázka číslování objektů
# # cara2=platno.create_line(0, 100, 200, 0, fill="red", dash=(20, 4))
# # platno.move(cara2,10,10)
# # print(elipsa, cara1, cara2, obdelnik) #ukázka číslování objektů

# # platno.bind("<1>",Zmena) #při kliknutí levým tlačítkem se provede fce Zmena

# # platno.create_polygon(10,10,100,100,200,20, 100, 50)

# #létající objekt
# obj = platno.create_oval(0,150,20,170, fill="red")
# smer = 5

# def Pohyb():
#     global smer
#     platno.move(obj,smer,0)
#     sourad = platno.coords(obj)
#     if sourad[2]==300 or sourad[0]==0: 
#         smer *= -1
#     hlavni.after(20, Pohyb)

# Pohyb()

# mainloop()


"""
Úkol:
1) Nakreslete 5 úseček s náhodnými souřadnicemi.
   Pomocí cyklu!
   (Vylepšení: úsečky budou po nějakém čase měnit pozici)
2) Vykreslete barevný kruh na náhodné pozici, který se bude 
   přemísťovat svým středem tam, kam klikneme myší.
3) Pomocí událostí naprogramujte nakreslení obdélníku.
   (někam kliknu a táhnu myší)
4) Naprogramujte míček, který létá v okně a odráží se od stěn.  
  
""" 

# #1
# from tkinter import *
# import random

# hlavni = Tk()

# platno = Canvas(hlavni, width=300, height=300)
# platno.pack()

# for i in range(5):
#     x1 = random.randint(0, 300)
#     y1 = random.randint(0, 300)
#     x2 = random.randint(0, 300)
#     y2 = random.randint(0, 300)
#     platno.create_line(x1, y1, x2, y2, width=2)

# mainloop()
# #2
# hlavni = Tk()

# platno = Canvas(hlavni, width=400, height=400)
# platno.pack()

# x = random.randint(50, 350)
# y = random.randint(50, 350)
# r = 15 

# kruh = platno.create_oval(x - r, y - r, x + r, y + r, fill="pink", outline="green")

# def presun_kruh(udalost):
#     platno.coords(kruh, udalost.x - r, udalost.y - r, udalost.x + r, udalost.y + r)

# platno.bind("<Button-1>", presun_kruh)

# hlavni.mainloop()

#3
hlavni = Tk()

platno = Canvas(hlavni, width=500, height=500)
platno.pack()

start_x = 0
start_y = 0
obdelnik = None
def start(udalost):
    global start_x, start_y, obdelnik
    start_x = udalost.x
    start_y = udalost.y
    obdelnik = platno.create_rectangle(start_x, start_y, start_x, start_y, outline="black",dash=(4, 4), width=2)
def kresleni(udalost):
    global obdelnik
    platno.coords(obdelnik, start_x, start_y, udalost.x, udalost.y)
def uvolneni(udalost):
    global obdelnik
    platno.itemconfig(obdelnik, fill="green", dash=())

platno.bind("<ButtonPress-1>", start)
platno.bind("<B1-Motion>", kresleni)
platno.bind("<ButtonRelease-1>", uvolneni)

hlavni.mainloop()


# #4
# hlavni = Tk()

# platno = Canvas(hlavni,width=300, height=300)
# platno.pack()
# def nahodna():
#    while True:
#       nahod= random.randint(-5,5)
#       if nahod != 0:
#           return nahod

# obj = platno.create_oval(140,140,160,160, fill="green")
# smer1 = nahodna()
# smer2 = nahodna()

# def Pohyb():
#     global smer1,smer2
#     platno.move(obj,smer1,smer2)
#     sourad = platno.coords(obj)
#     if sourad[2]>=300 or sourad[0]<=0: 
#         smer1 = nahodna()
#     if sourad[3]>=300 or sourad[1]<=0: 
#         smer2 = nahodna()
#     hlavni.after(20, Pohyb)

# Pohyb()

#mainloop()



"""
Navíc:
1) Vykreslete šachovnici
2) Vykreslete hrací plochu pro Člověče, nezlob se   
"""

"""
Pro mistry
1) Zjistěte si aktuální čas a vykreslete ručičkové hodiny
"""


"""
x) Uživatel kliká na Canvas levým tlačítkem myši.
   Vykreslujte postupně s každým kliknutím
   lomenou čáru. Když klikneme pravým tlačítkem,
   čára se uzavře. (Musíme si pamatovat první bod)

   y) Uživatel kliká na Canvas. Vždy po třech kliknutích vykreslete
   trojúhelník.
"""

#xy
hlavni = Tk()

platno = Canvas(hlavni,width=300, height=300)
platno.pack()

body = []  

def kresli_lomenou_caru(udalost):
    global body
    body.append((udalost.x, udalost.y))  
    if len(body) > 1:
        platno.create_line(body[-2], body[-1], fill="black", width=2)

def uzavri_caru(udalost):
    if len(body) > 2:
        platno.create_line(body[-1], body[0], fill="black", width=2)
    body.clear() 

trojuhel = []
def kresli_trojuhelnik(udalost):
    global trojuhel
    trojuhel.append((udalost.x, udalost.y)) 
    if len(trojuhel) == 3:
        platno.create_polygon(trojuhel, outline="black", fill="", width=2)
        trojuhel.clear()  
def tecky(udalost):
    global trojuhel
    if len(trojuhel) > 1:
        platno.create_line(trojuhel[-2], trojuhel[-1], fill="black", width=2)

        

platno.bind("<ButtonPress-1>", kresli_lomenou_caru)
platno.bind("<ButtonPress-3>", uzavri_caru)
platno.bind("<ButtonPress-2>", kresli_trojuhelnik)  
platno.bind("<B2-Motion>", tecky)  

mainloop()








