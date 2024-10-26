# Cara Variabel Bekerja

# Variabel adalah sebuah hasil. Kita bisa mengprint hasil yang kita buat berdasarkan jenisnya, terdapat 4 jenis, diantaranya:

# 1.String = Karakter
# untuk string biasanya memakai tanda petik dua
nama_pertama = "Asupan"
nama_kedua = "Syab"
nama = nama_pertama + " " + nama_kedua
print("Halo " + nama)

print("###############")

# 2.Integer = Angka
# Integer bisa memakai fungsi aritmatika sedangkan String tidak
umur = 21
print(umur)
print("Umur saya adalah : " + str(umur))
# Kalian harus mengubah integer kedalam string(str) agar bisa di running bersamaan dengan string(typecasting)
# Jika, print("Umur saya adalah : " + umur), maka hasilnya tidak akan keluar(error)

print("###############")

# 3.Float
# Float bisa menghitung hasil desimal, sementara integer hanya angka asli
tinggi = 160.5
print(tinggi)
print("Tinggi saya adalah : " + str(tinggi))

print("###############")

# 4.Boolean
# Boolean hanya diantara true/false
cinta = False
print(cinta)
print("Apakah kamu masih cinta dia? " + str(cinta))

print("###############")


print("Tipe data dari variabel nama adalah : " + str(type(nama)))
print("Tipe data dari variabel nama adalah : " + str(type(umur)))
print("Tipe data dari variabel nama adalah : " + str(type(tinggi)))
print("Tipe data dari variabel nama adalah : " + str(type(cinta)))
