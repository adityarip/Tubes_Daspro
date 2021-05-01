def register(User):
    #Register user baru
    #Input: array User
    #Output: bertambah data user pada array User
    def cek():  #mengecek apakah username unik
        for i in range(len(User)):
            if username == str(User[i][2]):
                return False
        return True

    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    if cek() and username != "exit":   #jika username unik
        password = input("Masukkan password: ")
        alamat = input("Masukkan alamat: ")
        id = len(User)
        User.append([('U'+str(id)),nama,username,password,alamat,'user'])   #memasukkan user baru ke array User
        print(f'User {username} telah berhasil register ke dalam kantong ajaib')
    else:
        print("Username sudah terdaftar")
    print()