def ubahjumlah(Gadget,Consumable):
    def cari(X):
        for i in range(len(X)):
            if ID == X[i][0]:
                return True
        print("Tidak ada item dengan ID tersebut")
        return False
    
    ID = input("Masukkan ID: ")
    if ID[0] == "G":
        if cari(Gadget):
            jumlah = int(input("Masukkan Jumlah: "))
            for i in range(len(Gadget)):
                if ID == Gadget[i][0]:
                    count = int(Gadget[i][3])
                    if jumlah >= 0:
                        count +=  jumlah
                        Gadget[i][3] = count
                        print(f"{jumlah} {Gadget[i][1]} berhasil ditambahkan. Stok sekarang: {(Gadget[i][3])}")
                    else: #jumlah < 0
                        jumlah *= -1
                        if count - jumlah >= 0:
                            count -=  jumlah
                            Gadget[i][3] = count
                            print(f"{jumlah} {Gadget[i][1]} berhasil dibuang. Stok sekarang:  {(Gadget[i][3])}")
                        else: #count - jumlah < 0
                            print(f"{jumlah} {Gadget[i][1]} gagal dibuang karena stok kurang. Stok sekarang: {(Gadget[i][3])} (< {jumlah} )")

    elif ID[0] == "C":
        if cari(Consumable):
            jumlah = int(input("Masukkan Jumlah: "))
            for i in range(len(Consumable)):
                if ID == Consumable[i][0]:
                    count = int(Consumable[i][3])
                    if jumlah >= 0:
                        count +=  jumlah
                        Consumable[i][3] = count
                        print(f"{jumlah} {Consumable[i][1]} berhasil ditambahkan. Stok sekarang: {(Consumable[i][3])}")
                    else: #jumlah < 0
                        jumlah *= -1
                        if count - jumlah >= 0:
                            count -=  jumlah
                            Consumable[i][3] = count
                            print(f"{jumlah} {Consumable[i][1]} berhasil dibuang. Stok sekarang:  {(Consumable[i][3])}")
                        else: #count - jumlah < 0
                            print(f"{jumlah} {Consumable[i][1]} gagal dibuang karena stok kurang. Stok sekarang: {(Consumable[i][3])} (< {jumlah} )")
    else: #ID[0] tidak "C" atau "G"
        print("ID tidak valid")
    print()
