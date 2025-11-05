"Program Manajemen Kontak"

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
        # Melihat Semua Kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}.{item["nama"]}({item["phone"]})({item["email"]})')
        else:
            print("KONTAK TIDAK ADA!")
    elif pilihan == '2':
        # Menambahkan Kontak Baru
        nama = input("Masukkan Nama Kontak Yang Baru: ")
        phone = input("Masukkan Nomor Ponsel Yang Baru: ")
        email = input("Masukkan Email Yang Baru: ")
        kontak_baru = {'nama': nama,'phone':phone, 'email':email}
        kontak.append(kontak_baru)
        print("KONTAK BERHASIL DITAMBAH!")
    elif pilihan == '3':
        # Menghapus Kontak
        print("\n")
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}.{item["nama"]}({item["phone"]})({item["email"]})')
        else:
            print("KONTAK TIDAK ADA!")
            continue

        i_hapus = int(input("Masukkan Nomor Kontak Yang Akan Dihapus: "))
        del kontak[i_hapus - 1]
        print("KONTAK BERHASIL DIHAPUS")
    elif pilihan == '4':
        # Keluar dari Kontak
        break
    else:
        print("ANDA MEMASUKKAN PILIHAN YANG SALAH!")

