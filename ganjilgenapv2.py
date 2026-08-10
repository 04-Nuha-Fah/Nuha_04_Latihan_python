#Perulangan Ganjil genap#

while True:
    
    a = int(input("Angka: "))
    if a % 2 == 0:
        print(f"{a} adalah bilangan GENAP")
    else:
        print(f"{a} adalah bilangan GANJIL")
        
    if a == 100:
        break
    
print("selesai")