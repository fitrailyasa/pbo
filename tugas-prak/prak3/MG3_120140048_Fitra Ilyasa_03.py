class Coba:
    def __init__(self, nama, panggilan, umur):
        self.nama = nama # Public
        self._panggilan = panggilan # Protected
        self.__umur = umur # Private

    def cetakUmur(self):
        return self.__umur
    
coba = Coba("Fitra Ilyasa","Nde",20)

print("Nama Lengkap :",coba.nama) # dapat diakses dimana saja
print("Panggilan    :",coba._panggilan) # hanya dapat diakses dikelas dan sub kelas
print("Umur         :",coba.cetakUmur()) # hanya dapat diakses dikelas tersebut
