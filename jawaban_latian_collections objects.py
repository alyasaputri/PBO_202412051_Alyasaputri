# a. Membuat class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun: {self.tahun}"


# b. Membuat list berisi 5 objek buku
daftar_buku = [
    Buku("Pemrograman Python", "Andi", 2020),
    Buku("Struktur Data", "Budi", 2019),
    Buku("Basis Data", "Andi", 2018),
    Buku("OOP dengan Python", "Citra", 2021),
    Buku("Algoritma", "Budi", 2017)
]


# c. Fungsi untuk mencari buku berdasarkan penulis
def cari_buku_berdasarkan_penulis(daftar_buku, nama_penulis):
    hasil = []
    for buku in daftar_buku:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# d. Menampilkan hasil pencarian
penulis_dicari = "Andi"
hasil_pencarian = cari_buku_berdasarkan_penulis(daftar_buku, penulis_dicari)

print(f"=== Buku dengan penulis {penulis_dicari} ===")
for buku in hasil_pencarian:
    print(buku.info())
