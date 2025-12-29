class Penulis:
    def __init__(self, nama):
        self.nama = nama


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis  # Composition (buku memiliki penulis)

    def info(self):
        return f"Buku '{self.judul}' ditulis oleh {self.penulis.nama}"


# Demonstrasi akses data penulis melalui objek buku
p = Penulis("Tere Liye")
b = Buku("Hujan", p)

print(b.info())               # akses via method info()
print("Nama Penulis:", b.penulis.nama)   # akses langsung atribut penulis
