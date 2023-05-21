# method input buku
def input_buku():
    nama = input("Masukkan nama buku: ")
    genre = input("Masukkan genre buku: ")
    penulis = input("Masukkan penulis: ")
    tahun = input("Masukkan tahun terbit: ")

    data_buku = {'nama':nama,'genre':genre,'penulis':penulis,'tahun':tahun}
    return data_buku

# Kelas Toko Buku
class TokoBuku:
    __list_buku = []
    def __init__(self):
        jumlah_buku = int(input("Masukkan jumlah buku mula-mula: "))

        for i in range(jumlah_buku):
            data_buku = input_buku()
            self.__list_buku.append(data_buku)
            print("")

        if self.__list_buku:
            print("Buku berhasil ditambahkan!")
            print("")

    # method tambah buku
    def tambah_buku(self):
        data_buku = input_buku()
        self.__list_buku.append(data_buku)

        if self.__list_buku:
            print("Buku berhasil ditambahkan!")
    
    # method lihat buku
    def lihat_list_buku(self):
        for i in self.__list_buku:
            print(i['nama'],i['genre'],i['penulis'],i['tahun'])
    
    # method modifikasi buku
    def modifikasi_buku(self):
        cari_nama_buku = input("Cari nama buku yg akan dimodifikasi: ")

        for i in range(len(self.__list_buku)):
            if cari_nama_buku == self.__list_buku[i]['nama']:
                data_buku = input_buku()
                self.__list_buku[i] = data_buku
                print("Buku berhasil dimodifikasi!")
                break
            else:
                print("Buku tidak ditemukan!")
            
    
    # method hapus buku
    def hapus_buku(self):
        cari_nama_buku = input("Cari nama buku yg akan dihapus: ")

        for i in range(len(self.__list_buku)):
            if cari_nama_buku == self.__list_buku[i]['nama']:
                del(self.__list_buku[i])
                print("Buku berhasil dihapus!")
                break
            else:
                print("Buku tidak ditemukan!")

# instansiasi objek
buku = TokoBuku() 



# pilihan awalnya 0
pilihan = 0
# program diulang jika inputan bukan 1-5
while pilihan != 5:
    # Menu Pilihan
    print("")
    print("TOKO BUKU")
    print("1) Tambah Buku")
    print("2) Lihat List Buku")
    print("3) Modifikasi Buku Lama")
    print("4) Hapus Buku Lama")
    print("5) Keluar Program")
    
    pilihan = int(input("Masukkan nomor input: "))
    if pilihan == 1:
        buku.tambah_buku()
    elif pilihan == 2:
        buku.lihat_list_buku()
    elif pilihan == 3:
        buku.modifikasi_buku()
    elif pilihan == 4:
        buku.hapus_buku()
    elif pilihan == 5:
        break 
        

