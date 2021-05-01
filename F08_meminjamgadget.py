from time import gmtime,strftime

def pinjam(id_peminjam,Gadget,riwayat_pinjam):
    ID = input("Masukkan ID: ")
    def cek():
        for i, element in enumerate(Gadget):
            if element[0] == ID:
                tanggal = strftime("%d/%m/%Y")
                jumlah = int(input("Masukkan jumlah: "))
                if jumlah > 0:
                    k = int(element[3]) - jumlah
                    if k >= 0:
                        element[3] = str(k)
                        print(f"Tanggal permintaan: {tanggal}")
                        print(f'Item {Gadget[i][1]} (x{jumlah}) berhasil dipinjam!')
                        riwayat_pinjam.append([str(len(riwayat_pinjam)),str(id_peminjam) ,str(ID), str(tanggal), str(jumlah), False])
                        return True
                    else:
                        print("Jumlah peminjaman melebihi ketersediaan")
                        return False
                else:
                    print("Masukan jumlah salah")
                    return False
        print("ID tidak valid")
        return False
    def validasi():
        for i, element in enumerate(riwayat_pinjam):
            if element[2] == ID and element[1] == id_peminjam and str(element[5]) == "False" :
                print("Gadget sudah pernah dipinjam")
                return False
        return True
    if len(ID) > 1:
        if validasi():
            cek()
    else:
        print("ID tidak valid")
    print()
