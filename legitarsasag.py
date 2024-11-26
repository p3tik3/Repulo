from jarat import Jarat

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = {}
        self.foglalasok = []

    def hozzaad_jarat(self, jarat):
        self.jaratok[jarat.jaratszam] = jarat

    def hozzaad_foglalas(self, jaratszam, utazo_nev):
        if jaratszam in self.jaratok:
            self.foglalasok.append((utazo_nev, jaratszam))
        else:
            print(f"Hiba: {jaratszam} járat nem található!")
    def foglalas_keszitese(self):
        jaratszam = input("Add meg a járatszámot: ")
        utas_nev = input("Add meg az utas nevét: ")

        if jaratszam in self.jaratok:
            self.foglalasok.append((utas_nev, jaratszam))
            print("Foglalás sikeres!")
        else:
            print("Hiba: Nem létezik ilyen járat!")

    def foglalas_lemondasa(self):
        utas_nev = input("Add meg az utas nevét: ")
        jaratszam = input("Add meg a járatszámot: ")

        if (utas_nev, jaratszam) in self.foglalasok:
            self.foglalasok.remove((utas_nev, jaratszam))
            print("Foglalás sikeresen törölve!")
        else:
            print("Hiba: A foglalás nem található!")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            print("Foglalások listája:")
            for utas, jaratszam in self.foglalasok:
                print(f"- {utas} a(z) {jaratszam} járaton.")
