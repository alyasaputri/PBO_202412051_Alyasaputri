# Class Dosen

class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Saya Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"
    

# Pembuatan object
dosen1 = Dosen("Dr. Andi Pratama", "123456789")
dosen2 = Dosen("Nur Aisyah, M.Kom", "987654321")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Pemrograman Python"))
print(dosen2.ajar_mata_kuliah("Basis Data"))
