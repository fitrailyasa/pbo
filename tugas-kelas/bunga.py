# ----------------------
# Nama : Fitra Ilyasa
# NIM : 120140048
# Kelas : RD
# ----------------------

# Kelas Bunga
class Bunga:
  def __init__(self, nama, jenis, warna):
    # Atribut
    self.nama = nama
    self.jenis = jenis
    self.warna= warna
  
  # Method Data Bunga
  def data_bunga(self):
      print("Nama         : {} ".format(self.nama))
      print("Spesies      : {} ".format(self.jenis))
      print("Warna        : {} ".format(self.warna))

# Instansiasi Objek
bunga1 = Bunga("Mawar","Bunga","Merah")
bunga2 = Bunga("Melati","Bunga","Putih")
bunga3 = Bunga("Anggrek Bulan ","Bunga Anggrek","Ungu")

print("KELAS BUNGA")

# Akses Atribut
print("+====================================+")
print("1.",bunga1.nama)
print("2.",bunga2.nama)
print("3.",bunga3.nama)
print("+====================================+")

# Akses Method
bunga1.data_bunga()
print("+====================================+")
bunga2.data_bunga()
print("+====================================+")
bunga3.data_bunga()
print("+====================================+")
