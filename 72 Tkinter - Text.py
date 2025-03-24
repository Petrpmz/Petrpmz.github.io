# -*- coding: utf-8 -*-
"""
Created on Tue Apr 09 11:31:49 2013

@author: Radek
"""
"""
Komponenta Text
---------------
metoda tag_config(název, font=, foreground=, underline=)
- definice stylu

metoda insert(řádek.pozice, řetězec, styl)
- vkládá do textového pole řetězec na zadaný řádek od dané pozice
- ano, tyto dva údaje se oddělují tečkou
- pokud daná pozice neexistuje, vkládá na konec textu
- vložený text je formátován zvoleným stylem

metoda get(od, do)
- získání řetězce z komponenty text

metoda delete(od, do)
- smázání vymezené části textu
"""

from tkinter import *

hlavni=Tk()
text=Text(hlavni)
text.pack(fill=BOTH, expand=1)

text.tag_config("modry", font="Arial 20 italic", foreground="blue", underline=1)
text.tag_config("cerveny", font="Arial 15 bold", foreground="red", underline=0)

text.insert(1.0,"Ahoj studenti!\n","modry")
text.insert(5.0, "Jak se máte?\n","cerveny")
text.insert(END, "To je dnes hezky...")

# text.insert(2.5, " (Vsuvka) ","modry")

smazat=Button(hlavni,text="Smazat vše", command=lambda: text.delete(1.0, END))
smazat.pack()

retezec=text.get(1.0, END)
print (retezec)

mainloop() 

"""
Úkol:
1) Vytvořte jednoduchý textový editor, který umožní
   uložit nebo načíst obsah komponenty text ze souboru.
   Tyto volby umožněte vybrat pomocí menu.
   Vše bez formátování = bez použití stylů.
   Použijte souborové dialogy.
   
   POZOR!
   - při stornování souborového dialogu nesmím nic otvírat
   - při otevření dalšího souboru musí předchozí obsah okna zmizet
""" 
import tkinter 
from tkinter import messagebox
def otevri_soubor():
    cesta = "soubor.txt"  
    soubor = open(cesta, "r")
    obsah = soubor.read()
    text.delete("1.0", "end")  
    text.insert("1.0", obsah)
    soubor.close()


def uloz_soubor():
    cesta = "soubor.txt"  
    soubor = open(cesta, "w")
    soubor.write(text.get("1.0", "end-1c"))
    soubor.close()

def smazat_soubor():
    odpoved = messagebox.askyesno("Potvrzení", "Opravdu?")
    if odpoved:
        text.delete("1.0", END)

hlavni = Tk()
hlavni.title("editor")
hlavni.geometry("600x500")


text = Text(hlavni, wrap=WORD)
text.pack(fill=BOTH, expand=1)


menu_bar = Menu(hlavni)
hlavni.config(menu=menu_bar)

soubor_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Soubor", menu=soubor_menu)

soubor_menu.add_command(label="Otevřít", command=otevri_soubor)
soubor_menu.add_command(label="Uložit", command=uloz_soubor)
soubor_menu.add_command(label="Smazat", command=smazat_soubor)
soubor_menu.add_command(label="Konec", command=hlavni.quit)


hlavni.bind("<Control-o>",otevri_soubor)
hlavni.bind("<Control-s>",uloz_soubor)
hlavni.bind("<Control-d>",smazat_soubor)


mainloop()

"""
1) Do menu přidejte položky:
"Smazat" - smaže celý obsah v komponentě Text
         - nejprve se zeptá, jestli opravdu chceme smazat
"Nahradit" - načte od uživatele, co má nahradit a čím (využijte
             buď vedlejší okno se dvěma vstupy a tlačítky "OK"
             a "Storno")
2) Přidat události klávesnice
Klávesová zkratka Ctrl + o - otevření souboru
Klávesová zkratka Ctrl + s - uložení souboru
Klávesová zkratka Ctrl + n - nahrazení v souboru
Klávesová zkratka Ctrl + d - smazání textu v komponentě
"""









