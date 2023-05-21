username="informatika"
password="12345678"

def login():
    x=input("Username anda :")
    y=input("Password anda :")

    if(x == username and y == password):
        print("Berhasil login!")
    elif(x != username or y != password):
        print("Username atau Password anda salah coba lagi")
        login()
