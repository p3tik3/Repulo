class Jarat:
    def __init__(self, jaratszam, tipus, indulas, cel, jegyar):
        self.jaratszam = jaratszam
        self.tipus = tipus
        self.indulas = indulas
        self.cel = cel
        self.jegyar = jegyar

    def __str__(self):
        return f"{self.jaratszam}: {self.tipus}: {self.indulas} -> {self.cel}, Jegyár: {self.jegyar} Ft"
