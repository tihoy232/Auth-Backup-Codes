""" Seperti judulnya, Generator Backup Code Discord, itu menyebalkan. 
Waktu grendengan (ngoceh). 

pertama, latar belakang: Saya memiliki 2fa pada perselisihan yang diatur untuk menggunakan nomor telepon saya, dan saya tidak memiliki cadangan kode cadangan saya. <br>
Saya baru-baru ini dirampok ponsel saya, dan beberapa waktu berlalu (sekitar satu atau dua bulan), saya mencoba membuka perselisihan, boom, saya keluar dari ponsel, pc desktop, dan laptop saya,
dan yang tersisa hanyalah akun alt saya, dan alasan untuk menangis sampai tertidur. 
kata-kata kasar.

Bagaimanapun saya membuat program ini untuk memaksa masuk ke akun saya, dan mudah-mudahan saya tidak mendapat teguran dari perselisihan karena ini bukan semacam masalah keamanan,
dan berpikir untuk menjadikannya open source. 
Skrip kecil ini juga menggunakan beberapa kode dari generator kode saya yang akan saya jadikan open source suatu hari nanti.
Saya lupa menyebutkan ini di komit pertama, tetapi alasan mengapa perselisihan 2fa menyebalkan, adalah karena: 
a) jika Anda menghubungi perselisihan, mereka akan memberi Anda respons bot generik: oops, apakah Anda punya cadangan, bukan? kalau begitu lakukan saja hal lain
b) Anda mungkin berkata, baiklah itu masalah Anda, dan saya setuju, namun jika Anda mengirim email dukungan, mereka akan memberi tahu Anda: ups kami tidak dapat melakukan apa-apa, atau HAPUS AKUN ANDA, seperti bruh, itu seharusnya berbicara sendiri

Source : 1. SpaghettDev
		 2. PALGET666
"""
from os import getcwd
from time import sleep
from typing import Union
from random import choice
from os import mkdir, path, getcwd

def formatgc(arr: list) -> str:

	return ''.join(map(str, arr))

def genRndmChr(num: int = 0, gty: str = "abcdefghijklmnopqrstuvwxyz0123456789") -> Union[str, None]:

	arr = []
	if num == 0:
		print("Masukin berapa banyak code yang lu pengen!")
		sleep(5)
		quit()

	for x in range(num):
		arr.append(choice(gty))
	return formatgc(arr)

def genRndmDigit(num: int = 0, gty: str = "0123456789") -> Union[str, None]:

	arr = []
	if num == 0:
		print("Masukin berapa banyak code yang lu pengen!")
		sleep(5)
		quit()

	for x in range(num):
		arr.append(choice(gty))
	return formatgc(arr)

def writeToFile(file: str, mode: str, towrite: str) -> None:

	with open(file, mode) as out:
		out.write(towrite)

def createGDir() -> None:

	try:
		mkdir(path.join(getcwd() + "/Kode Generator"))
	except PermissionError:
		print("Please grant permission to make folders.")
	except FileExistsError:
		pass

def genBackup(num: int): 

	ar = []
	for x in range(num):
		ar.append("Code Backup: " + genRndmChr(4) + "-" + genRndmChr(4) + "\n")
	return formatgc(ar)

def genNormal(num: int): 

	ar = []
	for x in range(num):
		ar.append("Code Normal: " + genRndmDigit(6) +  "\n")
	return formatgc(ar)

createGDir()

if __name__ == "__main__":
	try:
		print("====================================================", )
		print("[PALGET GENERATOR BACKUP DISCORD CODES]")
		print("SOCIAL MEDIA:", )
		print("FACEBOOK : HTTTPS://FACEBOOK.COM/MASTIHOY", )
		print("INSTAGRAM: @PALGET666", )
		print("====================================================\n", )	
		menu = int(input("Jenis kode apa yang ingin lu hasilkan?\n[1] - 8 Digit Backup Code\n[2] - 6 Digit Normal Code\n ", ))
		if menu == 1:
			t = int(input(" Berapa banyak code Discord Backups? ", ))
			filep = getcwd() + f"/Kode Generator/ {t} backup codes.txt"
			writeToFile(filep, "a", genBackup(t))
			print("Telah tersimpan di Backup Codes.", )
			quit()
		elif menu == 2:
			t = int(input(" Berapa banyak code Discord Normal? ", ))
			filep = getcwd() + f"/Kode Generator/ {t} normal codes.txt"
			writeToFile(filep, "a", genNormal(t))
			print("Telah tersimpan normal codes.", )
			quit()
		else:
			print("Invalid option entered!")
			
	except BaseException as ex:
		if isinstance(ex, SystemExit) or isinstance(ex, KeyboardInterrupt):
			quit()
