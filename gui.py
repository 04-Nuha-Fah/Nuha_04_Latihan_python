import tkinter as tk
from tkinter import messagebox
import mysql.connector


# =========================
# KONFIGURASI DATABASE
# =========================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1843322Abc?",
    "database": "school"
}


# =========================
# FUNGSI DATABASE
# =========================
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


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
            messagebox.showinfo(
                "Login",
                "You Successfully Logged In"
            )
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


# =========================
# FUNGSI PINDAH HALAMAN
# =========================
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()


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


# =========================
# GUI UTAMA
# =========================
gui = tk.Tk()
gui.geometry("480x480")
gui.title("GUI LOGIN")
gui.config(background="#333333")

try:
    icon = tk.PhotoImage(file="Icon.png")
    gui.iconphoto(True, icon)
except tk.TclError:
    pass

frame = tk.Frame(gui, bg="#333333")
frame.pack(expand=True)

show_login()

gui.mainloop()
