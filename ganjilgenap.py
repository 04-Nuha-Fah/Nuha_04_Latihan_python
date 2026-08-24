a = int(input("Angka: "))

if a % 2 == 0:
    print(f"{a} adalah bilangan GENAP")
else:
    print(f"{a} adalah bilangan GANJIL")
    
b = int(input("Angka: "))

if b // 2 * 2 == b:
    print(f"{b} adalah bilangan GENAP")
else:
    print(f"{b} adalah bilangan GANJIL")
    
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
