# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012

@author: Radek
"""
"""     Soubory (textové)
open(cesta,mód) - otevře soubor a nastaví způsob
                  přístupu (mód)

módy:
  "r" - otevře daný soubor pro čtení, soubor musí
        existovat
  "r+" - otevře existující soubor jak pro čtení, tak 
        pro zápis
  "w" - otevře pro zápis, neexistující soubor bude
        vytvořen, existující soub. bude přepsán
  "a" - pro zápis na konec souboru, neexistující 
        bude vytvořen

close() - zavře soubor, způsobí uložení, uvolní jej
          pro jiné aplikace
flush() - vynucené uložení souboru
write() - zapíše do souboru daný řetězec na aktuální
          pozici
writelines() - zapíše do souboru seznam řádků         
  
"""

#data="Souborová data ze dne 27.9.2022"

# soubor=open("data.txt","w")  #systém se neptá a smaže!!!
# soubor.write(data)
# soubor.write("\n")
# soubor.write("Další data")
# soubor.close()

# soubor=open("data.txt","w")  
# x=0
# while x<1000000:         #pozor na nekonečný cyklus!!!
#     soubor.write(data)
#     x+=1
# soubor.close()



# import random
# soubor=open("cisla.txt","w")
# for i in range(100):
#     soubor.write(str(random.randint(1,1000))+"\n")
# soubor.close()


# seznam=["<html>\n","<head>\n","</head>\n","<body>\n","\n","</body>\n","</html>"]
# soubor=open("kostra.html","w")
# soubor.writelines(seznam)
# soubor.close()


# data2="\nDalší řádek souboru"
# soubor=open("data.txt","a")
# soubor.write(data2)
# soubor.close()


"""
Úkoly:
1) Zapište do souboru CISLA.TXT pod sebe čísla od 1 
   do 1000.
   (Rozšíření: ka každému číslu doplnit jeho dělitele)
"""

# soubor=open("CISLA.txt","w")
# for i in range(1,1001):
#     x=[]
#     z=[]
#     for y in range(1,i+1):  
#       if i%y==0:
#          x.append(str(y))
#     soubor.write(f"{i}:")
#     for y in x:
#        z.append(y)
#     soubor.write(f"{z},\n")
# soubor.close()
"""

2) Načtěte z klávesnice celý název souboru, načtěte 
   řetězec a zapište jej do zadaného souboru.
"""
# x = input("Zadejte název souboru: ")
# y = input("Zadejte, co chcete zapsat do souboru: ")
 
# soubor=open(x, "w")
# soubor.write(y)
# print("Řetězec byl zapsán do souboru:",x)
# soubor.close()

"""

3) Načtěte od uživatele 3 řetězce do seznamu a pomocí 
   operace WRITELINES zapište seznam do souboru.   
"""
# sez=[]
# for i in range(3):
#     sez.append(input("Zadejte řetězec: "))
    
# soubor=open("retezce3.txt","w")
# soubor.writelines(sez)
# soubor.close()
"""
4) Zapište do souboru "heslo.dat" náhodné heslo 
   složené z číslic a velkých písmen o délce 7 znaků.
"""
# import random
# sez=[]
# for i in range(7):
#    x=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
#    sez.append(x)
# soubor=open("hesla.dat", "w")
# soubor.writelines(sez)
# soubor.close()


"""

5) Do souboru tabulka.html vygenerujte html kód
   tabulky, která bude obsahovat odmocniny čísel od
   1 do 100.
   Bude mít dva sloupce, v řádcích bude vždy číslo a 
   odpovídající odmocnina zaokrouhlená na 2 místa.
"""   
# import math
# soubor = open("tabulka.html", "w")
# soubor.write("<html>\n<head>\n</head>\n<body>\n<table border=2 width=40%>\n")
# z = 1
# while z != 101:
#     y = math.sqrt(z)
#     row = "<tr>\n <td>{}</td>\n <td>{}</td>\n</tr>\n".format(z, y)
#     soubor.write(row)
#     z += 1
# soubor.write("</table>\n</body>\n</html>")
# soubor.close()
    

vstup=open("vstup.txt","r")
vystup=open("vystup.txt","w")
radek=vstup.readline()

for i in radek:
   cislo=int(radek[0])
   pismeno=radek[1]
for i in range(cislo):
   vystup.writelines(pismeno)

vystup.close()
vstup.close()

    
    
        





