# 120140048_Fitra Ilyasa
import random

# kelas Game Bom
class gameBom:

    # deklarasi variabel kelas yg awalnya bernilai 0
    jumlahBom = 0
    jumlahBuka = 0

    # kontruktor
    def __init__(self):
        # kondisi jika jumlah bom kurang dari sama dengan 4
        if gameBom.jumlahBom <= 4 :
            self.__isi = random.randrange(0, 2) # angka acak 0-2
            if self.__isi == 0:
                gameBom.jumlahBom += 1
        else:
            self.__isi = 1
        
        self.__status = 0

    # method buka kotak
    def buka(self):  
        self.__status = 1
        gameBom.jumlahBuka += 1 

    # method cek kotak
    def cek(self):
        if self.__status == 1 and self.__isi == 1:
            print("Selamat! Kotak tersebut tidak berisi bom.")
            return 1
        else:
            print("Game over! Kotak tersebut berisi bom.")
            return 0

    # method cetak
    def cetak(self):
        if self.__status == 0:
            print("?", end=" ")
        else:
            if self.__isi == 0:
                print("x", end=" ")
            else:
                print("o", end=" ")

print("Permainan Minesweeper")
dimensi = int(input("Masukan dimensi area: "))

# list dimensi
listDimensi = []

# instansiasi objek
for i in range(dimensi * dimensi):
    listDimensi.append(gameBom())

# tampilan pertama
print("")
for i in range(0, dimensi * dimensi):
    listDimensi[i].cetak()
    if (i + 1) % dimensi == 0:
        print("")
        
nomor = int(input("Masukan nomor yang ingin dibuka (1-9): "))
listDimensi[nomor - 1].buka()

# jika tidak mengenai bom maka akan diulang sampai menang
coba = True
while coba == True:
    print("")
    for i in range(0, dimensi * dimensi):
        listDimensi[i].cetak()
        if (i + 1) % dimensi == 0:
            print("")
            
    # kondisi ketika tidak mengenai bom
    if listDimensi[nomor - 1].cek() == 1:
        coba = True
        nomor = int(input("Masukan nomor yang ingin dibuka (1-9): "))
        listDimensi[nomor - 1].buka()

        # kondisi ketika bom habis dan menang
        if gameBom.jumlahBuka == dimensi - gameBom.jumlahBom:
            print("Selamat anda menang!")
            for i in range(n):
                listDimensi[i].buka()
                break
    else:
        break
