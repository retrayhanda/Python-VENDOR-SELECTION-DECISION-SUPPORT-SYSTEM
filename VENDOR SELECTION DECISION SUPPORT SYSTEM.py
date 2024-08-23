def print_cover_page():
    width = 89
    def print_line():
        print('+' + '-' * (width - 2) + '+')
    
    def print_centered(text):
        print('|' + text.center(width - 2) + '|')
    
    print_line()
    print_centered('')
    print_centered('')
    print_centered('SISTEM PENUNJANG KEPUTUSAN PEMILIHAN VENDOR')
    print_centered('DALAM SUPPLY CHAIN MENGGUNAKAN METODE WEIGHTED PRODUCT')
    print_centered('')
    print_centered('Oleh:')
    print_centered('Rahmad Haret Rayhanda')
    print_line()

def welcome_message(title):
    bintang = '=' * len(title)
    print(bintang.center(89))
    print(title.center(89))
    print(bintang.center(89))

def main():
    print_cover_page()
    print('\n' * 2)
    welcome_message('PROGRAM SISTEM PENUNJANG KEPUTUSAN PEMILIHAN VENDOR DALAM SUPPLY CHAIN MENGGUNAKAN METODE WEIGHTED PRODUCT')

main()


class Login :  #Menu sign up dan log in
    def __init__(self):
        self.list_username = []
        self.list_password = []

    def sign_up(self) :
        username = input("Masukkan username baru : ").title()  #huruf awal kapital dan huruf selanjutnya kecil
        password = input("Masukkan password baru : ")
        self.list_username.append(username)
        self.list_password.append(password)

    def login(self) :
        self.username = input("Masukkan username : ").title() #huruf awal kapital dan huruf selanjutnya kecil
        self.password = input("Masukkan password : ")
        
    def cek_login(self):
        if self.username in self.list_username and self.password in self.list_password:
            return True
        else:
            return False
login_signup = Login()

while True : #Eksekusi program
    print("\nMenu :\n1. Sign up\n2. Login \n3. keluar")
    opsi = input("Masukkan pilihan (1-3) : ")
    if opsi == '1':
        login_signup.sign_up()
        print("Akun berhasil dibuat")
    elif opsi == '2':
        login_signup.login()
        if login_signup.cek_login():
            print("Login berhasil")
            break
        else:
            print("username atau password tidak valid, pastikan akun anda telah terdaftar")
    elif opsi == "3":
        print("Terima Kasih")
        exit()
    else :
        print ('Pilihan tidak valid')

class Bobot:
    def __init__(self, kode, judul, nilai):
        self.kode = kode
        self.judul = judul
        self.nilai = nilai
    def __str__(self):
        return f"{self.kode}, Judul kriteria: {self.judul}, Nilai : {self.nilai}"
class Kriteria:
    def __init__(self):
        self.bobot = []   
    def tambah_kriteria(self):
        while True:
            try:
                kode = input("\nMasukkan Kode kriteria penilaian : ").upper()
                judul = input("Kriteria penilaian : ").title()
                nilai = int(input("Masukkan bobot nilai kriteria penilaian : "))
                self.bobot.append(Bobot(kode, judul, nilai))
                print(f"Kriteria penilaian {kode} ditambahkan")
                break
            except ValueError:
                print("Input Anda tidak valid")

    def hapus_kriteria(self):
        kode = input("Masukkan kode kriteria penilaian yang ingin dihapus : ").upper()
        for skor in self.bobot:
            if skor.kode == kode:
                self.bobot.remove(skor)
                print(f"Kriteria penilaian {kode} dihapus")
                return
        print("Kriteria tidak ditemukan")

    def tampilkan_kriteria(self):
        print("\nData kriteria penilaian : ")
        print("="*64)
        topline = ["Kode", "Kriteria Penilaian", "Bobot Nilai"]
        kolom = "|{:^15}|{:^30}|{:^15}|" 
        print(kolom.format(*topline)) 
        print("="*64)
        for kriteria in self.bobot: 
            print(kolom.format(kriteria.kode, kriteria.judul, kriteria.nilai))
            print("-"*64)

    def normalisasi_bobot(self):
        total_bobot = sum(bobot.nilai for bobot in self.bobot)
        normalisasi = [bobot.nilai / total_bobot for bobot in self.bobot]
        print("="*48)
        topline = ["Kode", "Hasil Normalisasi"]
        kolom = "|{:^20}|{:^25}|"
        print(kolom.format(*topline))
        print("="*48)
        for i,  nilai in enumerate(normalisasi):
            print(kolom.format(f"W{i + 1}", f"{nilai:.3f}"))
            print("-"*48)
        return normalisasi

