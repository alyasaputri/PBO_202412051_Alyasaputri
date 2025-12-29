# Class Parent
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} - Gaji Pokok: {self.gaji_pokok}"


# Child Class Manager
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"{self.nama} - Manager | Total Gaji: {total}"


# Child Class Programmer
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"{self.nama} - Programmer | Total Gaji: {total}"


# Composition: Departemen memiliki list karyawan
class Departemen:
    def __init__(self, nama_departemen):
        self.nama_departemen = nama_departemen
        self.daftar_karyawan = []   # list of objects

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"--- Daftar Karyawan Departemen {self.nama_departemen} ---")
        for k in self.daftar_karyawan:
            print(k.info_gaji())


# Instansiasi
m1 = Manager("Anya", 5000000, 2000000)
m2 = Manager("Burhan", 5500000, 1500000)

p1 = Programmer("Cici", 4500000, 1000000)
p2 = Programmer("Dinda", 4700000, 1200000)

# Masukkan ke departemen
dep = Departemen("IT")
dep.tambah_karyawan(m1)
dep.tambah_karyawan(m2)
dep.tambah_karyawan(p1)
dep.tambah_karyawan(p2)

# Tampilkan semua karyawan
dep.tampilkan_karyawan()
