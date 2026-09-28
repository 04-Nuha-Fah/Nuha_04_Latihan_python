import tkinter as tk
from tkinter import messagebox
import mysql.connector

#Database
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1843322Abc?",
    "database": "school"
}


gui = tk.Tk()
gui.geometry("480x480")
gui.title("GUI MODUL")
gui.config(background="#333333")

try:
    icon = tk.PhotoImage(file="Icon.png")
    gui.iconphoto(True, icon)
except tk.TclError:
    pass

frame = tk.Frame(gui, bg="#333333")
frame.pack(expand=True)

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


#Signin
def signin():
    username = user_entry.get().strip()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Peringatan",
            "Username dan password harus diisi!"
        )
        return

    mydb = None
    mycursor = None

    try:
        mydb = get_connection()
        mycursor = mydb.cursor()

        sql = """
            SELECT * FROM login_siswa
            WHERE Nama = %s AND Password = %s
        """
        mycursor.execute(sql, (username, password))
        result = mycursor.fetchone()

        if result:
            Modul_MTK()
            user_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau password salah!"
            )

    except mysql.connector.Error as err:
        messagebox.showerror(
            "Error",
            f"Gagal terhubung ke database: {err}"
        )

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


#Signup
def signup():
    username = user_entry.get().strip()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Peringatan",
            "Username dan password harus diisi!"
        )
        return

    mydb = None
    mycursor = None

    try:
        mydb = get_connection()
        mycursor = mydb.cursor()

        # Memeriksa apakah username sudah digunakan
        check_sql = """
            SELECT * FROM login_siswa
            WHERE Nama = %s
        """
        mycursor.execute(check_sql, (username,))

        if mycursor.fetchone():
            messagebox.showwarning(
                "Peringatan",
                "Username sudah terdaftar!"
            )
            return

        sql = """
            INSERT INTO login_siswa (Nama, Password)
            VALUES (%s, %s)
        """
        mycursor.execute(sql, (username, password))
        mydb.commit()

        messagebox.showinfo(
            "Signup",
            "Akun berhasil dibuat!"
        )

        show_login()

    except mysql.connector.Error as err:
        messagebox.showerror(
            "Error",
            f"Gagal membuat akun: {err}"
        )

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()


def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

#GUI Signin
def show_login():
    clear_frame()

    tk.Label(
        frame,
        text="Sign In",
        font=("Arial", 25, "bold"),
        fg="white",
        bg="#333333"
    ).grid(row=0, column=1, pady=16)

    tk.Label(
        frame,
        text="Username",
        font=("Arial", 16),
        fg="white",
        bg="#333333"
    ).grid(row=1, column=0)

    global user_entry, password_entry

    user_entry = tk.Entry(frame, font=("Arial", 16))
    user_entry.grid(row=1, column=1)

    tk.Label(
        frame,
        text="Password",
        font=("Arial", 16),
        fg="white",
        bg="#333333"
    ).grid(row=2, column=0)

    password_entry = tk.Entry(
        frame,
        show="*",
        font=("Arial", 16)
    )
    password_entry.grid(row=2, column=1)

    tk.Button(
        frame,
        text="LOGIN",
        font=("Arial", 16),
        fg="white",
        bg="#FF3399",
        command=signin
    ).grid(row=4, column=1, pady=16)

    tk.Label(
        frame,
        text="Belum memiliki akun?",
        font=("Arial", 8),
        fg="white",
        bg="#333333"
    ).grid(row=6, column=1)

    tk.Button(
        frame,
        text="Sign Up",
        font=("Arial", 8),
        fg="white",
        bg="#FF3399",
        command=show_signup
    ).grid(row=6, column=2)


def show_signup():
    clear_frame()

    tk.Label(
        frame,
        text="Sign Up",
        font=("Arial", 25, "bold"),
        fg="white",
        bg="#333333"
    ).grid(row=0, column=1, pady=16)

    tk.Label(
        frame,
        text="Username",
        font=("Arial", 16),
        fg="white",
        bg="#333333"
    ).grid(row=1, column=0)

    global user_entry, password_entry

    user_entry = tk.Entry(frame, font=("Arial", 16))
    user_entry.grid(row=1, column=1)

    tk.Label(
        frame,
        text="Password",
        font=("Arial", 16),
        fg="white",
        bg="#333333"
    ).grid(row=2, column=0)

    password_entry = tk.Entry(
        frame,
        show="*",
        font=("Arial", 16)
    )
    password_entry.grid(row=2, column=1)

    tk.Button(
        frame,
        text="SIGNUP",
        font=("Arial", 16),
        fg="white",
        bg="#FF3399",
        command=signup
    ).grid(row=4, column=1, pady=16)

    tk.Button(
        frame,
        text="Kembali ke Login",
        font=("Arial", 10),
        fg="white",
        bg="#555555",
        command=show_login
    ).grid(row=6, column=1, pady=10)
    

