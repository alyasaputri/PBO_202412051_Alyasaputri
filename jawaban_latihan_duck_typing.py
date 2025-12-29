class Laptop:
    def nyalakan(self):
        return "Laptop menyala, sistem booting..."


class Smartphone:
    def nyalakan(self):
        return "Smartphone menyala, logo muncul..."


def tes_nyala(obj):
    print(obj.nyalakan())


# Demonstrasi duck typing
l = Laptop()
s = Smartphone()

tes_nyala(l)
tes_nyala(s)
