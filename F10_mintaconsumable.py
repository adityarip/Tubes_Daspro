from time import strftime

def minta(id_peminjam,Consumable,Riwayat_ambil): 
    def cek_id(X):
        for i in range (len(Consumable)):
            if X == Consumable[i][0]:
                return True
        return False
    def cek_jml(X):
        for i in range (len(X)):
            if not(48 <= ord(jumlah[i]) <= 57):
                return False
        return True

    ID = input("Masukkan ID: ")
    if cek_id(ID):
        jumlah = input("Masukkan jumlah: ")
        if cek_jml(jumlah):
            tanggal = strftime("%d/%m/%Y")
            print(f"Tanggal permintaan: {tanggal}")
            for i in range (len(Consumable)):
                if ID == Consumable[i][0]:
                    count = int(Consumable[i][3])
                    if int(jumlah) <= count:
                        count -= int(jumlah)
                        Consumable[i][3] = count
                        Riwayat_ambil.append(["M" + str(len(Riwayat_ambil)),str(id_peminjam),str(ID),str(tanggal),str(jumlah)])
                        print("Item " + str(Consumable[i][1] + " (x" + str(jumlah) + ") berhasil diambil!"))
                    else: #jumlah ambil > jumlah consum
                        print("Jumlah consumable tidak mencukupi")
        else:
            print("Jumlah harus berupa bilangan")
    else: #not(cek(ID))
        print("Tidak ada item dengan ID tersebut")
    print()