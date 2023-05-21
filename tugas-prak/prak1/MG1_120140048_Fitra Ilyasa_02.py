# 120140048_Fitra Ilyasa

# judul program
print("Permainan gunting batu kertas\n")
print("Pilih 1 untuk batu, 2 untuk kertas, 3 untuk gunting\n")
ulang = int(input("Berapa kali permainan: "))
hasil = {'pemain_a': 0, 'pemain_b': 0}

# ulang permainan
for i in range(ulang):
    print()
    print("Pilih 1 untuk batu, 2 untuk kertas, 3 untuk gunting")
    p1 = int(input("Tangan pemain A: "))
    p2 = int(input("Tangan pemain B: "))

    # tanding
    if (p1 == p2):
        hasil['pemain_a'] += 1
        hasil['pemain_b'] += 1
        print("Permainan Seri")
    else:
        if (p1 == 1):
            if (p2 == 2):
                hasil['pemain_b'] += 1
                print("Pemain B Menang")
            elif (p2 == 3):
                hasil['pemain_a'] += 1
                print("Pemain A Menang")
        elif (p1 == 2):
            if (p2 == 1):
                hasil['pemain_a'] += 1
                print("Pemain A Menang")
            elif (p2 == 3):
                hasil['pemain_b'] += 1
                print("Pemain B Menang")
        elif (p1 == 3):
            if (p2 == 1):
                hasil['pemain_b'] += 1
                print("Pemain B Menang")
            elif (p2 == 2):
                hasil['pemain_a'] += 1
                print("Pemain A Menang")
# cetak hasil
if(hasil['pemain_a'] > hasil['pemain_b']):
    print("Hasil Akhir - Pemain A menang dengan perolehan nilai: Pemain A: ", hasil['pemain_a'], ' dan Pemain B: ', hasil['pemain_b'])
elif(hasil['pemain_a'] < hasil['pemain_b']):
    print("Hasil Akhir - Pemain B menang dengan perolehan nilai: Pemain B: ", hasil['pemain_b'], ' dan Pemain A: ', hasil['pemain_a'])
elif(hasil['pemain_a'] == hasil['pemain_b']):
    print("Hasil Akhir - Permainan Seri")
        
        
