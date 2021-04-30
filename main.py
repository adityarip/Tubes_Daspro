from F01_register import register
from F02_login import login
from F03_4_carigadget import carirarity,caritahun
from F05_06_tambahhapusitem import tambahitem,hapusitem
from F07_ubahjumlah import ubahjumlah
from F08_meminjamgadget import pinjam
from F09_kembalikangadget import kembalikan
from F10_mintaconsumable import minta
from F11_12_13_riwayat import lihatPinjam,lihatAmbil,lihatKembali
from F16_help import helpAdmin,helpUser
import F14_15_loadsave as tb
import os,argparse,sys


def menuAdmin():    #Function pilihan menu untuk admin
    inp = input("Pilihan: ")
    if inp == "register":
        register(User)
    elif inp == "carirarity":
        carirarity(Gadget)
    elif inp == "caritahun":
        caritahun(Gadget)
    elif inp == "tambah":
        tambahitem(Gadget,Consumable)
    elif inp == "hapus":
        hapusitem(Gadget,Consumable)
    elif inp == "ubahjumlah":
        ubahjumlah(Gadget,Consumable)
    elif inp == "riwayatpinjam":
        lihatPinjam(Riwayat_pinjam,User,Gadget)
    elif inp == "riwayatkembali":
        lihatKembali(Riwayat_kembali,Riwayat_pinjam,User,Gadget)
    elif inp == "riwayatambil":
        lihatAmbil(Riwayat_ambil,User,Consumable)
    elif inp == "save":
        save_db()
    elif inp == "help":
        helpAdmin()
    elif inp == "exit":     #admin memilih untuk keluar program
        saving = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if saving == "Y" or saving == "y":
            save_db()
            sys.exit()
        elif saving == "N" or saving == "n":
            sys.exit()
        else:
            print("Masukan tidak valid")
    else:
        print("Masukan tidak valid\n")

def menuUser():     #Function pilihan menu untuk user
    inp = input("Pilihan: ")
    if inp == "carirarity":
        carirarity(Gadget)
    elif inp == "caritahun":
        caritahun(Gadget)
    elif inp == "pinjam":
        pinjam(isloggedIn,Gadget,Riwayat_pinjam)
    elif inp == "kembalikan":
        kembalikan(isloggedIn,Gadget,Riwayat_pinjam,Riwayat_kembali)
    elif inp == "minta":
        minta(isloggedIn,Consumable,Riwayat_ambil)
    elif inp == "save":
        save_db()
    elif inp == "help":
        helpUser()
    elif inp == "exit":     #user memilih untuk keluar program
        saving = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if saving == "Y" or saving == "y":
            save_db()
            sys.exit()
        elif saving == "N" or saving == "n":
            sys.exit()
        else:
            print("Masukan tidak valid")
    else:
        print("Masukan tidak valid\n")

def load_db(folder: str):
    """
    load_db: Membaca data enam csv dalam folder untuk digunakan program utama.

    Input:  <folder>    str     Nama folder
    Output: <status>    bool    True apabila program berhasil jalan,
                                False apabila tidak (folder tidak ada dsb.)
    """

    # ambil variabel tabel
    global User, Gadget, Consumable, \
           Riwayat_pinjam, Riwayat_kembali, Riwayat_ambil

    # cek folder ada
    if not os.path.exists(folder):
        print("Folder \'%s\' tidak dapat ditemukan" % folder)
        return False

    # CSV ke variabel tabel
    try:
        User = tb.loadcsv(_filenames["user"] % folder)
        Gadget = tb.loadcsv(_filenames["gadget"] % folder)
        Consumable = tb.loadcsv(_filenames["consumable"] % folder)
        Riwayat_pinjam = tb.loadcsv(_filenames["gadget_borrow_history"] % folder)
        Riwayat_kembali = tb.loadcsv(_filenames["gadget_return_history"] % folder)
        Riwayat_ambil = tb.loadcsv(_filenames["consumable_history"] % folder)
    except OSError as e:
        if isinstance(e, FileNotFoundError):
            print("Tidak dapat menemukan file \'%s\'" % e.filename)
        else:
            print("OSError: %s" % e.strerror)
        return False

    # akhir program - proses berhasil
    return True

