# ----------------------
# Nama : Fitra Ilyasa
# NIM : 120140048
# Kelas : RD
# ----------------------

# Kelas Bunga
class Bunga:
  def __init__(self, nama, spesies, genus, famili, ordo, subkelas, kelas, divisi, superdivisi, kingdom):
    # Atribut
    self.nama = nama
    self.spesies = spesies
    self.genus = genus
    self.famili = famili
    self.ordo = ordo
    self.subkelas = subkelas
    self.kelas = kelas
    self.divisi = divisi
    self.superdivisi = superdivisi
    self.kingdom = kingdom
  
  # Fungsi/Method Data Klasifikasi Bunga
  def data_bunga(self):
      print("Nama         : {} ".format(self.nama))
      print("Spesies      : {} ".format(self.spesies))
      print("Genus        : {} ".format(self.genus))
      print("Famili       : {} ".format(self.famili))
      print("Ordo         : {} ".format(self.ordo))
      print("Sub-Kelas    : {} ".format(self.subkelas))
      print("Kelas        : {} ".format(self.kelas))
      print("Divisi       : {} ".format(self.divisi))
      print("Super Divisi : {} ".format(self.superdivisi))
      print("Kingdom      : {} ".format(self.kingdom))
      print("+====================================+")

# Instansiasi Objek
bunga1 = Bunga("Bunga Pagoda","Clerodendron paniculatum Vahl","Clerodendron","Verbenaccac","Lamiles","Asteridac","Magnoliopsida","Magnoliophyta","Spermatophyta","Plantae")
bunga2 = Bunga("Pisang Hias","Heliconia colisiana","Heliconia","Heliconiaceae","Zingiberales","Zengiberidae","Magnoliopsida","Magnoliophyta","Spermatophyta","Plantae")
bunga3 = Bunga("Kembang Kertas","Zinnia elegans Jacq","Zinnia","Asteraceae","Asterales","Asteridac","Magnoliopsida","Magnoliophyta","Spermatophyta","Plantae")

print("+====================================+")
print("|         KLASIFIKASI BUNGA          |")
print("+====================================+")

# Akses Atribut
print("1.",bunga1.nama)
print("2.",bunga2.nama)
print("3.",bunga3.nama)
print("+====================================+")

# Akses Method
bunga1.data_bunga()
bunga2.data_bunga()
bunga3.data_bunga()