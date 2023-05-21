# 120140048_Fitra Ilyasa

# data mahasiswa
mhs = [
    {'nama': 'Andi', 'nim': 120140201, 'nilai': 76},
    {'nama': 'Mahmud', 'nim': 119140165, 'nilai': 94},
    {'nama': 'Rahman', 'nim': 120140222, 'nilai': 80}
]

# ulang data mahasiswa
for i in range(len(mhs)):
    print('Nama mahasiswa ',i+1,': ', mhs[i]['nama'],)
    print('NIM mahasiswa ',i+1,': ', mhs[i]['nim'],)
    print('Nilai mahasiswa ',i+1,': ', mhs[i]['nilai'])
print('')

# Sorting (Pengurutan Data)
urutkan_berdasarkan = input("Urutkan berdasarkan (nama/nim/nilai): ")
urutkan = input("Urutkan data ter (besar/kecil): ")
if (urutkan.lower() == "besar"):
    for i in range(len(mhs)):
        for n in range(i):
            if mhs[i][urutkan_berdasarkan] > mhs[n][urutkan_berdasarkan]:
                tmp = mhs[n]
                mhs[n] = mhs[i]
                mhs[i] = tmp
elif (urutkan.lower() == "kecil"):
    for i in range(len(mhs)):
        for n in range(i):
            if mhs[i][urutkan_berdasarkan] < mhs[n][urutkan_berdasarkan]:
                tmp = mhs[n]
                mhs[n] = mhs[i]
                mhs[i] = tmp
print('')

# cetak hasil
for i in range(len(mhs)):
    print(mhs[i]['nama'], mhs[i]['nim'], mhs[i]['nilai'])
    
