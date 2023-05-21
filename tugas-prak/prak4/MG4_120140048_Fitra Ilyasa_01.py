# 120140048_Fitra Ilyasa

# Parent class
class Komputer:
    # konstruktor
    def __init__(self, nama, jenis, merk, harga):
        self.nama = nama
        self.jenis = jenis
        self.merk = merk
        self.harga = harga

# Child class
class Processor(Komputer):
    # konstruktor
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor):
        super().__init__(nama, 'CPU', merk, harga)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

# Child class
class RAM(Komputer):
    # konstruktor
    def __init__(self, merk, nama, harga, capacity):
        super().__init__(nama, 'RAM', merk, harga)
        self.capacity = capacity

# Child class
class HDD(Komputer):
    # konstruktor
    def __init__(self, merk, nama, harga, capacity, rpm):
        super().__init__(nama, 'HDD', merk, harga)
        self.capacity = capacity
        self.rpm = rpm

# Child class
class VGA(Komputer):
    # konstruktor
    def __init__(self, merk, nama, harga, capacity):
        super().__init__(nama, 'VGA', merk, harga)
        self.capacity = capacity

# Child class
class PSU(Komputer):
    # konstruktor
    def __init__(self, merk, nama, harga, daya):
        super().__init__(nama, 'PSU', merk, harga)
        self.daya = daya

# Instansiasi objek
p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

# print rakitan komputer 1 & 2
komputer1 = [p1, ram1, hdd1, vga1, psu1]
print("")
print("Komputer 1")
for komponen in komputer1:    
    print(komponen.jenis, komponen.nama, "produksi", komponen.merk)

komputer2 = [p2, ram2, hdd2, vga2, psu2]
print("")
print("Komputer 2")
for komponen in komputer2:    
    print(komponen.jenis, komponen.nama, "produksi", komponen.merk)
