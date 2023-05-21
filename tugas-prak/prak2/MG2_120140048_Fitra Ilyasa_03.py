# 120140048_Fitra Ilyasa
# Soal 3

# Kelas Game Kuis Sederhana
class GameKuis:
    # konstruktor
    def __init__(self, namaPemain):
        print("GAME KUIS SEDERHANA")
        print("Halo",namaPemain)
        print("Selamat bermain!")
        
    # method skor
    def hasil(self):
        skor = 0

        jawaban = input('Apa kepanjangan dari CPU? \n')
        if jawaban.lower() == 'central processing unit':
            print("Benar")
            skor += 1
        else:
            print('Kurang tepat')
         
        jawaban = input('Apa kepanjangan dari GPU? \n')
        if jawaban.lower() == 'graphical processing unit':
            print("Benar")
            skor += 1
        else:
            print('Kurang tepat')

        jawaban = input('Apa kepanjangan dari RAM? \n')
        if jawaban.lower() == 'random access memory':
            print("Benar")
            skor += 1
        else:
            print('Kurang tepat')

        jawaban = input('Apa kepanjangan dari ROM? \n')
        if jawaban.lower() == 'read only memory':
            print("Benar")
            skor += 1
        else:
            print('Kurang tepat')

        jawaban = input('Mouse termasuk input device atau ouput device? \n')
        if jawaban.lower() == 'input device':
            print("Benar")
            skor += 1
        else:
            print('Kurang tepat')
            
        print("Kamu mendapatakan " + str(skor) + " jawaban yang benar")
        print("Skor kamu " + str((skor/5) *100)+ " poin!")

# Instansiasi Objek
kuis1 = GameKuis("Fitra")
kuis1.hasil()
