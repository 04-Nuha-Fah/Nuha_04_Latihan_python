
import json

# Baca data lama
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

# Tambahkan user baru
users.append({
        "nama": input(""),
        "umur": int(),
        "kelas": input(""),
        "password": input("")
})

# Simpan kembali
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print("User berhasil ditambahkan")