## Wajib
from tkinter import *
import mysql.connector

global InfoLabel

"""


        Nama : Hamzah Wiranata
        Name : Hamzah Wiranata


"""

## Hubungkan Ke Database Mu, Sebelum Itu Buat Database Mu Dulu!
mysql = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "databaseku")

## Command Masuk
def Masuk():
	global InfoLabel
	## Menghapus Label "InfoLabel"
	InfoLabel.destroy()
	Nama = NamaEntry.get()
	Sandi = SandiEntry.get()
	## Jika Nama Yang Di Masukan Pengguna Di "NamaEntry" Kosong Maka Akan Memanggil Effect Ini
	if Nama == "":
		InfoLabel = Label(MaBox, text="Nama Tidak Boleh Kosong!", compound="center", font=("arial", 11, "bold"))
		InfoLabel.place(rely=0.6, relx=0.5, anchor="center")
	## Jika Sandi Yang Di Masukan Pengguna Di "SandiEntry" Kosong Maka Akan Memanggil Effect Ini
	elif Sandi == "":
		InfoLabel = Label(MaBox, text="Sandi Tidak Boleh Kosong!", compound="center", font=("arial", 11, "bold"))
		InfoLabel.place(rely=0.6, relx=0.5, anchor="center")
	## Jika Nama Dan Sandi Tidak Kosong Maka Akan Lanjut Ke Tahap Berikut Nya
	else:
		cursor = mysql.cursor()
		sql = "SELECT * FROM informasiakunku WHERE Nama = %s and Sandi = %s"
		cursor.execute(sql, [Nama, Sandi])
		hasil = cursor.fetchall()
		## Jika Nama Dan Sandi Yang Di Masukan Pengguna Ada Di Dalam Database
		if hasil:
			for i in hasil:
				InfoLabel = Label(MaBox, text="Berhasil Masuk!", compound="center", font=("arial", 11, "bold"))
				InfoLabel.place(rely=0.6, relx=0.5, anchor="center")
		## Jika Nama Dan Sandi Yang Di Masukan Pengguna Tidak Ada Di Dalam Database
		else:
			InfoLabel = Label(MaBox, text="Gagal Untuk Masuk, Akun Tersebut Belum Terdaftar!", compound="center", font=("arial", 11, "bold"))
			InfoLabel.place(rely=0.6, relx=0.5, anchor="center")

## Box Masuk
MaBox = Tk()
MaBox.title("Masuk Akun")
MaBox.geometry("490x450+450+145")
## ==============================[LABEL]============================== ##
MasukLabel = Label(MaBox, text="Masuk Akun", compound="center", font=("arial", 20, "bold"))
MasukLabel.place(rely=0.2, relx=0.5, anchor="center")

NamaLabel = Label(MaBox, text="Nama", compound="top", font=("arial", 11, "bold"))
NamaLabel.place(rely=0.4, relx=0.2, anchor="w")

SandiLabel = Label(MaBox, text="Sandi", compound="top", font=("arial", 11, "bold"))
SandiLabel.place(rely=0.5, relx=0.2, anchor="w")

InfoLabel = Label(MaBox, text="", compound="center")
InfoLabel.place(rely=0.6, relx=0.5, anchor="center")

## ==============================[ENTRY]============================== ##
NamaEntry = Entry(MaBox)
NamaEntry.place(rely=0.4, relx=0.5, anchor="center")

SandiEntry = Entry(MaBox, show="*")
SandiEntry.place(rely=0.5, relx=0.5, anchor="center")

## ==============================[BUTTON]============================== ##
MasukButton = Button(MaBox, text="Masuk", compound="center", command=Masuk)
MasukButton.place(rely=0.7, relx=0.5, anchor="center")

## Agar Ukuran Box Tidak Bisa Di Atur Besar Kecil Nya Oleh Pengguna
MaBox.resizable(False, False)
MaBox.mainloop()