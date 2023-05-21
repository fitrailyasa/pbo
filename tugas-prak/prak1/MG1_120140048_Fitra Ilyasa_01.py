# 120140048_Fitra Ilyasa

# input bilangan
bil = int(input("Masukkan bilangan: "))
print("Faktor dari", bil, "adalah:")

# ulang faktor dari bilangan
for i in range(1, bil+1):
    if bil % i == 0:
        print(i, end=" ")
