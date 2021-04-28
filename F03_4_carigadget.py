def out(i,Gadget):
    #output untuk gadget
    print("ID               : "+ str(Gadget[i][0]))
    print("Nama             : "+ str(Gadget[i][1]))
    print("Deskripsi        : "+ str(Gadget[i][2]))
    print("Jumlah           : "+ str(Gadget[i][3]))
    print("Rarity           : "+ str(Gadget[i][4]))
    print("Tahun ditemukan  : "+ str(Gadget[i][5]))
    print()

def carirarity(Gadget):
    #Mencari rarity gadget sesuai inputan user
    rarity = str(input("Masukkan rarity: "))
    print()
    print("Hasil pencarian:")
    print()
    count = 0
    for i in range (len(Gadget)): 
        if rarity == Gadget[i][4]:  #mengeluarkan data gadget sesuai rarity
            out(i,Gadget)
            count += 1
    if count == 0: #tidak ada gadget yang ditemukan
        print("Tidak ada gadget yang ditemukan")
        print()

def caritahun(Gadget):
    #mencari gadget berdasarkan kategori tahun
    tahun = int(input("Masukkan tahun: "))
    category = str(input("Masukkan kategori: "))
    print()
    print("Hasil pencarian:")
    print()
    count = 0
    if tahun > 0 and tahun <= 9999:
        for i in range (1,len(Gadget)):
            if category == "=":     #jika kategori = maka sama dengan tahun input
                if tahun == int(Gadget[i][5]):
                    out(i,Gadget)
                    count += 1
            elif category == "<":   #jika kategori < maka lebih kecil dari tahun input
                if tahun > int(Gadget[i][5]):
                    out(i,Gadget)
                    count += 1
            elif category == ">":   #jika kategori > maka lebih besar dari tahun input
                if tahun < int(Gadget[i][5]):
                    out(i,Gadget)
                    count += 1
            elif category == "<=":  #jika kategori <= maka lebih kecil atau sama dengan tahun input
                if tahun >= int(Gadget[i][5]):
                    out(i,Gadget)
                    count += 1
            elif category == ">=":  #jika kategori >= maka lebih besar atau sama dengan tahun input
                if tahun <= int(Gadget[i][5]):
                    out(i,Gadget)
                    count += 1
            else: #jika memasukkan selain =,<=,>=,<,>
                print("Input kategori tidak valid.")
                print()
                return
    else: #tahun < 0 atau > 9999
        print("Input tahun tidak valid")
        print()
        return
    if count == 0:
        print("Tidak ada gadget yang ditemukan")
        print()