def gui_luas_persegi_panjang():
    clear_frame()
    tk.Label(
        frame,
        text="Luas PERSEGI PANJANG",
        font=("Arial", 22, "bold"),
        bg="#FF3399"
        
    ).pack(pady=30)


    tk.Label(
        frame,
        text="Panjang",
        font=("Arial", 13),
        bg="#FF3399"
    ).pack()

    entry_panjang = tk.Entry(
        frame,
        font=("Arial", 13),
        width=25
    )
    entry_panjang.pack(pady=5)

    tk.Label(
        frame,
        text="Lebar",
        font=("Arial", 13),
        bg="#FF3399"
    ).pack()

    entry_lebar = tk.Entry(
        frame,
        font=("Arial", 13),
        width=25
    )
    entry_lebar.pack(pady=5)

    hasil = tk.Label(
        frame,
        text="Hasil: -",
        font=("Arial", 15, "bold")
    )
    hasil.pack(pady=20)


    def hitung():
        try:
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())

            luas = panjang * lebar

            hasil.config(
                text=f"Luas = {luas:g} cm²"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        frame,
        text="HITUNG",
        font=("Arial", 13, "bold"),
        width=20,
        command=hitung,
        bg="#FF3399"
    ).pack(pady=5)

    tk.Button(
        frame,
        text="Kembali",
        font=("Arial", 11),
        width=20,
        command=Modul_MTK
    ).pack(pady=10)
    
    
def gui_keliling_persegi_panjang():
    clear_frame()

    tk.Label(
        frame,
        text="KELILING PERSEGI PANJANG",
        font=("Arial", 22, "bold"),
        bg="#FF3399"
    ).pack(pady=30)

    tk.Label(
        frame,
        text="Panjang",
        font=("Arial", 13),
        bg="#FF3399"
    ).pack()

    entry_panjang = tk.Entry(
        frame,
        font=("Arial", 13),
        width=25
    )
    entry_panjang.pack(pady=5)

    tk.Label(
        frame,
        text="Lebar",
        font=("Arial", 13),
        bg="#FF3399"
    ).pack()

    entry_lebar = tk.Entry(
        frame,
        font=("Arial", 13),
        width=25
    )
    entry_lebar.pack(pady=5)

    hasil = tk.Label(
        frame,
        text="Hasil: -",
        font=("Arial", 15, "bold"),
    )
    hasil.pack(pady=20)


    def hitung():
        try:
            panjang = float(entry_panjang.get())
            lebar = float(entry_lebar.get())

            keliling = 2 * (panjang + lebar)

            hasil.config(
                text=f"Keliling = {keliling:g} cm"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        frame,
        text="HITUNG",
        font=("Arial", 13, "bold"),
        width=20,
        command=hitung,
        bg="#FF3399"
    ).pack(pady=5)

    tk.Button(
        frame,
        text="Kembali",
        font=("Arial", 11),
        width=20,
        command=Modul_MTK
    ).pack(pady=10)


def gui_luas_jajar_genjang():
    clear_frame()

    tk.Label(
        frame,
        text="LUAS JAJAR GENJANG",
        font=("Arial", 22, "bold")
    ).pack(pady=30)

    tk.Label(
        frame,
        text="Alas",
        font=("Arial", 13)
    ).pack()

    entry_alas = tk.Entry(
        frame,
        font=("Arial", 13),
        width=25
    )
    entry_alas.pack(pady=5)

    tk.Label(
        frame,
        text="Tinggi",
        font=("Arial", 13)
    ).pack()

    entry_tinggi = tk.Entry(
        frame,
        font=("Arial", 13),
        width=25
    )
    entry_tinggi.pack(pady=5)

    hasil = tk.Label(
        frame,
        text="Hasil: -",
        font=("Arial", 15, "bold")
    )
    hasil.pack(pady=20)

    def hitung():
        try:
            alas = float(entry_alas.get())
            tinggi = float(entry_tinggi.get())

            luas = alas * tinggi

            hasil.config(
                text=f"Luas = {luas:g} cm²"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        frame,
        text="HITUNG",
        font=("Arial", 13, "bold"),
        width=20,
        command=hitung
    ).pack(pady=5)

    tk.Button(
        frame,
        text="Kembali",
        font=("Arial", 11),
        width=20,
        command=Modul_MTK
    ).pack(pady=10)
    
    
def Modul_MTK():
    clear_frame()

    tk.Label(
        frame,
        text="Modul Matematika",
        font=("Arial", 25, "bold"),
        fg="white",
        bg="#333333",
    ).grid(row=0, column=1, pady=16)
    
    
    
    tk.Button(
        frame,
        text="Ganjil / Genap",
        font=("Arial", 16),
        fg="white",
        bg="#333333",
        width=15,
        height=5
    ).grid(row=1, column=0, pady=16)
    
    tk.Button(
        frame,
        text="Perkalian",
        font=("Arial", 16),
        fg="white",
        bg="#333333",
        width=15,
        height=5,
    ).grid(row=2,column=0, pady=16)
    
    tk.Button(
        frame,
        text="Pembagian",
        font=("Arial", 16),
        fg="white",
        bg="#333333",
        width=15,
        height=5
    ).grid(row=3,column=0, pady=16)
    
    tk.Button(
        frame,
        text="L Persegi Panjang",
        font=("Arial", 16),
        fg="white",
        bg="#333333",
        width=15,
        height=5,
        command=gui_luas_persegi_panjang
    ).grid(row=1,column=2, pady=16)
    
    tk.Button(
        frame,
        text="K Persegi Panjang",
        font=("Arial", 16),
        fg="white",
        bg="#333333",
        width=15,
        height=5,
        command=gui_keliling_persegi_panjang
    ).grid(row=2,column=2, pady=16)
    
    tk.Button(
        frame,
        text="K Persegi Panjang",
        font=("Arial", 16),
        fg="white",
        bg="#333333",
        width=15,
        height=5
    ).grid(row=3,column=2, pady=16)
    
    


# =========================
# GUI UTAMA
# =========================


show_login()

gui.mainloop()

