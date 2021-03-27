# Assignment #2 - Basic Python
# Yanuar Adrian Bomantara
# Soal no 1

# Buku Telepon
buku_telepon = []

# Function

def preview():
    for kontak in buku_telepon:
        print("Nama: {}".format(kontak["Nama"]))
        print("Nomor Telepon: {}".format(kontak["Telepon"]))

def add():
    list_kontak = {}
    nama = input("Nama: ")
    telepon = input("Telepon: ")
    list_kontak["Nama"] = nama
    list_kontak["Telepon"] = telepon
    buku_telepon.append(list_kontak)
    print("Kontak berhasil ditambahkan")

def keluar():
    print("Program selesai, sampai jumpa!")

menu = "Selamat datang!"
while menu != "3":
    print("--- Menu ---")
    print(
        "1. Daftar Kontak\n"
        "2. Tambah Kontak\n"
        "3. Keluar\n"
    )
    menu = input("Pilih menu: ")

    if menu == "1":
        preview()
    elif menu == "2":
        add()
    elif menu == "3":
        keluar()
    else:
        print("Menu tidak tersedia")