# relasi aggregation
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []   # agregasi: Nilai dapat berdiri sendiri

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []   # agregasi

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)

    def get_matakuliah(self):
        return self.daftar_matakuliah


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
def report_program(prodi: ProgramStudi, semua_mahasiswa: list):
    print(f"Program Studi: {prodi.nama}")

    mk_prodi = prodi.get_matakuliah()
    mk_kode_list = [mk.kode for mk in mk_prodi]

    print("Matakuliah:", ", ".join(mk_kode_list) or "-")
    print("Mahasiswa dan rata-rata nilai:")

    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if n.kode_mk in mk_kode_list]

        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
        else:
            avg = 0

        print(f" {m.nim} - {m.nama}: {round(avg, 2)}")

    print("-" * 40)


# blok eksekusi
if __name__ == "__main__":
    # universitas dan prodi
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")

    # mata kuliah
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")

    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    # mahasiswa
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")

    # nilai mahasiswa
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m2.tambah_nilai(Nilai("TI101", 90))

    # tampilkan report
    report_program(prodi_ti, [m1, m2])
