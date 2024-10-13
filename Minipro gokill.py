from prettytable import PrettyTable
from datetime import datetime
import sys

# Menyimpan kamar dalam dictionary terpisah berdasarkan lantai
kamar_lantai_2 = {
    "201": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang"},
    "202": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang"},
    "203": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang"},
    "204": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang"},
    "205": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang"},
}

kamar_lantai_3 = {
    "301": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang"},
    "302": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang"},
    "303": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang"},
    "304": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang"},
    "305": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang"},
}

kamar_lantai_4 = {
    "401": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang, makan dan renang"},
    "402": {"tipe": "Single Bed", "fasilitas": "Kamar untuk 1 orang, makan dan renang"},
    "403": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang, makan dan renang"},
    "404": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang, makan dan renang"},
    "405": {"tipe": "Double Bed", "fasilitas": "Kamar untuk 2 orang, makan dan renang"},
}
reservasi = {}
# Fungsi untuk login
def login():
    while True:
        print("=" * 10 + "Selamat Datang Hotel Jatra Balikpapan" + "=" * 10)
        print("1. Admin")
        print("2. Tamu")
        pilihan = input("Silakan Pilih Mode Login : ")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            tamu()
            break
        else:
            print("Mode Login Tidak ada, silakan coba kembali!")
            return login()

# Fungsi untuk menambah kamar
def tambah_kamar():
    daftar_kamar()
    lantai = input("Masukkan lantai kamar (2, 3, atau 4): ")
    
    if lantai == '2':
        if nomor_kamar not in kamar_lantai_2:
            nomor_kamar = input("Masukkan nomor kamar: ")
            tipe_kamar = input("Masukkan tipe kamar: ")
            fasilitas = input("Masukkan fasilitas: ")
            kamar_lantai_2[nomor_kamar] = {'tipe': tipe_kamar, 'fasilitas': fasilitas}
            print(f"Kamar {nomor_kamar} berhasil ditambahkan di lantai {lantai}.")
        else:
            print(f"Kamar {nomor_kamar} sudah ada di lantai {lantai}.")
    
    elif lantai == '3':
        if nomor_kamar not in kamar_lantai_3:
            nomor_kamar = input("Masukkan nomor kamar: ")
            tipe_kamar = input("Masukkan tipe kamar: ")
            fasilitas = input("Masukkan fasilitas: ")
            kamar_lantai_3[nomor_kamar] = {'tipe': tipe_kamar, 'fasilitas': fasilitas}
            print(f"Kamar {nomor_kamar} berhasil ditambahkan di lantai {lantai}.")
        else:
            print(f"Kamar {nomor_kamar} sudah ada di lantai {lantai}.")
    
    elif lantai == '4':
        if nomor_kamar not in kamar_lantai_4:
            nomor_kamar = input("Masukkan nomor kamar: ")
            tipe_kamar = input("Masukkan tipe kamar: ")
            fasilitas = input("Masukkan fasilitas: ")
            kamar_lantai_4[nomor_kamar] = {'tipe': tipe_kamar, 'fasilitas': fasilitas}
            print(f"Kamar {nomor_kamar} berhasil ditambahkan di lantai {lantai}.")
        else:
            print(f"Kamar {nomor_kamar} sudah ada di lantai {lantai}.")
    
    else:
        print("Lantai tidak valid!")

# Fungsi untuk menghapus kamar
def hapus_kamar():
    nomor_kamar = input("Masukkan nomor kamar yang ingin di hapus: ")
    
    # cari setiap lantai
    for lantai in [kamar_lantai_2, kamar_lantai_3, kamar_lantai_4]:
        if nomor_kamar in lantai:
            del lantai[nomor_kamar]
        print(f"kamar{nomor_kamar}berhasil dihapus daftar kamar")
        return
    else:
        print("Nomor kamar tidak dapat di temukan")

# Fungsi untuk melihat daftar kamar 
def daftar_kamar():
    # Tabel untuk semua lantai
    table = PrettyTable()
    table.field_names = ["Nomor Kamar", "Tipe Kamar", "Fasilitas", "status"]
    
    for lantai in [kamar_lantai_2, kamar_lantai_3, kamar_lantai_4]:
        for nomor, info in lantai.items():
            # Cek apakah kamar sudah dipesan
            status = "Tersedia"
            if nomor in reservasi:
                status = "Dipesan"
            table.add_row([nomor, info['tipe'], info['fasilitas'], status])
    print("\n=== Daftar Kamar Hotel Jatra Balikpapan ===")
    print(table)

