
class Mahasiswa:

    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan_diri
    def perkenalan_diri(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}, IPK: {self.ipk}, Universitas: {Mahasiswa.universitas}"

    # Method update_ipk
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK diperbarui menjadi {self.ipk}"

    # Method predikat_kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# Instansiasi object
mhs1 = Mahasiswa("Andi", "TI001", "Informatika", 3.6)
mhs2 = Mahasiswa("Budi", "TI002", "Informatika", 3.1)
mhs3 = Mahasiswa("Citra", "TI003", "Sistem Informasi", 2.4)

# Demonstrasi method
print(mhs1.perkenalan_diri())
print(mhs1.predikat_kelulusan())

print(mhs2.perkenalan_diri())
print(mhs2.predikat_kelulusan())

print(mhs3.perkenalan_diri())
print(mhs3.update_ipk(2.8))
print(mhs3.predikat_kelulusan())
