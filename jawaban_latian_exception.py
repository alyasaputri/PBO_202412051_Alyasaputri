# =============== CUSTOM EXCEPTIONS ===============

class UmurTidakValidError(Exception):
    """Kesalahan untuk umur yang tidak masuk akal."""
    pass

class UmurTerlaluMudaError(Exception):
    """Error jika umur kurang dari 5."""
    pass

class UmurTerlaluTuaError(Exception):
    """Error jika umur lebih dari 100."""
    pass

class AkunTidakDiizinkanError(Exception):
    """Error jika umur kurang dari syarat daftar akun (18)."""
    pass


# =============== VALIDASI UMUR ===============

def set_umur(umur):
    if umur < 0:
        raise UmurTidakValidError("Umur tidak boleh negatif!")
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda! Minimal umur adalah 5 tahun.")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua! Maksimal umur adalah 100 tahun.")
    return umur


# =============== FUNGSI DAFTAR AKUN ===============

def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Akun tidak diizinkan! Minimal umur daftar adalah 18 tahun.")
    print("Akun berhasil dibuat!")


# =============== MAIN PROGRAM ===============

if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur = set_umur(u)
            print("Umur valid dan disimpan:", umur)
            break   # keluar loop jika input valid

        except ValueError:
            print("Input harus berupa bilangan bulat!")

        except (UmurTidakValidError, UmurTerlaluMudaError, UmurTerlaluTuaError) as e:
            print("Error:", e)
            print("Silakan coba lagi.\n")

    # Setelah umur valid → coba daftar akun
    try:
        daftar_akun(umur)
    except AkunTidakDiizinkanError as e:
        print("Error:", e)
