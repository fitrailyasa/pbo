# 120140048_Fitra Ilyasa
# Soal 1

# method input buku
def inputBuku():
    nama = input("Masukkan Nama Buku: ")
    genre = input("Masukkan Genre Buku: ")
    penulis = input("Masukkan Penulis Buku: ")
    tahun = int(input("Masukkan Tahun Terbit Buku: "))

    dataBuku = {'nama':nama, 'genre':genre, 'penulis':penulis, 'tahun':tahun} 
    return dataBuku

# Kelas Toko Buku
class TokoBuku:
    __listBuku = []
    def __init__(self):
        jumlahBuku = int(input("Masukkan Jumlah Buku Mula-mula: "))
        
        for i in range(jumlahBuku):
            print()
            dataBuku = inputBuku()
            
            self.__listBuku.append(dataBuku)
        
        if self.__listBuku:
            print("Buku Berhasil Ditambahkan!")

    # method tambah buku
    def tambahBuku(self):
        dataBuku = inputBuku()

        self.__listBuku.append(dataBuku)
        
        if self.__listBuku:
            print("Buku Berhasil Ditambahkan!")

    # method list buku
    def lihatlistBuku(self):
        for i in self.__listBuku:
            print(i['nama'],i['genre'],i['penulis'],i['tahun'])

    # method modifikasi buku
    def modifikasiBuku(self):
        cariNamaBuku = input("Masukkan Nama Buku Yang Dimodifikasi: ")
        
        for i in range(len(self.__listBuku)):
            if self.__listBuku[i]['nama'] == cariNamaBuku:
                print()
                dataBuku = inputBuku()
                self.__listBuku[i] = dataBuku
                print("Buku Berhasil Dimodifikasi!")
                break
        else:
            print("Nama Buku Tidak Ditemukan!")

    # method hapus buku
    def hapusBuku(self):
        cariNamaBuku = input("Masukkan Nama Buku Yang Dihapus: ")
        
        for i in range(len(self.__listBuku)):
            if self.__listBuku[i]['nama'] == cariNamaBuku:
                del(self.__listBuku[i])
                print("Buku Berhasil Dihapus!")
                break
        else:
            print("Nama Buku Tidak Ditemukan!")

# Instansiasi Objek
data = TokoBuku()

# Menu Pilihan
pilihan = 0
while pilihan != 5:
    print()
    print("Toko Buku Yang Jualan Buku")
    print("1) Tambah Buku Baru")
    print("2) Lihat List Buku")
    print("3) Modifikasi Buku Lama")
    print("4) Hapus Buku Lama")
    print("5) Keluar Program")
    pilihan = int(input("Masukkan Nomor Input: "))
    print()
    if pilihan == 1:
        data.tambahBuku()
    elif pilihan == 2:
        data.lihatlistBuku()
    elif pilihan == 3:
        data.modifikasiBuku()
    elif pilihan == 4:
        data.hapusBuku()
    elif pilihan == 5:
        break   
