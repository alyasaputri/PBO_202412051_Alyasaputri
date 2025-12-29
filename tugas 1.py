from datetime import date

# =========================
# Class Buku
# =========================
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul              # public
        self.penulis = penulis          # public
        self.kode_buku = kode_buku      # public
        self._stok = stok               # protected
        self.__lokasi_rak = lokasi_rak  # private

    # getter & setter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    # method stok
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
            return True
        return False


# =========================
# Class Peminjaman
# =========================
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = None
        self.status = "Dipinjam"

    def info_peminjaman(self):
        return f"Kode Buku: {self.kode_buku}, Status: {self.status}"


# =========================
# Class Anggota
# =========================
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam):
        self.id_anggota = id_anggota     # public
        self.nama = nama                 # public
        self._maks_pinjam = maks_pinjam  # protected
        self.__status_aktif = True       # private
        self.daftar_peminjaman = []      # aggregation

    # getter & setter status
    def get_status(self):
        return self.__status_aktif

    def set_status(self, status):
        self.__status_aktif = status

    # pinjam buku
    def pinjam_buku(self, buku):
        if not self.__status_aktif:
            print("Anggota tidak aktif")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Batas peminjaman tercapai")
            return

        if buku.kurangi_stok(1):
            peminjaman = Peminjaman(buku.kode_buku, date.today())
            self.daftar_peminjaman.append(peminjaman)
            print(f"{self.nama} berhasil meminjam buku {buku.judul}")
        else:
            print("Stok buku habis")

    # kembalikan buku
    def kembalikan_buku(self, buku):
        for p in self.daftar_peminjaman:
            if p.kode_buku == buku.kode_buku and p.status == "Dipinjam":
                p.status = "Dikembalikan"
                p.tanggal_kembali = date.today()
                buku.tambah_stok(1)
                print(f"{self.nama} mengembalikan buku {buku.judul}")
                return


# =========================
# DEMONSTRASI PROGRAM
# =========================

# Instansiasi Buku
buku1 = Buku("Python Dasar", "Andi", "B001", 3, "Rak A1")
buku2 = Buku("Struktur Data", "Budi", "B002", 2, "Rak B2")
buku3 = Buku("OOP Python", "Citra", "B003", 1, "Rak C3")

# Instansiasi Anggota
anggota1 = Anggota("A001", "Rina", 2)
anggota2 = Anggota("A002", "Doni", 1)

# Proses Peminjaman
anggota1.pinjam_buku(buku2)
anggota2.pinjam_buku(buku1)

# Pengembalian Buku
anggota1.kembalikan_buku(buku1)

# =========================
# OUTPUT PRINT
# =========================
print("\n=== Informasi Buku ===")
for buku in [buku1, buku2, buku3]:
    print(buku.judul, "- Stok:", buku._stok)

print("\n=== Informasi Anggota ===")
print(anggota1.id_anggota, anggota1.nama)
print(anggota2.id_anggota, anggota2.nama)

print("\n=== Daftar Peminjaman ===")
for p in anggota1.daftar_peminjaman:
    print("Anggota 1 ->", p.info_peminjaman())

for p in anggota2.daftar_peminjaman:
    print("Anggota 2 ->", p.info_peminjaman())
