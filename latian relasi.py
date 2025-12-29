# relasi aggregation
class Nilai:
    def __init__(self, kode_mk, skor):
        self.kode_mk = kode_mk
        self.skor = skor

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    # tambahan sesuai tugas
    def rata_rata(self):
        if len(self.daftar_nilai) == 0:
            return 0
        total = sum(n.skor for n in self.daftar_nilai)
        return total / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk):
        self.daftar_matakuliah.append(mk)


# relasi composition
class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# fungsi report
def report_program(prodi, semua_mhs):
    print("Program Studi:", prodi.nama)
    print("MataKuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]))
    print("Mahasiswa dan rata-rata nilai:")
    for m in semua_mhs:
        relevant = [n for n in m.daftar_nilai if n.kode_mk in [mk.kode for mk in prodi.daftar_matakuliah]]
        if relevant:
            avg = sum(n.skor for n in relevant) / len(relevant)
            print(m.nim, "-", m.nama + ":", round(avg, 2))
    print("-" * 40)



# =============================================
#              MULAI BAGIAN TUGAS
# =============================================

if __name__ == "__main__":
    # a. Tambahkan 2 Program Studi baru
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")

    # b. Tambah minimal 2 mata kuliah ke tiap prodi
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")
    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    mk3 = MataKuliah("SI201", "Basis Data")
    mk4 = MataKuliah("SI202", "Analisis Sistem")
    prodi_si.tambah_matakuliah(mk3)
    prodi_si.tambah_matakuliah(mk4)

    # c. Buat 3 mahasiswa + beri nilai
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    # nilai untuk prodi TI
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))

    m2.tambah_nilai(Nilai("TI101", 90))

    # nilai untuk prodi SI
    m3.tambah_nilai(Nilai("SI201", 88))
    m3.tambah_nilai(Nilai("SI202", 92))

    # d. Tampilkan daftar mata kuliah
    print("Daftar Mata Kuliah TI:", [mk.kode for mk in prodi_ti.daftar_matakuliah])
    print("Daftar Mata Kuliah SI:", [mk.kode for mk in prodi_si.daftar_matakuliah])

    # e. Tampilkan daftar nilai
    print("\nNilai Mahasiswa:")
    for m in [m1, m2, m3]:
        print(m.nim, m.nama, [(n.kode_mk, n.skor) for n in m.daftar_nilai])

    # f. tampilkan rata-rata (method rata_rata())
    print("\nRata-rata nilai:")
    print(m1.nama, ":", m1.rata_rata())
    print(m2.nama, ":", m2.rata_rata())
    print(m3.nama, ":", m3.rata_rata())

    # g. panggil report_program untuk setiap prodi
    print("\nLaporan Program TI:")
    report_program(prodi_ti, [m1, m2, m3])

    print("Laporan Program SI:")
    report_program(prodi_si, [m1, m2, m3])
