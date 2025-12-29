class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk             # private

    # Getter protected
    def get_semester(self):
        return self._semester

    # Setter protected
    def set_semester(self, semester_baru):
        if semester_baru <= 0:
            raise ValueError("Semester harus lebih dari 0")
        self._semester = semester_baru

    # Getter private
    def get_ipk(self):
        return self.__ipk

    # Setter private
    def set_ipk(self, ipk_baru):
        if not (0.0 <= ipk_baru <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0")
        self.__ipk = ipk_baru


# ===== PROGRAM UTAMA =====
if __name__ == "__main__":
    # Jawaban (b): buat 2 objek Mahasiswa
    m1 = Mahasiswa("23001", "Budi", 2, 3.2)
    m2 = Mahasiswa("23002", "Siti", 4, 3.8)

    # Tampilkan data awal
    print("=== Data Mahasiswa Awal ===")
    print("NIM:", m1.nim, "| Nama:", m1.nama,
          "| Semester:", m1.get_semester(), "| IPK:", m1.get_ipk())
    print("NIM:", m2.nim, "| Nama:", m2.nama,
          "| Semester:", m2.get_semester(), "| IPK:", m2.get_ipk())

    # Jawaban (c): ganti semester dan IPK
    m1.set_semester(3)
    m1.set_ipk(3.6)

    m2.set_semester(5)
    m2.set_ipk(3.9)

    # Tampilkan data setelah diubah
    print("\n=== Data Mahasiswa Setelah Perubahan ===")
    print("NIM:", m1.nim, "| Nama:", m1.nama,
          "| Semester:", m1.get_semester(), "| IPK:", m1.get_ipk())
    print("NIM:", m2.nim, "| Nama:", m2.nama,
          "| Semester:", m2.get_semester(), "| IPK:", m2.get_ipk())
