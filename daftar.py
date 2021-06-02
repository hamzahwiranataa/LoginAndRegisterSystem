## Wajib
from tkinter import *
import mysql.connector

global InfoLabel

"""


        Nama : Hamzah Wiranata
        Name : Hamzah Wiranata


"""

## Connect Ke Database mu
mysql = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "databaseku")

## Untuk Command Daftar
def Daftar():
	global InfoLabel
	InfoLabel.destroy()
	## Memanggil Entry Yang Telah Di Masukan Pengguna
	Nama = NamaEntry.get()
	Sandi = SandiEntry.get()
	SandiKonfirm = SandiKonfirmEntry.get()
	## Jika Entry "Nama" Kosong Makan Akan Memanggil Effect Ini
	if Nama == "":
		InfoLabel = Label(DafBox, text="Nama Tidak Boleh Kosong!", compound="center", font=("arial", 11, "bold"))
		InfoLabel.place(rely=0.7, relx=0.5, anchor="center")
	## Jika Entry "Sandi" Kosong Maka Akan Memanggil Effect Ini
	elif Sandi == "":
		InfoLabel = Label(DafBox, text="Sandi Tidak Boleh Kosong!", compound="center", font=("arial", 11, "bold"))
		InfoLabel.place(rely=0.7, relx=0.5, anchor="center")
	## Jika Entry "Sandi Konfirm" Kosong Maka Akan Memanggil Effect Ini
	elif SandiKonfirm == "":
		InfoLabel = Label(DafBox, text="Sandi Konfirm Tidak Boleh Kosong!", compound="center", font=("arial", 11, "bold"))
		InfoLabel.place(rely=0.7, relx=0.5, anchor="center")
	## Jika Sandi Dan SandiKonfirm Yang Di Masukan Di Dalam Entry Sama Maka Akan Lanjut Ke Tahap Berikut Nya
	elif Sandi == SandiKonfirm:
		cursor = mysql.cursor()
		## Menjalankan Command SQL 
		sql = "SELECT * FROM informasiakunku WHERE Nama = %s"
		cursor.execute(sql, [Nama])
		hasil = cursor.fetchall()
		## Jika Nama Yang Di Masukan Di "Nama Entry" Sudah Ada Di Database Maka Akan Tampil Label Ini
		if hasil:
			for i in hasil:
				InfoLabel = Label(DafBox, text="Nama Tersebut Telah Di Gunakan Oleh Orang Lain!", compound="center", font=("arial", 11, "bold"))
				InfoLabel.place(rely=0.7, relx=0.5, anchor="center")
		## Jika Nama Yang Di Masukan Di "Nama Entry" Belum Ada Di Database Maka Akan Lanjut Ke Tahap Berikut Nya
		else:
			cursor = mysql.cursor()
			sql = "INSERT INTO informasiakunku (Nama, Sandi) VALUES (%s, %s)"
			get = (Nama, Sandi)
			cursor.execute(sql, get)
			InfoLabel = Label(DafBox, text="Akun Berhasil Di Daftarkan!", compound="center", font=("arial", 11, "bold"))
			InfoLabel.place(rely=0.7, relx=0.5, anchor="center")
			mysql.commit()
		mysql.commit()
	## Jika Tidak Ada Effect Lain Yang Harus Di Jalankan Maka Akan Tampil Ini
	else:
		InfoLabel = Label(DafBox, text="Sandi Dan Sandi Konfirm Harus Sama!", compound="center", font=("arial", 11, "bold"))
		InfoLabel.place(rely=0.7, relx=0.5, anchor="center")


DafBox = Tk()
DafBox.title("Daftar Akun")
DafBox.geometry("490x450+450+145")
## ==============================[LABEL]============================== ##
DaftarLogo = Label(DafBox, text="Daftar Akun", compound="center", font=("arial", 20, "bold"))
DaftarLogo.place(rely=0.2, relx=0.5, anchor="center")

NamaLabel = Label(DafBox, text="Nama", compound="top", font=("arial", 11, "bold"))
NamaLabel.place(rely=0.4, relx=0.1, anchor="w")

SandiLabel = Label(DafBox, text="Sandi", compound="top", font=("arial", 11, "bold"))
SandiLabel.place(rely=0.5, relx=0.1, anchor="w")

SandiKonfirmLabel = Label(DafBox, text="Sandi Konfirm", compound="top", font=("arial", 11, "bold"))
SandiKonfirmLabel.place(rely=0.6, relx=0.1, anchor="w")

InfoLabel = Label(DafBox, text="", compound="center")
InfoLabel.place(rely=0.7, relx=0.5, anchor="center")

## ==============================[ENTRY]============================== ##
NamaEntry = Entry(DafBox)
NamaEntry.place(rely=0.4, relx=0.5, anchor="center")

SandiEntry = Entry(DafBox, show="*")
SandiEntry.place(rely=0.5, relx=0.5, anchor="center")

SandiKonfirmEntry = Entry(DafBox, show="*")
SandiKonfirmEntry.place(rely=0.6, relx=0.5, anchor="center")

## ==============================[BUTTON]============================= ##
DaftarButton = Button(DafBox, text="Daftar", compound="center", command=Daftar)
DaftarButton.place(rely=0.8, relx=0.5, anchor="center") 

## Agar Lebar Dan Panjang Box Tidak Bisa Di Atur Oleh Pengguna
DafBox.resizable(False, False)
DafBox.mainloop()