#Mendefinisikan kelas vendor
class Vendor:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.skor = {}
        self.vektor_s = 0
        self.vektor_v = 0
            
    def __str__(self):
        return f"{self.nama}, {self.alamat} "

#mendefinisikan daftar vendor
class DaftarVendor:
    def __init__(self):
        self.data_vendor = []

    #menambahkan vendor ke array daftar vendor
    def input_vendor(self):
        while True:
            try:
                jumlah_vendor = int(input("\nMasukkan jumlah pilihan vendor: "))
                for i in range(jumlah_vendor):
                    print(f"\nMasukkan data vendor ke-{i+1}: ")
                    nama = input("Nama vendor: ").upper()
                    alamat = input("Alamat : ").title()
                    vendor_baru = Vendor (nama, alamat)
                    self.data_vendor.append(vendor_baru)
                    print(f"{nama} telah ditambahkan ke daftar vendor.")
                break
            except ValueError:
                print("Input tidak valid, silakan ulangi")

    #menghapus vendor dari array daftar vendor
    def hapus_vendor(self):
        nama = input("Masukkan nama vendor yang ingin dihapus: ").upper()
        for vendor in self.data_vendor:
            if vendor.nama == nama:
                self.data_vendor.remove(vendor)
                print(f"{nama} telah dihapus dari daftar vendor.")
                return
        print("Vendor tidak ditemukan pada daftar vendor.")
            
    #membuat tampilan daftar vendor dalam bentuk tabel
    def tampilkan_daftar_vendor(self):
        print("=" * 43)
        headers = ["Nama", "alamat"]
        kolom = "|{:^20}|{:^20}|"
        print(kolom.format(*headers))
        print("=" * 43)
        for vendor in self.data_vendor:
            print(kolom.format(vendor.nama, vendor.alamat))
            print("-" * 43)

    #menambahkan skor untuk tiap-tiap vendor
    def input_skor(self, kriteria):
        for vendor in self.data_vendor:
            print(f"\nMasukkan skor untuk {vendor.nama}: ")
            for bobot in kriteria.bobot:
                while True:
                    try:
                        skor = float(input(f"Nilai untuk {bobot.judul} ({bobot.kode}): "))
                        vendor.skor[bobot.kode] = skor
                        break
                    except ValueError:
                        print("Input tidak valid, silakan ulangi") 

    #menampilkan skor tiap-tiap vendor
    def tampilkan_skor(self, kriteria):
        print("\n Skor untuk setiap vendor.")
        print("="*97)
        headers = ["Nama Vendor"] + [bobot.kode for bobot in kriteria.bobot]
        kolom = "|{:^15}" * len(headers) + "|"
        print(kolom.format(*headers))
        print("=" * 97)
        for vendor in self.data_vendor:
            skor = [vendor.skor.get(bobot.kode, 0) for bobot in kriteria.bobot]
            print(kolom.format(vendor.nama, *skor ))
            print("-" * 97)

    def ubah_skor(self, kriteria):
        nama_vendor = input("Masukkan nama vendor yang ingin diubah skornya: ").upper()
        for vendor in self.data_vendor:
            if vendor.nama == nama_vendor:
                for bobot in kriteria.bobot:
                    while True:
                        try:
                            skor = float(input(f"Ubah nilai untuk {bobot.judul} ({bobot.kode}): "))
                            vendor.skor[bobot.kode] = skor
                            break
                        except ValueError:
                            print("Input tidak valid, silakan ulangi")
                print(f"Skor untuk {vendor.nama} telah diubah.")
                return
        print("Vendor tidak ditemukan.")

    #menghitung nilai vektor s tiap-tiap vendor
    def hitung_vektor_s(self, kriteria):
        normalisasi_bobot = kriteria.normalisasi_bobot()
        for vendor in self.data_vendor:
            vektor_s = 1
            for i, bobot in enumerate(kriteria.bobot):
                nilai = vendor.skor.get(bobot.kode, 0)
                vektor_s = nilai ** normalisasi_bobot[i]
            vendor.vektor_s = vektor_s

        # Tampilkan hasil perhitungan vektor S
        print("\nHasil Perhitungan Vektor S:")
        print("Vektor S = (Skor vendor i)^normalisasi bobot")
        print("="*63)
        kolom = "|{:^30}|{:^30}|"
        headers = ["Nama Vendor", "Vektor S"]
        print(kolom.format(*headers))
        print("="*63)
        for vendor in self.data_vendor:
            print(kolom.format(vendor.nama, f"{vendor.vektor_s:.3f}"))
            print("-"*63)

    #menghitung nilai vektor v tiap-tiap vendor
    def hitung_vektor_v(self):
        total_vektor_s = sum(vendor.vektor_s for vendor in self.data_vendor)
        if total_vektor_s == 0:
            print("Total vektor S adalah 0, tidak dapat menghitung vektor V.")
            return

        for vendor in self.data_vendor:
            vendor.vektor_v = vendor.vektor_s / total_vektor_s

        print("\nHasil Perhitungan Vektor V:")
        print("Vektor S = (Vektor S Vendor i)/total Vektor S")
        print("=" * 63)
        kolom = "|{:^30}|{:^30}|"
        headers = ["Nama Vendor", "Vektor V"]
        print(kolom.format(*headers))
        print("=" * 63)
        for vendor in self.data_vendor:
            print(kolom.format(vendor.nama, f"{vendor.vektor_v:.3f}"))
            print("-" * 63)

    #mengurutkan perolehan vektor v tiap-tiap vendor, diambil pilihan tiga teratas
    def peringkat_vendor(self):
        sorted_vendor = sorted(self.data_vendor, key=lambda rank: rank.vektor_v, reverse=True)
        print("\nPeringkat Vendor Berdasarkan Vektor V:")
        print("=" * 74)
        kolom = "|{:^30}|{:^20}|{:^20}|"
        headers = ["Nama Vendor", "Vektor V", "Keterangan"]
        print(kolom.format(*headers))
        print("=" * 74)
        for i, vendor in enumerate(sorted_vendor):
            status = "Lulus" if i < 3 else "Tidak Lulus"
            print(kolom.format(vendor.nama, f"{vendor.vektor_v:.3f}", status))
            print("-" * 74)    

