class Pemain:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi

    def memperkenalkan_diri(self):
        print(f"\n{self.nama}: Hai, nama saya {self.nama}.")
        print(f"Saya bermain di posisi {self.posisi}.")

    def mengajak_latihan(self):
        print(f"\n{self.nama}: Rafi, kamu jadi ikut latihan")
        print("sepak bola sore ini?")

    def bertanya_latihan(self):
        print(f"\n{self.nama}: Rio, hari ini kita latihan apa?")
        print("Apakah latihan passing dan shooting?")


class Teman:
    def __init__(self, nama, posisi):
        self.nama = nama
        self.posisi = posisi

    def menyambut(self):
        print(f"\n{self.nama}: Hai, Rio!")
        print("Tentu saja, saya ikut latihan sore ini.")

    def menjelaskan_latihan(self):
        print(f"\n{self.nama}: Hari ini kita akan latihan")
        print("passing, dribbling, dan shooting.")
        print("Setelah itu kita bermain pertandingan kecil.")

    def pemanasan(self):
        print(f"\n{self.nama}: Sebelum latihan, kita harus")
        print("melakukan pemanasan terlebih dahulu.")
        print("Supaya otot kita tidak mengalami cedera.")

    def latihan_passing(self):
        print(f"\n{self.nama}: Ayo kita mulai latihan passing.")
        print("Kita saling mengoper bola dengan akurat.")

    def latihan_shooting(self):
        print(f"\n{self.nama}: Sekarang kita latihan shooting.")
        print("Coba tendang bola ke arah gawang.")

    def evaluasi(self):
        print(f"\n{self.nama}: Latihan hari ini cukup bagus.")
        print("Kita harus terus berlatih agar semakin hebat.")

    def berpamitan(self):
        print(f"\n{self.nama}: Baik, Rio. Sampai jumpa")
        print("di latihan berikutnya.")


class Percakapan:
    def __init__(self, pemain, teman):
        self.pemain = pemain
        self.teman = teman

    def mulai(self):
        print("=== PERCAKAPAN LATIHAN SEPAK BOLA ===")
        self.pemain.memperkenalkan_diri()
        self.teman.menyambut()
        self.pemain.mengajak_latihan()
        print(f"\n{self.teman.nama}: Iya, Rio.")
        print("Aku sudah menyiapkan sepatu dan bola.")
        self.pemain.bertanya_latihan()
        self.teman.menjelaskan_latihan()
        print(f"\n{self.pemain.nama}: Baik, Rafi.")
        print("Aku ingin meningkatkan kemampuan passing.")
        self.teman.pemanasan()
        print(f"\n{self.pemain.nama}: Setuju, Rafi.")
        print("Kita lakukan pemanasan selama 10 menit.")
        self.teman.latihan_passing()
        print(f"\n{self.pemain.nama}: Operanmu bagus, Rafi.")
        print("Sekarang coba oper bola ke arah kakiku.")
        print(f"\n{self.teman.nama}: Siap, Rio!")
        print("Aku akan mencoba memberikan operan yang akurat.")
        self.teman.latihan_shooting()
        print(f"\n{self.pemain.nama}: Aku akan mencoba")
        print("menendang bola ke sudut kanan gawang.")
        print(f"\n{self.teman.nama}: Wah, tendanganmu bagus!")
        print("Bola hampir masuk ke dalam gawang.")
        print(f"\n{self.pemain.nama}: Terima kasih, Rafi.")
        print("Sekarang giliran kamu melakukan shooting.")
        print(f"\n{self.teman.nama}: Baik, Rio.")
        print("Aku akan mencoba menendang lebih keras.")
        print(f"\n{self.pemain.nama}: Hebat, Rafi!")
        print("Tendanganmu berhasil masuk ke gawang.")
        print(f"\n{self.teman.nama}: Terima kasih, Rio.")
        print("Kita memang harus saling mendukung.")
        self.teman.evaluasi()
        print(f"\n{self.pemain.nama}: Betul, Rafi.")
        print("Latihan hari ini sangat menyenangkan.")
        print("Semoga kemampuan kita semakin meningkat.")
        print(f"\n{self.teman.nama}: Setuju, Rio.")
        print("Besok kita latihan lagi, ya.")
        self.teman.berpamitan()
        print(f"\n{self.pemain.nama}: Oke, Rafi.")
        print("Sampai jumpa di latihan berikutnya!")
        print("Tetap semangat!")
        print("\n=== LATIHAN SELESAI ===")


# Membuat objek
rio = Pemain("Rio", "Penyerang")
rafi = Teman("Rafi", "Gelandang")

# Menjalankan percakapan
percakapan = Percakapan(rio, rafi)
percakapan.mulai()