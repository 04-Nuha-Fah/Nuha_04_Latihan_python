import ModulMath
import ModulBangunDatar

print("Menu Modul")
print("1.Ganjil Genap\n2.Perkalian\n3.Pembagian\n4.Luas Persegi Panjang\n5.Keliling Persegi Panjang\n6.Luas Jajar Genjang")
print("")
a = int(input("No = "))
if a == 1:
    print(ModulMath.ganjil_genap(print("Ganjil Genap\nMasukkan angkamu")))
if a == 2:
    print(ModulMath.perkalian(print("Perkalian\nMasukkan Angkamu")))
if a == 3:
    print(ModulMath.pembagian(print("Pembagian\nMasukkan Angkamu")))
if a == 4:
    print(ModulBangunDatar.hitung_luas_persegi_panjang(print("Hitung Luas Persegi Panjangmu\nMasukkan Angkamu")))
if a == 5:
    print(ModulBangunDatar.hitung_keliling_persegi_panjang(print("Hitung Keliling Persegi Panjangmu\nMsukkan Angkamu")))
if a == 6:
    print(ModulBangunDatar.hitung_luas_jajar_genjang(print("Hitung Luas Jajar Genjangmu\nMasukkan Angkamu")))
