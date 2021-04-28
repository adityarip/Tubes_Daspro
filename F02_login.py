import sys

def login(User):
    #Login ke program dengan input username dan password dari user
    #Mengembalikan ID jika username dan password benar
    username = input("Username  : ")
    if username == "exit":
        sys.exit()
    password = input("Password  : ")
    for i in range (len(User)):     
        if username == User[i][2]:  #mengecek jika username benar
            if password == User[i][3]:  #mengecek jika password benar
                nama = User[i][1]
                if User[i][5] == "admin": #login sebagai admin
                    print(f"Halo admin {nama}! Selamat datang di Kantong Ajaib.\n")
                    ID = User[i][0] #ID admin yang login
                    return ID
                else: #login sebagai user
                    print(f"Halo {nama}! Selamat datang di Kantong Ajaib.\n")
                    ID = User[i][0] #ID user yang login
                    return ID 
    print("Username/Password salah!\n")
    return False


