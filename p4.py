class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim



mhs = Mahasiswa("irpan maulan", "14022500098")
print(mhs.nama)
print(mhs.nim)