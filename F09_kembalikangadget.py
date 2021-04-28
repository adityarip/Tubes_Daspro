from time import strftime

def kembalikan(ID_user,Gadget,Riwayat_pinjam,Riwayat_kembali):
    def cekInt(x):
        for i in range(len(x)):
            if not(48 <= ord(x[i]) <= 57):
                return False
        return True

    tanggal = strftime("%d/%m/%Y")
    count = 0
    ID = []
    for i in range(len(Riwayat_pinjam)):
        #Mencari semua gadget yang dipinjam user
        if ID_user == Riwayat_pinjam[i][1] and (str(Riwayat_pinjam[i][5]) == "False"):
            for j in range(len(Gadget)):
                if Riwayat_pinjam[i][2] == Gadget[j][0]:
                    count += 1
                    nama = Gadget[j][1]
                    jumlah = Riwayat_pinjam[i][4]
                    ID.append(Riwayat_pinjam[i][0])
                    print(f"{count}. {nama} (x{jumlah})")

    
    if count == 0: #jika user tidak meminjam gadget
        print("Anda tidak meminjam gadget apapun")
    else: #ada gadget yang terpinjam
        kembali = input("Masukkan nomor peminjaman: ")
        if cekInt(kembali):
            if (int(kembali) <= count) and (int(kembali) > 0):
                for i in range (len(Riwayat_pinjam)):
                    if ID[int(kembali)-1] == Riwayat_pinjam[i][0]:
                        jumlah = input("Masukkan jumlah yang ingin dikembalikan: ")
                        if cekInt(jumlah):
                            jumlah = int(jumlah)
                            if (jumlah) >= 0 and (jumlah <= int(Riwayat_pinjam[i][4])):
                                Riwayat_pinjam[i][4] = int(Riwayat_pinjam[i][4]) - jumlah
                                if int(Riwayat_pinjam[i][4]) == 0:
                                    Riwayat_pinjam[i][5] = True
                                Riwayat_kembali.append(["R"+ str(len(Riwayat_kembali)),Riwayat_pinjam[i][0],str(jumlah),tanggal])
                                for j in range(len(Gadget)):
                                    if Riwayat_pinjam[i][2] == Gadget[j][0]:
                                        Gadget[j][3] = int(Gadget[j][3]) + jumlah
                                        nama = Gadget[j][1]
                                print(f"Item {nama} (x{jumlah}) telah dikembalikan pada tanggal {tanggal}")
                            else:
                                print("Jumlah tidak valid")
                        else:
                            print("Jumlah tidak valid")
            else:
                print("Inputan tidak valid")
        else:
            print("Inputan tidak valid")
    print()