#Fungsi utama program
def main():
    kriteria = Kriteria()
    kriteria.bobot.append(Bobot("C1", "Pengalaman Project", 4))
    kriteria.bobot.append(Bobot("C2", "Harga Penawaran", 4))
    kriteria.bobot.append(Bobot("C3", "Waktu Pengerjaan", 3))
    kriteria.bobot.append(Bobot("C4", "Garansi Purna Jual", 3))
    kriteria.bobot.append(Bobot("C5", "Kelengkapan Dokumentasi", 5))

    while True:
        print("""\nMenu : 
1. Tambah kriteria penilaian
2. Hapus kriteria penilaian
3. Tampilkan daftar kriteria penilaian
4. Normalisasi nilai bobot preferensi
5. Lanjutkan program""")
        opsi = input("Pilih opsi (1-5) : ")

        if opsi == '1':
            kriteria.tambah_kriteria()
        elif opsi == '2':
            kriteria.hapus_kriteria()
        elif opsi == '3':
            kriteria.tampilkan_kriteria()
        elif opsi == '4':
            kriteria.normalisasi_bobot()
        elif opsi == '5':
            break
        else:
            print("Opsi tidak valid. silahkan pilih opsi yang benar")
        
    vendor = DaftarVendor()
    vendor.data_vendor.append(Vendor("PT BCH", "Jakarta"))
    vendor.data_vendor.append(Vendor("PT TLK", "Jakarta"))
    vendor.data_vendor.append(Vendor("PT ISP", "Jakarta"))
    vendor.data_vendor.append(Vendor("PT MII", "Jakarta"))
    vendor.data_vendor.append(Vendor("PT HDC", "Jakarta"))
    vendor.data_vendor.append(Vendor("PT BCA", "Jakarta"))
    vendor.data_vendor.append(Vendor("PT DIKA", "Jakarta"))

    while True:
        print("""\nMenu : 
1. Tambahkan vendor
2. Hapus vendor
3. Tampilkan daftar vendor
4. Input skor vendor
5. Ubah skor vendor
6. Tampilkan skor vendor
7. Hitung vektor S
8. Hitung vektor V
9. Hasil Seleksi Vendor
10. Keluar""")
        opsi = input("Pilih opsi (1-9) : ")

        if opsi == '1':
            vendor.input_vendor()
        elif opsi == '2':
            vendor.hapus_vendor()
        elif opsi == '3':
            vendor.tampilkan_daftar_vendor()
        elif opsi == '4':
            vendor.input_skor(kriteria)
        elif opsi == '5':
            vendor.ubah_skor(kriteria)
        elif opsi == '6':
            vendor.tampilkan_skor(kriteria)
        elif opsi == '7':
            vendor.hitung_vektor_s(kriteria)
        elif opsi == '8':
            vendor.hitung_vektor_v()
        elif opsi == '9':
            print('\nPerusahaan akan memilih 3 vendor dengan nilai vektor v teratas')
            vendor.peringkat_vendor()
        elif opsi == '10':
            print("Terima Kasih")
            break
        else:
            print("Opsi tidak valid. Silakan pilih opsi yang benar.")
        
if __name__ == "__main__":
    main()