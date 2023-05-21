# 120140048_Fitra ilyasa

# judul program (inputan)
kata = input("Masukkan kata: ") 
metode = input("Metode (1 = enkripsi, 2 = dekripsi): ")
pembagi = int(input("Jumlah pembagian huruf: "))
tmp = ""

# mengabaikan spasi
for i in kata:
    if i != " ":
        tmp += i

# memisahkan kata/kalimat menjadi per huruf/karakter
tmp,kata = kata,tmp
tmp = len(kata) % pembagi

# jika jumlah kata/kalimat tidak habis dibagi tambah 0
if tmp != 0:
    kata += ("0" * (pembagi - tmp))
tmp = int(len(kata) / pembagi)

# cetak hasil
print("\nHasil: ", end="")

# kondisi jika pilihan 1 = enkripsi
if metode == "1":	
    for i in range(pembagi):
        for j in range(tmp):
            print(kata[j * pembagi + i], end="")
        print("",end=" ")
        
# kondisi jika pilihan 2 = dekripsi
elif metode == "2":
    for i in range(tmp):
        for j in range(pembagi):
            if kata[j * tmp + i] != "0":
                print(kata[j * tmp + i], end=" ")
