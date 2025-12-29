# ============================================
#        NOMOR 2d — 4 PERINTAH TERPISAH
# ============================================

# --- Class Mahasiswa (versi dari nomor 2a–2c) ---
class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

# Tambahan dari nomor 2b
def __len__(self):
    return len(self.nama)

Mahasiswa.__len__ = __len__

# Tambahan dari nomor 2c
def __eq__(self, other):
    return self.nilai == other.nilai

Mahasiswa.__eq__ = __eq__


# --- Membuat objek mahasiswa ---
m1 = Mahasiswa("Pouster", 80)
m2 = Mahasiswa("Ahmad", 90)
m3 = Mahasiswa("Dewi", 90)


# ============================================
#   PERINTAH 1 — Representasi String
# ============================================
print("")
print(m1)
print(m2)
print(m3)

print("\n")
print("Apakah Ahmad > Pouster?", m2 > m1)
print("Apakah Ahmad > Dewi?", m2 > m3)

print("\n")
print("Total nilai m1 + m2 =", m1 + m2)
print("Nilai Ahmad x 2 =", m2 * 2)

print("\n(Sorting) ")
daftar = [m1, m2, m3]
hasil_sort = sorted(daftar, key=lambda x: x.nilai)

for m in hasil_sort:
    print(m)
