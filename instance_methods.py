# Class ManajerInventori

class ManajerInventori:
    def __init__(self):
        # Menyimpan inventori dalam bentuk dictionary
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah > 0:
            if nama in self.inventori:
                self.inventori[nama] += jumlah
            else:
                self.inventori[nama] = jumlah
            return f"Berhasil menambah {jumlah} {nama}. Total: {self.inventori[nama]}"
        return "Jumlah harus lebih dari 0."

    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"Barang {nama} tidak ditemukan."

        if jumlah <= self.inventori[nama]:
            self.inventori[nama] -= jumlah
            return f"Berhasil menghapus {jumlah} {nama}. Sisa: {self.inventori[nama]}"
        return "Jumlah pengurangan melebihi stok yang ada."

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong."
        return f"Daftar Inventori: {self.inventori}"


# ===========================
# Testing (Poin b & c)
# ===========================

inv = ManajerInventori()

print(inv.tambah_barang("Buku", 10))
print(inv.tambah_barang("Pulpen", 20))
print(inv.hapus_barang("Buku", 5))
print(inv.lihat_inventori())
