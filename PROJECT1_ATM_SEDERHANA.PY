print("===============================")
print("SELAMAT DATANG DI ATM")
print("PILIH OPTION")
print("1. CHECK SALDO")
print("2. AMBIL SALDO")
print("3. MASUKAN SALDO UNTUK MENABUNG")
print("===============================")
option=int(input("SILAHKAN PILIH OPTION :"))
uang_kamu=200000
if option==1:
    print("SALDO ANDA BERJUMLAH Rp.200.000")
elif option==2:
    print("SALDO ANDA BERJUMLAH Rp.200.000, MAU AMBIL SALDO BERAPA?")
    print("1. 100.000")
    print("2. 200.000")
    option2=int(input("OPTION: "))
    if option2==1:
        hasil=uang_kamu-100000
        print("SALDO ANDA SEKARANG BERJUMLAH",hasil)
    elif option2==2:
        hasil2=uang_kamu-200000
        print("SALDO ANDA SEKARANG BERJUMLAH",hasil2)
    else:
        print("TRANSAKSI GAGAL, SILAKAN COBA LAGI!")
elif option==3:
        print("SALDO ANDA BERJUMLAH Rp.200.000, MAU TABUNG BERAPA?")
        option3=int(input("MASUKAN JUMLAH SALDO :"))
        hasil3=uang_kamu+option3
        print("JUMLAH SALDO ANDA SEKARANG ADALAH",hasil3)
else:
        print("TRANSAKSI GAGAL, SILAKAN COBA LAGI!")

