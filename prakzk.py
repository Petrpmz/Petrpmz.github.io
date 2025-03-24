import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


hlavni=Tk()
hlavni.geometry("250x100")

def Otevrit():
    cesta = filedialog.askopenfilename(title="Otevřít soubor")
    if cesta != "":
        uhly = []
        hodnoty = []
    try:
        soubor=open(cesta,"r")
        vstup = soubor.readline()
        plt.title(vstup)
        vstup = soubor.readline()
        plt.xlabel(vstup)
        vstup = soubor.readline()
        plt.ylabel(vstup)

        vstup= soubor.readline()
        while(vstup != ""):
            seznam=vstup.split(" ")
            uhly.append(int(seznam[0]))
            hodnoty.append(int(seznam[1]))
            vstup=soubor.readline()

        soubor.close()
        plt.plot(uhly,hodnoty)
        plt.show()
    except:
        messagebox.showerror("HC","csac")

def Formular():
    global okno
    okno=Toplevel()
    okno.minsize(300,100)
    okno.title("graf fce")

    popisek1 = Label(okno, text= "X min:")
    popisek1.grid(row=0,column=0)
    inp_minx = Entry(okno)
    inp_minx.grid(row=0,column=1)

    
    popisek2 = Label(okno, text= "X max:")
    popisek2.grid(row=1,column=0)
    inp_maxx = Entry(okno)
    inp_maxx.grid(row=1,column=1)
    
    
    popisek3 = Label(okno, text= "Krok:")
    popisek3.grid(row=2,column=0)
    ikrok = Entry(okno)
    ikrok.grid(row=2,column=1)

    def Vykresli_graf():
        min_x= int(inp_minx.get())
        max_x= int(inp_maxx.get())
        krok= float(ikrok.get())
        x= np.arange(min_x,max_x,krok)
        y=np.cos(x)
        plt.plot(x,y)
        plt.show()  

    tlac= Button(okno, text="Vykreslit", command=Vykresli_graf)
    tlac.grid(row=3,column=0)


Hornimenu = Menu(hlavni)
Menusoubor= Menu(Hornimenu, tearoff=0)

Menusoubor.add_command(label="Otevrit", command=Otevrit)
Menusoubor.add_command(label="Vlastni funkce", command=Formular)
Menusoubor.add_command(label="Konec", command=hlavni.destroy)

Hornimenu.add_cascade(label="Menu", menu=Menusoubor)
hlavni.config(menu=Hornimenu)


mainloop()