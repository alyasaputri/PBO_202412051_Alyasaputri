# Class Kendaraan

class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk          # Instance attribute
        self.warna = warna        # Instance attribute
        self.tahun = tahun        # Instance attribute

    # Method untuk menampilkan informasi kendaraan
    def info_kendaraan(self):
        return f"{self.merk} berwarna {self.warna}, tahun {self.tahun}, menggunakan bahan bakar {Kendaraan.bahan_bakar}"


# Instansiasi 2 object
kend1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
kend2 = Kendaraan("Honda Beat", "Merah", 2022)

# Menampilkan info kendaraan (instance attribute + class attribute)
print(kend1.info_kendaraan())
print(kend2.info_kendaraan())

# Perbedaan: mengakses class attribute langsung dari class
print(f"Bahan bakar (akses via class): {Kendaraan.bahan_bakar}")

# Perbedaan: mengakses instance attribute
print(f"Merk Object 1: {kend1.merk}")
print(f"Merk Object 2: {kend2.merk}")
