def operasi():
    print("=== Operasi Matematika Aman ===")
    print("Pilih operasi:")
    print("1. Pembagian")
    print("2. Perkalian")

    # ambil pilihan (tidak langsung memaksa jadi angka supaya user input tetap tampil di console)
    pilihan = input("Masukkan pilihan (1/2): ").strip()

    # ambil input sebagai string (agar echo di console terlihat saat SS)
    x = input("Masukkan angka pertama: ").strip()
    y = input("Masukkan angka kedua: ").strip()

    try:
        # 1) Validasi input kosong (soal b)
        if x == "" or y == "":
            raise ValueError("Input tidak boleh kosong!")

        # 2) Cek apakah input bisa diubah jadi float, jika tidak -> ValueError
        try:
            a = float(x)
            b = float(y)
        except ValueError:
            raise ValueError("Input tidak valid: masukkan angka yang benar!")

        # 3) Validasi angka positif (soal c)
        if a < 0 or b < 0:
            raise ValueError("Hanya angka positif yang diperbolehkan!")

        # 4) Proses operasi sesuai pilihan
        if pilihan == "1":
            # Pembagian — ini bisa memicu ZeroDivisionError
            hasil = a / b
            print(f"Hasil pembagian: {hasil}")

        elif pilihan == "2":
            hasil = a * b
            print(f"Hasil perkalian: {hasil}")

        else:
            # jika pilihan bukan 1 atau 2, tampilkan pesan (tidak dianggap exception untuk blok else)
            print("Pilihan operasi tidak valid!")
            # tidak raise agar blok finally tetap jalan; namun jangan tampilkan "Operasi berhasil..." karena tidak ada operasi yang valid
            return

    except ZeroDivisionError:
        # Tangani pembagian dengan nol (soal f skenario 2)
        print("Error: Tidak bisa membagi dengan nol!")

    except ValueError as ve:
        # Menangani input kosong, angka negatif, atau konversi gagal
        print(f"Error: {ve}")

    else:
        # (d) blok else hanya dieksekusi jika tidak ada exception
        print("Operasi berhasil tanpa error!")

    finally:
        # (e) selalu tampilkan
        print("Selesai memproses input.")


if __name__ == "__main__":
    operasi()