def prompt(msg: str, *, custom_yes: str = "ya", custom_no: str = "tidak"):
    # ---------------------------------------------------------------
    """
    Meminta prompt ya/tidak/batal kepada user.
    """
    # ---------------------------------------------------------------
    """
    - Digunakan di save_db().
    Input fungsi:
        msg         : str       Pesan pemasukan data
        custom_yes  : str       Optional: Kata pengganti "ya" pada prompt
        custom_no   : str       Optional: Kata pengganti "tidak" pada prompt
    Variabel lokal:
        option      : str       Masukan dari pengguna, antara 'y', 'n', dan 'x'.
    Output:
        ret         : int       1: ya (y), 0: tidak (n), -1: batal (x)
    """
    # ---------------------------------------------------------------

    # ambil input dari user
    option = ""
    while option not in ('y','n','x'):
        print(msg)
        option = input("(Y: %s/N: %s/X: batalkan): " % (custom_yes, custom_no)).lower()

    # proseskan input
    if option == 'y':
        ret = 1
    elif option == 'n':
        ret = 0
    else:
        ret = -1
    return ret

def save_db():
    # ---------------------------------------------------------------
    """
    Menyimpan data yang telah diubah oleh program ke dalam suatu folder.
    Meminta opsi penyimpanan dan folder penyimpanan kepada user.
    """
    # ---------------------------------------------------------------
    """
    Input masukan:
        option          : int       Opsi penyimpanan file, memanggil prompt().
                                    1: Ke folder lama, 0: Ke folder baru, -1: Batalkan
        folder          : str       Lokasi penyimpanan, default ke db_folder dari program utama jika option = 1
    Variabel lokal:
        folder_files    : [str]     Isi folder penyimpanan (diambil dari variabel folder).
        fo              : object    Objek sementara untuk pembuatan file csv yang belum ada.
    """
    # ---------------------------------------------------------------

    # input opsi penyimpanan (save, save as, cancel)
    option = prompt("Simpan ke folder '%s'?" % db_folder, custom_no="lain")

    if option == -1:
        # 'X' dipilih
        print()
        return

    # basis variabel
    folder = ""            # nama folder penyimpanan
    folder_files = []      # isi folder penyimpanan, digunakan di os.walk()

    if option == 1:
        # 'Y' dipilih
        folder = db_folder
    else:
        # 'N' dipilih
        while folder.strip() == "":
            folder = input("Nama folder penyimpanan: ")

    # cek apakah folder sudah ada
    if not os.path.exists(folder):
        os.mkdir(folder)

    # cek isi folder dan keberadaan file
    for root, dirs, files in os.walk(folder):
        folder_files = files

    for file in _filenames.values():
        if file[3:] not in folder_files:
            fo = open(file % folder, mode='x')
            fo.close()

    # lakukan save
    tb.savecsv(_filenames["user"] % folder, User)
    tb.savecsv(_filenames["gadget"] % folder, Gadget)
    tb.savecsv(_filenames["consumable"] % folder, Consumable)
    tb.savecsv(_filenames["gadget_borrow_history"] % folder, Riwayat_pinjam)
    tb.savecsv(_filenames["gadget_return_history"] % folder, Riwayat_kembali)
    tb.savecsv(_filenames["consumable_history"] % folder, Riwayat_ambil)
    print()
    return

def main():
    global db_folder
    # argparse (baca masukan folder)
    parser = argparse.ArgumentParser(description="Kantong Ajaib.")
    parser.add_argument("folder", help="Nama folder lokasi data")
    args = parser.parse_args()

    # baca file (jika fungsi load_db berhasil berjalan)
    if load_db(args.folder):
        db_folder = args.folder
    else:
        return

    # panggil prosedur baca panggilan di sini

# =========================================================
# BASE VARIABLES LOAD

db_folder = ""

User, Gadget, Consumable = [], [], []
Riwayat_pinjam, Riwayat_kembali, Riwayat_ambil = [], [], []

_filenames = {
    "user": "%s/user.csv",
    "gadget": "%s/gadget.csv",
    "consumable": "%s/consumable.csv",
    "gadget_borrow_history": "%s/gadget_borrow_history.csv",
    "gadget_return_history": "%s/gadget_return_history.csv",
    "consumable_history": "%s/consumable_history.csv"
}

if __name__ == "__main__":
    main()

#Algoritma utama
isloggedIn = login(User)
while not(isloggedIn):
    isloggedIn = login(User)


while isloggedIn[0] == "A": 
    menuAdmin()     

while isloggedIn[0] == "U": 
    menuUser()
