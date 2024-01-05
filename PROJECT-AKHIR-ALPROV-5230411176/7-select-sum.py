import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()
# ambil data berdasarkan rata-rata gaja AVG() dan SUM()
kursor.execute("SELECT SUM(jml_skrng) FROM fauna")
jumlah_populasi = kursor.fetchone()[0] # ambil data fauna jadikan baris baru dimulai dari indeks 0

print(f"Total populasi hewan langka saat ini:{jumlah_populasi}")

koneksi.close()