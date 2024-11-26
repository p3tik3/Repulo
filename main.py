from legitarsasag import LegiTarsasag
from jarat import Jarat

def main():
    legitarsasag = LegiTarsasag("Péter Airlines")


    legitarsasag.hozzaad_jarat(Jarat("JARAT1", "Belföldi", "Debrecen", "Budapest", 8900))
    legitarsasag.hozzaad_jarat(Jarat("JARAT2", "Belföldi", "Szeged", "Debrecen", 19000))
    legitarsasag.hozzaad_jarat(Jarat("JARAT3", "Nemzetközi", "London", "Dunakeszi", 49999))

    legitarsasag.hozzaad_foglalas("JARAT1", "Minta Milán")
    legitarsasag.hozzaad_foglalas("JARAT1", "Gipsz Jakab")
    legitarsasag.hozzaad_foglalas("JARAT2", "Trab Antal")
    legitarsasag.hozzaad_foglalas("JARAT2", "Para Zita")
    legitarsasag.hozzaad_foglalas("JARAT3", "Kis Irma")
    legitarsasag.hozzaad_foglalas("JARAT3", "Mezei Virág")

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Foglalás készítése")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            legitarsasag.foglalas_keszitese()
        elif valasztas == "2":
            legitarsasag.foglalas_lemondasa()
        elif valasztas == "3":
            legitarsasag.foglalasok_listazasa()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás. Próbáld újra!")

if __name__ == "__main__":
    main()
