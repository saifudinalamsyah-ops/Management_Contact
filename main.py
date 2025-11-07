"Program Manajemen Kontak"

class kontak:
    def __init__(self):
        self.kontak = []

def melihat_kontak(self):
    # Melihat Semua Kontak
    if kontak:
        for num, item in enumerate(self.kontak, start=1):
            print(f'\n{num}.{item["nama"]}({item["phone"]})({item["email"]})')
    else:
        print("KONTAK TIDAK ADA!")
        return 1

    def menambah_kontak(self):
        # Menambahkan Kontak Baru
        nama = input("Masukkan Nama Kontak Yang Baru: ")
        phone = input("Masukkan Nomor Ponsel Yang Baru: ")
        email = input("Masukkan Email Yang Baru: ")
        kontak_baru = {'nama': nama, 'phone': phone, 'email': email}
        self.kontak.append(kontak_baru)
        print("KONTAK BERHASIL DITAMBAH!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("Masukkan Nomor Kontak Yang Akan Dihapus: "))
            del kontak[i_hapus - 1]
            print("KONTAK BERHASIL DIHAPUS")

kontak_kantor = kontak()
kontak_keluarga = kontak()


while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3, atau 4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

        i_hapus = int(input("Masukkan Nomor Kontak Yang Akan Dihapus: "))
        del kontak[i_hapus - 1]
        print("KONTAK BERHASIL DIHAPUS")
    elif pilihan == '4':
        # Keluar dari Kontak
        break
    else:
        print("ANDA MEMASUKKAN PILIHAN YANG SALAH!")

