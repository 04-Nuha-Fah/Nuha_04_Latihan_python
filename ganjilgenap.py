#Ganjil Genap#

#a = int(input("Angka: "))
#if a % 2 == 0:
    #print(f"{a} adalah bilangan GENAP")
#else:
    #print(f"{a} adalah bilangan GANJIL")
    
#b = int(input("Angka: "))
#if b // 2 * 2 == b:
    #print(f"{b} adalah bilangan GENAP")
#else:
    #print(f"{b} adalah bilangan GANJIL")
    
    
#Perulangan Ganjil genap#

#while True:
    
    #a = int(input("Angka: "))
    #if a % 2 == 0:
        #print(f"{a} adalah bilangan GENAP")
    #else:
        #print(f"{a} adalah bilangan GANJIL")
        
    #if a == 100:
        #break
    
#print("selesai")


#Modularitas

#Modul Ganjil_Genap
def ganjil_genap(a):
    while True:
        ank = int(input("angkamu = "))
        if ank % 2 == 0:
            print(f"{ank} adalah bilangan GENAP")
        else:
            print(f"{ank} adalah bilangan GANJIL")
            
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
        
        if pilihan == 'stop':
            print("Program selesai.")
            break
                
#Modul Perkalian
def perkalian(b):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("ingin dikali dengan = "))
        print(f"{angka} * {ank} = {angka * ank}")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
    
#Modul Pembagian
def pembagian(c):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("ingin dibagi dengan = "))
        print(f"{angka} / {ank} = {angka / ank}")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break

#Modul Luas Persegi Panjang
def hitung_luas_persegi_panjang(c):
    while True:
        angkapjg = int(input("Panjang = "))
        angkalbr = int(input("Lebar = "))
        print(f"{angkapjg}cm * {angkalbr}cm = {angkapjg * angkalbr} cm")
        print(f"jadi luas persegi panjangmu adalah {angkapjg * angkalbr}cm atau {angkapjg * angkalbr / 100}m")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
        
#Modul Keliling Persegi Panjang
def hitung_keliling_persegi_panjang(c):
    while True:
        angkapjg = int(input("Panjang = "))
        angkalbr = int(input("Lebar = "))
        print(f"2 * {angkapjg}cm * {angkalbr}cm = {2 * angkapjg * angkalbr} cm")
        print(f"jadi luas persegi panjangmu adalah {2 * angkapjg * angkalbr}cm atau {2 * angkapjg * angkalbr / 100}m")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
        
#Modul Keliling Persegi Panjang
def hitung_luas_jajar_genjang(c):
    while True:
        angkaals = int(input("Alas = "))
        angkatgi = int(input("Tinggi = "))
        print(f"{angkaals}cm * {angkatgi}cm = {angkaals * angkatgi} cm")
        print(f"jadi luas jajar genjangmu adalah {angkaals * angkatgi}cm atau {angkaals * angkatgi / 100}m")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
