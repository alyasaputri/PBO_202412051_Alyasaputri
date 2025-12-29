from abc import ABC, abstractmethod
import math

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

print()
l = Lingkaran(5)
p = PersegiPanjang(4, 3)
print("Luas Lingkaran:", l.luas())
print("Keliling Lingkaran:", l.keliling())
print("Luas Persegi Panjang:", p.luas())
print("Keliling Persegi Panjang:", p.keliling())


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

    def keliling(self):
        return 4 * self.sisi

print("\n")
s = Persegi(6)
print("Luas Persegi:", s.luas())
print("Keliling Persegi:", s.keliling())


print("\n")
s2 = Persegi(6)
print("Luas Persegi:", s2.luas())
print("Keliling Persegi:", s2.keliling())

class PersegiPanjangWarna(PersegiPanjang):
    def __init__(self, panjang, lebar, warna):
        super().__init__(panjang, lebar)
        self.warna = warna

    def info(self):
        return f"Persegi Panjang warna {self.warna}"

print("\n")
pw = PersegiPanjangWarna(4, 3, "Merah")
print("Luas:", pw.luas())
print("Keliling:", pw.keliling())
print("Info:", pw.info())
