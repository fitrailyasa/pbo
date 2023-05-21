# 120140048_Fitra Ilyasa

# Parent Class
class Goku():
    # konstruktor
    def __init__(self, warna_rambut, warna_mata):
        self.warna_rambut = warna_rambut
        self.warna_mata = warna_mata

# Child Class
class Gohan(Goku):
    # konstruktor
    def __init__(self,warna_rambut,warna_mata):
        Goku.__init__(self,warna_rambut,warna_mata) # inheritance

    # method gen
    def gen(self):
        print("Warna rambut Gohan: "+self.warna_rambut)
        print("Warna mata Gohan: "+self.warna_mata)

    # method turunan
    def turunan(Gohan): 
        return Gohan.gen() # overloading

# Instansiasi objek
anak1 = Gohan("Hitam","Coklat")
anak1.turunan()
