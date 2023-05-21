# 120140048_Fitra Ilyasa

# kelas untuk menampung data data pelanggan
class AkunBank:

    # variabel kelas list (kosong) dan jumlah pelanggan 0
    listPelanggan = []
    jumlahPelanggan = 0

    # kontrukstor
    def __init__(self, noPelanggan, namaPelanggan, jumlahSaldo):
        self.noPelanggan = noPelanggan
        self.namaPelanggan = namaPelanggan
        self.__jumlahSaldo = jumlahSaldo

        # inisialisasi list data pelanggan 
        AkunBank.listPelanggan.append({"no": self.noPelanggan, "nama" : self.namaPelanggan, "saldo" : self.__jumlahSaldo})
        AkunBank.jumlahPelanggan += 1
    

    # method menu
    def lihatMenu(self):
        print("Halo {}, ingin melakukan apa?".format(self.namaPelanggan))
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Tranfer saldo")
        print("4. Keluar")

    # method lihat saldo
    def lihatSaldo(self):
        print("{} memiliki saldo Rp{}".format(self.namaPelanggan, self.__jumlahSaldo))
        print("")

    # untuk tarik saldo
    def tarikSaldo(self):
        jumlahTransfer = int(input("Berapa yang ingin ditarik? : "))

        # kondisi saldo ketika akan ditarik
        if jumlahTransfer <= self.__jumlahSaldo:
            self.__jumlahSaldo -= jumlahTransfer
            print("Saldo berhasil ditarik!")
            print("Saldo anda sekarang {}".format(self.__jumlahSaldo))
        else:
            print("Saldo anda tidak cukup!")

        print()

    # method transfer saldo
    def transferSaldo(self):
        jumlahTransfer = int(input("Masukan nominal yang ingin di transfer : "))

        # kondisi saldo ketika akan ditransfer
        if jumlahTransfer <= self.__jumlahSaldo:
            noRekening = int(input("Masukan no rekening yang ingin di transfer : "))
            for i in range(AkunBank.jumlahPelanggan):
                if AkunBank.listPelanggan[i]["no"] == noRekening:
                    print("Berhasil transfer ke {} sebesar Rp{}".format(AkunBank.listPelanggan[i]["nama"], jumlahTransfer))
                    self.__jumlahSaldo -= jumlahTransfer
                    print("Saldo anda sekarang {}".format(self.__jumlahSaldo))
                    break
                if i == AkunBank.jumlahPelanggan - 1:
                    print("No rekening tujuan tidak dikenali!")
        else:
            print("Saldo anda tidak cukup!")
        print("")

# instansiasi objek
akun1 = AkunBank(1234, "Fitra", 5000000000)
akun2 = AkunBank(1235, "Ukraina", 6666666666)
akun3 = AkunBank(1236, "Elon Musk", 9999999999)

print("Selamat datang di Bank Jago!")
# Pilihan menu
pilihan = 0
while pilihan != 4:
    akun1.lihatMenu()

    pilihan = int(input("Masukkan Nomor Input: "))

    if pilihan == 1:
        akun1.lihatSaldo()
    elif pilihan == 2:
        akun1.tarikSaldo()
    elif pilihan == 3:
        akun1.transferSaldo()
    elif pilihan == 4:
        break
   

