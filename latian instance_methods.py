class ManajerInventori:
    def __init__(self):
        self.inventori = {}

    def tambah_barang(self, nama_barang, jumlah):
        self.inventori[nama_barang] = self.inventori.get(nama_barang, 0) + jumlah
        return f"{nama_barang} ditambah {jumlah}"

    def hapus_barang(self, nama_barang, jumlah):
        if nama_barang in self.inventori and self.inventori[nama_barang] >= jumlah:
            self.inventori[nama_barang] -= jumlah
            return f"{nama_barang} dikurangi {jumlah}"
        return "Stok tidak cukup"

    def lihat_inventori(self):
        return self.inventori


# Testing / Demonstrasi
inv = ManajerInventori()

print(inv.tambah_barang("Buku", 10))
print(inv.tambah_barang("Pulpen", 5))
print(inv.hapus_barang("Buku", 3))
print(inv.lihat_inventori())
