def login(c):
  while True:
    import mysql.connector

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="1843322Abc?",
      database="school"
    )

    a = input("Nama = ")
    b = input("Password = ")

    mycursor = mydb.cursor()

    sql = "SELECT * FROM login_siswa WHERE Nama = %s AND Password = %s"
    val = (a, b)

    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    if myresult:
        print(f"Selamat datang {a}")
        break
    else:
        print("Nama atau password anda salah")
