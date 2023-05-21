
#rumus = Pesan + Key = (angkaP + angkaK) % 26 = enkripsi
#T + P = (19 + 15) % 26 = 34 % 26 = 8 (I)


class Chiper:
    def __init__(self):
        self.kunci = input("Masukkan kunci (key): ")

    def enkripsi(self, teks):
        kunci = []
        for i,j in enumerate(self.kunci):
            if j.isupper(): # kapital
                kunci.append(ord(j) - ord('A')) # P = 80, A = 65 => 84 - 65 = 15
            elif j.islower(): # no kapital
                kunci.append(ord(j) - ord('a')) # p = 112, a = 97 => 112 - 97 = 15
        rumus = ""
        i = 0
        for j in teks:
            angka_kunci = kunci[i % len(self.kunci)] # TEKNIK => T = 116, E K N I K
            if j.isupper():
                angka_pesan = ord(j) - ord('A') # 19 = T - A = 80 - 65
                rumus += chr((angka_pesan + angka_kunci) % 26 + ord('A')) # (ASCII) I = 73
                i += 1
            elif j.islower():
                angka_pesan = ord(j) - ord('a') # 19 = t - a = 116 - 97
                rumus += chr((angka_pesan + angka_kunci) % 26 + ord('a')) # (ascii) i = 105
                i += 1
            else:
                rumus += j
        return rumus
    
    def dekripsi(self, teks):
        kunci = []
        for i,j in enumerate(self.kunci):
            if j.isupper(): # kapital
                kunci.append(ord(j) - ord('A')) # P = 80, A = 65 => 84 - 65 = 15
            elif j.islower(): # no kapital
                kunci.append(ord(j) - ord('a')) # p = 112, a = 97 => 112 - 97 = 15
        rumus = ""
        i = 0
        for j in teks:
            angka_kunci = kunci[i % len(self.kunci)] # TEKNIK => T = 116, E K N I K
            if j.isupper():
                angka_pesan = ord(j) - ord('A') # 19 = T - A = 80 - 65
                rumus += chr((angka_pesan - angka_kunci) % 26 + ord('A')) # (ASCII) I = 73
                i += 1
            elif j.islower():
                angka_pesan = ord(j) - ord('a') # 19 = t - a = 116 - 97
                rumus += chr((angka_pesan - angka_kunci) % 26 + ord('a')) # (ascii) i = 105
                i += 1
            else:
                rumus += j
        return rumus
    
    def ganti_kunci(self, kunci):
        self.kunci = kunci

    
# Instansiasi Objek
pesan = Chiper()

# pilihan awalnya 0
pilihan = 0
# program diulang jika inputan bukan 1-4
while pilihan != 4:
    # Menu Pilihan
    print("")
    print("VIGNERE CHIPER")
    print("1) Enkripsi plainteks")
    print("2) Dekripsi cipher")
    print("3) Ganti kunci (key)")
    print("4) Keluar Program")
    
    pilihan = int(input("Masukkan nomor input: "))
    if pilihan == 1:
        teks = input("Masukkan plainteks: ")
        print("Hasil enkripsi: ",pesan.enkripsi(teks))
    elif pilihan == 2:
        teks = input("Masukkan chiper: ")
        print("Hasil dekripsi: ",pesan.dekripsi(teks))
    elif pilihan == 3:
        kunci = input("Masukkan kunci (key) yang baru: ")
        pesan.ganti_kunci(kunci)
    elif pilihan == 4:
        break 
