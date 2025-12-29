class ProgramStudi:
    def __init__(self, kode, ketua):
        self.kode = kode
        self._ketua = ketua
        self.__anggaran = 500000000

    def get_ketua(self):
        return self._ketua

    def set_ketua(self, nama_baru):
        if not nama_baru:
            raise ValueError("Nama ketua tidak boleh kosong.")
        self._ketua = nama_baru

    def get_anggaran(self):
        return self.__anggaran

    def set_anggaran(self, nilai):
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = nilai

    def kurangi_anggaran(self, jumlah):
        if jumlah < 0:
            raise ValueError("Jumlah harus positif.")
        if jumlah > self.__anggaran:
            raise ValueError("Anggaran tidak mencukupi.")
        self.__anggaran -= jumlah
        return self.__anggaran


# ================================
#     TUGAS (CLASS MAHASISWA)
# ================================
class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk            # private

    def get_ipk(self):
        return self.__ipk

    def set_ipk(self, nilai):
        self.__ipk = nilai

    def set_semester(self, smt):
        self._semester = smt


# ================================
#       PENGGUNAAN / OUTPUT
# ================================
m1 = Mahasiswa("23001", "Budi", 3, 3.2)
m2 = Mahasiswa("23002", "Siti", 1, 3.7)

# Sebelum diubah
print("Data awal:")
print(m1.nim, m1.nama, m1._semester, m1.get_ipk())
print(m2.nim, m2.nama, m2._semester, m2.get_ipk())

# Mengubah semester dan IPK
m1.set_semester(4)
m1.set_ipk(3.5)

m2.set_semester(2)
m2.set_ipk(3.9)

print("\nData setelah diubah:")
print(m1.nim, m1.nama, m1._semester, m1.get_ipk())
print(m2.nim, m2.nama, m2._semester, m2.get_ipk())
