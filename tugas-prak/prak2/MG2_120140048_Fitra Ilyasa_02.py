# 120140048_Fitra Ilyasa
# Soal 2

# Kelas Pesan
class Pesan:
    def __init__(self):
        self.key = input("Masukkan Kunci (key): ")

    # method enkripsi
    def enkripsi(self, teks):
        kunci = []
        for i,j in enumerate(self.key):
            if j.isupper(): # Huruf Kapital
                # T = 84, A = 65 => 84 - 65 = 19
                # P = 80, A = 65 => 80 - 65 = 15
                kunci.append(ord(j) - ord('A'))
            elif j.islower(): # Bukan Huruf Kapital
                # t = 116, a = 97 => 116 - 97 = 19
                # p = 112, a = 97 => 112 - 97 = 15
                kunci.append(ord(j) - ord('a'))
        hasil = ""
        i = 0
        for j in teks:
            angkaKunci = kunci[i % len(self.key)]
            if j.isupper():
                angkaTeks = ord(j) - ord('A')
                #T + P = (19 + 15) % 26 = 34 % 26 + 65 = 8 => 8 + 65 = 73 (I)
                hasil += chr((angkaTeks + angkaKunci) % 26 + ord('A'))
                i += 1
            elif j.islower():
                angkaTeks = ord(j) - ord('a')
                #t + p = (19 + 15) % 26 = 34 % 26 = 8 => 8 + 97 = 105 (i)
                hasil += chr((angkaTeks + angkaKunci) % 26 + ord('a'))
                i += 1
            else:
                hasil += j
        return hasil

    # method dekripsi
    def dekripsi(self, teks):
        kunci = []
        for i,j in enumerate(self.key):
            if j.isupper(): 
                kunci.append(ord(j) - ord('A'))
            elif j.islower(): 
                kunci.append(ord(j) - ord('a'))
        hasil = ""
        i = 0
        for j in teks:
            angkaKunci = kunci[i % len(self.key)]
            if j.isupper():
                angkaTeks = ord(j) - ord('A')
                hasil += chr((angkaTeks - angkaKunci) % 26 + ord('A'))
                i += 1
            elif j.islower():
                angkaTeks = ord(j) - ord('a')
                hasil += chr((angkaTeks - angkaKunci) % 26 + ord('a'))
                i += 1
            else:
                hasil += j
        return hasil
    # method ganti kunci
    def gantiKunci(self, kunci):
        self.key = kunci

# Instasiasi Objek
pesan = Pesan()

# Menu Pilihan
pilihan = 0
while pilihan != 4:
    print("")
    print("Vigenere Cipher")
    print("1) Enkripsi Plainteks")
    print("2) Dekripsi Chiper")
    print("3) Ganti Kunci (key)")
    print("4) Keluar Program")

    pilihan = int(input("Masukkan Nomor Input: "))

    if pilihan == 1:
        teks = input("Masukkan Plainteks: ")
        print("Hasil Enkripsi: ", end="")
        print(pesan.enkripsi(teks))
    elif pilihan == 2:
        teks = input("Masukkan Cipher: ")
        print("Hasil Dekripsi: ", end="")
        print(pesan.dekripsi(teks))
    elif pilihan == 3:
        kunci = input("Masukkan Kunci (Key) Baru: ")
        pesan.gantiKunci(kunci)
    elif pilihan == 4:
        break
