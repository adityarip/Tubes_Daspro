def tambahitem(Gadget,Consumable):
    def cari(X):
        for i in range(len(X)):
            if ID == X[i][0]:
                print("Gagal menambahkan item karena ID sudah ada")
                return False
        return True
    def belakang():
        for i in range(1,len(ID)):
            if not(48 <= ord(ID[i]) <= 57):
                print("Gagal menambahkan item karena ID tidak valid")
                return False
        return True
    def rar():
        if Rarity == "A" or Rarity == "B" or Rarity == "C" or Rarity == "S":
            return True
        else:
            print("Input rarity tidak valid")
            return False

    ID = input("Masukkan ID: ")
    if ID[0] == "C":
        if len(ID) > 1:
            if cari(Consumable):
                if belakang():
                    Nama = input("Masukkan Nama: ")
                    Deskripsi = input("Masukkan Deskripsi: ")
                    Jumlah = int(input("Masukkan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if rar():
                        print("Item telah berhasil ditambahkan ke dalam database")
                        Consumable.append([ID,Nama,Deskripsi,str(Jumlah),Rarity])
        else:
            print("ID tidak valid")
    elif ID[0] == "G":
        if len(ID) > 1:
            if cari(Gadget):
                if belakang():
                    Nama = input("Masukkan Nama: ")
                    Deskripsi = input("Masukkan Deskripsi: ")
                    Jumlah = int(input("Masukkan Jumlah: "))
                    Rarity = input("Masukkan Rarity: ")
                    if rar():
                        Tahun = int(input("Masukkan tahun: "))
                        print("Item telah berhasil ditambahkan ke dalam database")
                        Gadget.append([ID, Nama, Deskripsi, str(Jumlah), Rarity, str(Tahun)])
        else:
            print("ID tidak valid")
    else:
        print("Gagal menambahkan item karena ID tidak valid")
    print()

def hapusitem(Gadget,Consumable):
    ID = input("Masukkan ID: ")
    def cari(X):
        for i in range(len(X)):
            if ID == X[i][0]:
                tanya = input(f'Apakah Anda yakin menghapus {X[i][1]}? : ')
                if tanya == "Y" or tanya == "y":
                    print(f"{X[i][1]} telah dihapus")
                    X.remove(X[i])
                    return True
                elif tanya == "N" or tanya == "n":
                    print(f'{X[i][1]} tetap ada')
                    return False
                else:
                    print("Masukan tidak valid")
                    return False
        print("ID tidak ditemukan")
        return False
    if ID[0] == "C":
        if len(ID) > 1:
            cari(Consumable)
        else:
            print("ID tidak valid")
    elif ID[0] == "G":
        if len(ID) > 1:
            cari(Gadget)
        else:
            print("ID tidak valid")
    else:
        print("ID tidak valid")
    print()
