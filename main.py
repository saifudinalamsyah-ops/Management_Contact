"Program Manajemen Kontak"

def melihat_kontak():
    # Melihat Semua Kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}.{item["nama"]}({item["phone"]})({item["email"]})')
    else:
        print("KONTAK TIDAK ADA!")
        return 1

def menambah_kontak():
    # Menambahkan Kontak Baru
    nama = input("Masukkan Nama Kontak Yang Baru: ")
    phone = input("Masukkan Nomor Ponsel Yang Baru: ")
    email = input("Masukkan Email Yang Baru: ")
    kontak_baru = {'nama': nama, 'phone': phone, 'email': email}
    kontak.append(kontak_baru)
    print("KONTAK BERHASIL DITAMBAH!")

def menghapus_kontak():
    # Menghapus Kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukkan Nomor Kontak Yang Akan Dihapus: "))
        del kontak[i_hapus - 1]
        print("KONTAK BERHASIL DIHAPUS")

kontak1 = {'nama': "Arif", 'phone': '081234565789', 'email': 'arif@python.com'}
kontak2 = {'nama': "Abdul", 'phone': '082345657891', 'email': 'abdul@python.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3, atau 4): ")

    if pilihan == '1':
        melihat_kontak()

    elif pilihan == '2':
        menambah_kontak()

    elif pilihan == '3':
        menghapus_kontak()

        i_hapus = int(input("Masukkan Nomor Kontak Yang Akan Dihapus: "))
        del kontak[i_hapus - 1]
        print("KONTAK BERHASIL DIHAPUS")
    elif pilihan == '4':
        # Keluar dari Kontak
        break
    else:
        print("ANDA MEMASUKKAN PILIHAN YANG SALAH!")

