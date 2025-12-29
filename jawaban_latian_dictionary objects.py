
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"ID: {self.id_pelanggan}, Nama: {self.nama}, Email: {self.email}"

data_pelanggan = {}

def tambah_pelanggan(pelanggan):
    data_pelanggan[pelanggan.id_pelanggan] = pelanggan

def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]

def cari_pelanggan(id_pelanggan):
    return data_pelanggan.get(id_pelanggan)


# Menambahkan data pelanggan
tambah_pelanggan(Pelanggan("PL001", "Andi", "andi@email.com"))
tambah_pelanggan(Pelanggan("PL002", "Budi", "budi@email.com"))
tambah_pelanggan(Pelanggan("PL003", "Citra", "citra@email.com"))


print("=== Daftar Pelanggan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())


#  pencarian pelanggan
hasil = cari_pelanggan("PL002")
if hasil:
    print("\nPelanggan ditemukan:")
    print(hasil.info())


# Contoh penghapusan pelanggan
hapus_pelanggan("PL001")

print("\n=== Daftar Pelanggan Setelah Penghapusan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())
