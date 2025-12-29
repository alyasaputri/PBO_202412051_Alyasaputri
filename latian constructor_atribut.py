
class Kendaraan:
    bahan_bakar = "Bensin"

    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"Kendaraan {self.merk}, warna {self.warna}, tahun {self.tahun}"

kendaraan1 = Kendaraan("Toyota", "Hitam", 2022)
kendaraan2 = Kendaraan("Honda", "Putih", 2021)

# Akses instance attribute
print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())

# Akses class attribute
print(f"Bahan bakar kendaraan: {Kendaraan.bahan_bakar}")
