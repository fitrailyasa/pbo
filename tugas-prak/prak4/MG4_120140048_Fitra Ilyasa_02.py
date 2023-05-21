# 120140048_Fitra Ilyasa

# Parent class
class Robot:
    # konstruktor
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage
        self.jumlah_turn = 0

    # menyerang lawan
    def lakukan_aksi(self, target):
        print(f"Robot ({self.nama}) menyerang sebanyak {self.damage} DMG")

        # menambah darah
        target.health -= self.damage
        if self.jumlah_turn % self.turn == 0:
            self.health += self.health_up
            self.damage *= self.damage_up
            print(f"Robot ({self.nama}) menambah darah sebanyak {self.damage_up} HP")

# Child class
class Antares(Robot):
    # konstruktor
    def __init__(self):
        super().__init__("Antares", 50000, 5000)
        self.turn = 3
        self.damage_up = 1.5
        self.health_up = 0

# Child class
class Alphasetia(Robot):
    # konstruktor
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)
        self.turn = 3
        self.damage_up = 1
        self.health_up = 4000

# Child class
class Lecalicus(Robot):
    # konstruktor
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)
        self.turn = 4
        self.damage_up = 2
        self.health_up = 7000

# Parent class
class Main:
    # konstruktor
    def __init__(self):
        self.robots = [Antares(), Alphasetia(), Lecalicus()]
        self.robotA = None
        self.robotB = None
        self.turn = 0

    # method mulai
    def mulai(self):
        print("Selamat datang di pertandingan robot Yamako")
        self.pilih_robot()
        self.ulang()

    # method pilih robot
    def pilih_robot(self):
        robotA = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
        robotB = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
        self.robotA = self.robots[robotA - 1]
        self.robotB = self.robots[robotB - 1]
        print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")

    # method untuk mengulang
    def ulang(self):
        self.turn += 1
        self.robotA.jumlah_turn += 1
        self.robotB.jumlah_turn += 1
        print(f"\nTurn saat ini: {self.turn}")
        self.status()
        
        # input pilih robot
        pilihanA = int(input(f"Pilih tangan robotmu ({self.robotA.nama}): "))
        pilihanB = int(input(f"Pilih tangan lawan ({self.robotB.nama}): "))

        # kondisi ketika salah satu robot menang
        if (pilihanA == 1 and pilihanB == 3) or (pilihanA == 2 and pilihanB == 1) or (pilihanA == 3 and pilihanB == 2):
            self.robotA.lakukan_aksi(self.robotB)
        else:
            self.robotB.lakukan_aksi(self.robotA)
            
        self.pemenang()
        self.ulang()

    # method status robot
    def status(self):
        saya, lawan = self.robotA, self.robotB
        print(f"Robotmu ({saya.nama} - {saya.health} HP), robot lawan ({lawan.nama} - {lawan.health} HP)")

    # method pemenang
    def pemenang(self):
        if self.robotB.health <= 0:
            print(f"\nRobot ({self.robotA.nama}) menang.")
            exit()
        if self.robotA.health <= 0:
            print(f"\nRobot ({self.robotB.nama}) menang.")
            exit()

# Instansiasi objek
main1 = Main()
main1.mulai()
