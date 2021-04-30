
def cariNama(Nama,User):
    for i in range(len(User)):
        if Nama == User[i][0]:
            nama = User[i][1]
            return nama

def cariItem(idItem,item):
    for i in range(len(item)):
        if idItem == item[i][0]:
            nama = item[i][1]
            return nama

def lihatPinjam(Riwayat_pinjam,User,Gadget):
    def out(i,riwayat,Nama,item):
        print(f"ID peminjaman       : {riwayat[i][0]}")
        print(f"Nama peminjam       : {Nama}")
        print(f"Nama Gadget         : {item}")
        print(f"Tanggal peminjaman  : {riwayat[i][3]}")
        print(f"Jumlah              : {riwayat[i][4]}")
        print()

    idx = len(Riwayat_pinjam)
    if idx == 1:
        print("Tidak ada riwayat peminjaman gadget")
        print()
        return
    #jika riwayat peminjaman ada
    else:
        if idx <= 6:
            for i in range(idx-1,0,-1):
                out(i,Riwayat_pinjam,cariNama(Riwayat_pinjam[i][1],User),cariItem(Riwayat_pinjam[i][2],Gadget))
        #riwayat peminjaman lebih dari 5 entri
        else:
            while idx > 6:
                for i in range(idx-1,idx-6,-1):
                    out(i,Riwayat_pinjam,cariNama(Riwayat_pinjam[i][1],User),cariItem(Riwayat_pinjam[i][2],Gadget))
                nex = input("Apakah anda ingin melihat entri selanjutnya? (y/n) ")
                if nex == "y" or nex == "Y":
                    idx -= 5
                else:
                    return
            if idx <= 6 and idx > 1:
                for i in range(idx-1,0,-1):
                    out(i,Riwayat_pinjam,cariNama(Riwayat_pinjam[i][1],User),cariItem(Riwayat_pinjam[i][2],Gadget))

def lihatKembali(Riwayat_kembali,Riwayat_pinjam,User,Gadget):
    def out(i,riwayat,Nama,item):
        print(f"ID pengembalian     : {riwayat[i][0]}")
        print(f"Nama pengembali     : {Nama}")
        print(f"Nama Gadget         : {item}")
        print(f"Tanggal pengembalian: {riwayat[i][3]}")
        print(f"Jumlah              : {riwayat[i][2]}")
        print()

    idx = len(Riwayat_kembali)
    if idx == 1:
        print("Tidak ada riwayat pengembalian gadget")
        print()
        return
    #jika riwayat pengembalian ada
    else:
        if idx <= 6:
            for i in range(idx-1,0,-1):
                for j in range(len(Riwayat_pinjam)):
                    if Riwayat_kembali[i][1] == Riwayat_pinjam[j][0]:
                        out(i,Riwayat_kembali,cariNama(Riwayat_pinjam[j][1],User),cariItem(Riwayat_pinjam[j][2],Gadget))
        #riwayat pengembalian lebih dari 5 entri
        else:
            while idx > 6:
                for i in range(idx-1,idx-6,-1):
                    for j in range(len(Riwayat_pinjam)):
                        if Riwayat_kembali[i][1] == Riwayat_pinjam[j][0]:
                            out(i,Riwayat_kembali,cariNama(Riwayat_pinjam[j][1],User),cariItem(Riwayat_pinjam[j][2],Gadget))
                nex = input("Apakah anda ingin melihat entri selanjutnya? (y/n) ")
                if nex == "y" or nex == "Y":
                    idx -= 5
                else:
                    return
            if idx <= 6 and idx > 1:
                for i in range(idx-1,0,-1):
                    for j in range(len(Riwayat_pinjam)):
                        if Riwayat_kembali[i][1] == Riwayat_pinjam[j][0]:
                            out(i,Riwayat_kembali,cariNama(Riwayat_pinjam[j][1],User),cariItem(Riwayat_pinjam[j][2],Gadget))

def lihatAmbil(Riwayat_ambil,User,Consumable):
    def out(i,riwayat,Nama,item):
        print(f"ID pengambilan      : {riwayat[i][0]}")
        print(f"Nama pengambil      : {Nama}")
        print(f"Nama Consumable     : {item}")
        print(f"Tanggal pengambilan : {riwayat[i][3]}")
        print(f"Jumlah              : {riwayat[i][4]}")
        print()

    idx = len(Riwayat_ambil)
    if idx == 1:
        print("Tidak ada riwayat pengambilan consumable")
        print()
        return
    #jika riwayat pengambilan ada
    else:
        if idx <= 6:
            for i in range(idx-1,0,-1):
                out(i,Riwayat_ambil,cariNama(Riwayat_ambil[i][1],User),cariItem(Riwayat_ambil[i][2],Consumable))
        #riwayat pengambilan lebih dari 5 entri
        else:
            while idx > 6:
                for i in range(idx-1,idx-6,-1):
                    out(i,Riwayat_ambil,cariNama(Riwayat_ambil[i][1],User),cariItem(Riwayat_ambil[i][2],Consumable))
                nex = input("Apakah anda ingin melihat entri selanjutnya? (y/n) ")
                if nex == "y" or nex == "Y":
                    idx -= 5
                else:
                    return
            if idx <= 6 and idx > 1:
                for i in range(idx-1,0,-1):
                    out(i,Riwayat_ambil,cariNama(Riwayat_ambil[i][1],User),cariItem(Riwayat_ambil[i][2],Consumable))


            