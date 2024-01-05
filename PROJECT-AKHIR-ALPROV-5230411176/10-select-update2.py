import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

# ubah berdasarkan id_pegawai
id_fauna = 4
jmlh_baru = 'Kalimantan Timur'

# mgunakan QUERY UPDATE
sql = (f"UPDATE fauna SET asal  = ? WHERE id_fauna = ?")
data = (jmlh_baru, id_fauna)
kursor.execute(sql,data)
koneksi.commit()

#cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tidak
    print(f"Data dengan ID {id_fauna} Berhasil diubah!!")
else:
    print(f"Tidak ada data fauna dengan ID {id_fauna}!")

kursor.execute("SELECT *FROM fauna")

data_fauna = kursor.fetchall()

print("DATA FAUNA")
print("="*123)
print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID Fauna", "Nama Fauna", "Jenis", "Asal", "Jumlah Saat Ini", "Tahun Terakhir Ditemukan"))
print("="*123)
#Tampilkan data sesuai format table dg perulangan
for baris in data_fauna:
    print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
kursor.close