# Fungsi untuk menambah reservasi
def buat_reservasi():
    nama_tamu = input("Masukkan nama tamu: ")
    nomor_kamar = input("Masukkan nomor kamar yang ingin dipesan (201-210, 301-310, atau 401-410): ")
    
    if (nomor_kamar in kamar_lantai_2 or 
        nomor_kamar in kamar_lantai_3 or 
        nomor_kamar in kamar_lantai_4):

        if nomor_kamar not in reservasi:
            tanggal_reservasi = input("Masukkan tanggal reservasi (YYYY-MM-DD): ")
            waktu_reservasi = input("Masukkan waktu reservasi (HH:MM): ")

            datetime.strptime(tanggal_reservasi, "%Y-%m-%d")
            datetime.strptime(waktu_reservasi, "%H:%M")
            reservasi[nomor_kamar] = {
                'nama_tamu': nama_tamu,
                'tanggal': tanggal_reservasi,
                'waktu': waktu_reservasi
                }
                
            print(f"Reservasi untuk {nama_tamu} di kamar {nomor_kamar} pada {tanggal_reservasi} pukul {waktu_reservasi} berhasil dibuat!")
        else:
            print(f"Kamar {nomor_kamar} sudah dipesan!")
    else:
        print("Nomor kamar tidak valid!")

# Fungsi untuk melihat daftar reservasi 
def daftar_reservasi():
    if not reservasi:
        print("Tidak ada reservasi yang terdaftar.")
        return
    
    table = PrettyTable()
    table.field_names = ["Nomor Kamar", "Nama Tamu", "Tanggal Reservasi", "Waktu Reservasi", "Status"]
    
    for nomor, info in reservasi.items():
        # Menentukan status kamar
        status = "Dipesan"
        table.add_row([nomor, info['nama_tamu'], info['tanggal'], info['waktu'], status])
    
    print("\n=== Daftar Reservasi Hotel Jatra Balikpapan ===")
    print(table)

#update kamar
def update_kamar():
    daftar_kamar()
    try:
        index = int(input("Pilih nomor kamar yang ingin diupdate : "))
        
        # Cek apakah nomor kamar valid di semua lantai
        for lantai in [kamar_lantai_2, kamar_lantai_3, kamar_lantai_4]:
            if str(index) in lantai:
                nomor_baru = input("Masukkan nomor kamar baru: ")
                tipe_baru = input("Masukkan tipe kamar baru: ")
                fasilitas_baru = input("Masukkan fasilitas baru: ")
                
                # Memperbarui informasi kamar
                lantai[nomor_baru] = {
                    'tipe': tipe_baru,
                    'fasilitas': fasilitas_baru
                }
                print(f"Kamar {index} berhasil diupdate menjadi {nomor_baru}!")
                return
        print("Nomor kamar tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka!")

# Login admin
def admin():
    while True:
            print("\n=== Menu Admin ===")
            print("1. Daftar Kamar")
            print("2. Tambah Kamar") 
            print("3. Update kamar") 
            print("4. Hapus kamar")
            print("5. Daftar Reservasi")
            print("6. Keluar")
            
            opsi = input("Pilih opsi (1-5): ")
            
            if opsi == '1':
                daftar_kamar()
            elif opsi == '2':
                tambah_kamar() 
            elif opsi == '3':
                update_kamar()
            elif opsi == '4':
                hapus_kamar()
            elif opsi == '5':
                daftar_reservasi()
            elif opsi == '6':
                mode_login = input ("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Kembali) : ").capitalize()
                if mode_login == "Keluar":
                    print("Terimakasih telah berkunjung di Hotel Jatra Balikpapan")
                    sys.exit()
                elif mode_login == "Kembali":
                    admin()
                    break  
            else:
                print("Pilihan tidak valid!")

# Login tamu
def tamu():
        while True:
            print("\n=== Menu Tamu ===")
            print("1. Daftar Kamar")
            print("2. Buat Reservasi")
            print("3. Daftar Reservasi")
            print("4. Keluar")
            
            opsi = input("Pilih opsi (1-4): ")
            
            if opsi == '1':
                daftar_kamar()
            elif opsi == '2':
                buat_reservasi()
            elif opsi == '3':
                daftar_reservasi()
            elif opsi == '4':
                mode_login = input ("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Kembali) : ").capitalize()
                if mode_login == "Keluar":
                    print("Terimakasih telah berkunjung di Hotel Jatra Balikpapan")
                    sys.exit()
                elif mode_login == "Kembali":
                    login()
                    break  
                break
            else:
                print("Pilihan tidak valid!")

if __name__ == "__main__":
    login()