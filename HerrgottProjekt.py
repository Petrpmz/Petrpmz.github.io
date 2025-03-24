from tkinter import *
import random
import time

class Apka:
    def __init__(self, hlavni):
        self.hlavni = hlavni
        self.hlavni.title("Matematický Test")
        self.hlavni.geometry("500x400")
        self.vytvor_menu()

    def vytvor_menu(self):
        self.menu_frame = Frame(self.hlavni)
        self.menu_frame.pack(pady=20)

        Label(self.menu_frame, text="Vyberte operaci:").pack()
        self.operace = StringVar(value="sčítání")
        operace_moznosti = ["sčítání", "odčítání", "násobení", "dělení"]
        for op in operace_moznosti:
            Radiobutton(self.menu_frame, text=op, variable=self.operace, value=op).pack(anchor="w")

        Label(self.menu_frame, text="Počet příkladů:").pack()
        self.pocet = IntVar(value=5)
        for num in [5, 10, 15]:
            Radiobutton(self.menu_frame, text=str(num), variable=self.pocet, value=num).pack(anchor="w")

        Button(self.menu_frame, text="Spustit test", command=self.spustit_test).pack(pady=20)

    def spustit_test(self):
        self.menu_frame.destroy()
        self.priklady = self.pocet.get()
        self.spravne = 0
        self.spatne = 0
        self.aktualni = 0
        self.start_cas = time.time()
        self.vytvor_testovaci_okno()
        self.generuj_priklad()

    def vytvor_testovaci_okno(self):
        self.test_frame = Frame(self.hlavni)
        self.test_frame.pack(pady=20)
        self.otazka = Label(self.test_frame, text="", font=("Arial", 20))
        self.otazka.pack()
        self.odpoved = Entry(self.test_frame, font=("Arial", 20))
        self.odpoved.pack(pady=10)
        self.odpoved.bind("<Return>", self.over_odpoved)
        self.canvas = Canvas(self.test_frame, width=100, height=100)
        self.canvas.pack()

    def generuj_priklad(self):
        operace = self.operace.get()
        if operace == "sčítání":
            self.a = random.randint(1, 100)
            self.b = random.randint(1, 100 - self.a)
            self.vysledek = self.a + self.b
            self.otazka.config(text=f"{self.a} + {self.b} =")
        elif operace == "odčítání":
            self.a = random.randint(1, 100)
            self.b = random.randint(1, self.a)
            self.vysledek = self.a - self.b
            self.otazka.config(text=f"{self.a} - {self.b} =")
        elif operace == "násobení":
            self.a = random.randint(1, 10)
            self.b = random.randint(1, 10)
            self.vysledek = self.a * self.b
            self.otazka.config(text=f"{self.a} × {self.b} =")
        elif operace == "dělení":
            self.b = random.randint(1, 10)
            self.vysledek = random.randint(1, 10)
            self.a = self.b * self.vysledek
            self.otazka.config(text=f"{self.a} ÷ {self.b} =")

    def over_odpoved(self, udalost):
        try:
            odpoved = int(self.odpoved.get())
            self.odpoved.delete(0, END)
            if odpoved == self.vysledek:
                self.spravne += 1
                self.zpetna_vazba("green")
            else:
                self.spatne += 1
                self.zpetna_vazba("red")
            self.aktualni += 1
            if self.aktualni < self.priklady:
                self.generuj_priklad()
            else:
                self.zobraz_vysledek()
        except ValueError:
            self.odpoved.delete(0, END)

    def zpetna_vazba(self, barva):
        self.canvas.delete("all")
        self.canvas.create_text(50, 40, text="✓" if barva == "green" else "✗", font=("Arial", 40), fill=barva)
        self.canvas.create_text(50, 80, text="Správně" if barva == "green" else "Špatně", font=("Arial", 10), fill=barva)

    def zobraz_vysledek(self):
        self.test_frame.destroy()
        konec_cas = time.time()
        trvani = round(konec_cas - self.start_cas, 2)
        vysledek_frame = Frame(self.hlavni)
        vysledek_frame.pack(pady=50)
        Label(vysledek_frame, text=f"Správně: {self.spravne}").pack()
        Label(vysledek_frame, text=f"Špatně: {self.spatne}").pack()
        Label(vysledek_frame, text=f"Čas: {trvani} s").pack()
        Button(vysledek_frame, text="Nový test", command=self.restart).pack(pady=20)

    def restart(self):
        self.hlavni.destroy()
        hlavni = Tk()
        app = Apka(hlavni)
        hlavni.mainloop()

if __name__ == "__main__":
    hlavni = Tk()
    app = Apka(hlavni)
    hlavni.mainloop()