import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
# SELECT ALL DATA FAUNA

kursor = koneksi.cursor()
#mengambil semua data dalam tabel dan tampilkan
kursor.execute("SELECT *FROM FAUNA WHERE jenis = 'Mamalia' ")
# tampilkan dalam bentuk baris
data_fauna = kursor.fetchall()

print("DATA FAUNA")
print("="*123)
print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("="*123)
#Tampilkan data sesuai format table dg perulangan
for baris in data_fauna:
    print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()