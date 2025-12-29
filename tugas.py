from abc import ABC, abstractmethod

# ========================================================
# 1. ABSTRACTION 
# ========================================================
class Pengguna(ABC):          
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod         
    def akses(self):
        pass

# ========================================================
# 4. CUSTOM EXCEPTION  
# ========================================================
class PoinTidakValidError(Exception):     
    """Error ketika poin tidak valid (negatif atau bukan angka)."""
    pass

# ========================================================
# CLASS MEMBER → IMPLEMENTASI ABSTRAKSI + SPECIAL METHODS
# ========================================================
class Member(Pengguna):        
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    # Implementasi abstract method  
    def akses(self):
        return f"Member {self.nama} memiliki hak akses penuh."

    # ====================================================
    # 2. SPECIAL METHODS 
    # ====================================================
    def __str__(self):        
        return f"Member: {self.nama} - Poin: {self.poin}"

    def __add__(self, other): 
        if not isinstance(other, Member):
            raise TypeError("Penjumlahan harus antar Member.")
        return self.poin + other.poin

    def __len__(self):         
        return len(self.nama)


# ========================================================
# 3. EXCEPTION HANDLING INPUT POIN  
# ========================================================
def input_poin():              
    while True:
        try:
            poin_text = input("Masukkan poin member: ").strip()

            if poin_text == "":
                print("Error: Input tidak boleh kosong!")
                continue

            if not poin_text.isdigit():
                raise ValueError("Poin harus berupa angka!")

            poin = int(poin_text)

            if poin < 0:
                raise PoinTidakValidError("Poin tidak boleh bernilai negatif!")

            return poin

        except ValueError as ve:                   
            print("Error:", ve)
        except PoinTidakValidError as pe:           
            print("Error:", pe)

# ========================================================
# 5. PROGRAM UTAMA 
# ========================================================
if __name__ == "__main__":
    print("=== INPUT MEMBER 1 ===")
    nama1 = input("Masukkan nama member 1: ")
    poin1 = input_poin()
    m1 = Member(nama1, poin1)

    print("\n=== INPUT MEMBER 2 ===")
    nama2 = input("Masukkan nama member 2: ")
    poin2 = input_poin()
    m2 = Member(nama2, poin2)

    print("\n=== HASIL PROGRAM ===")

    print("\n1) Info Member:")
    print(m1)
    print(m2)

    print("\n2) Jumlah Poin (m1 + m2):", m1 + m2)
    print("\n3) Panjang nama member 1:", len(m1))

    print("\n4) Hak akses:")
    print(m1.akses())
    print(m2.akses())

    print("\n5) Uji poin negatif:")
    try:
        test_negatif = Member("Uji", -5)
        if test_negatif.poin < 0:
            raise PoinTidakValidError("Poin tidak boleh negatif!")
    except PoinTidakValidError as e:
        print("Berhasil menangkap error:", e)
