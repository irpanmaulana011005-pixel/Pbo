class BankAccount:
    def __init__(self, no, saldo=0):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
        self.no = no
        self.saldo = saldo

    def tampil(self):
        print(f"No Rekening : {self.no}")
        print(f"Saldo       : Rp. {self.saldo:,}".replace(",", "."))

try:
    Abul = BankAccount("1234567890", 1000)
    print("Rio berhasil dibuat")
    Abul.tampil()
except ValueError as e:
    print("Error pada Rio:", e)

print("-" * 30)

try:
    Alfa = BankAccount("1234567890", -1000)
    print("Rafi berhasil dibuat")
    Alfa.tampil()
except ValueError as e:
    print("Error pada Rafi:", e)