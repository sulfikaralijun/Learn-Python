print("======== Selamat datang di kalkulator Sulfikar Alijun ========")

angka_pertama = input("Masukkan angka pertama: ")
angka_kedua = input("Masukkan angka kedua: ")
jenis_operasi = input("""Pilih operasi yang anda inginkan:
1. Penjumlah
2. Pengurangan
3. Perkalian
4. Pembagian

Masukkan nomor operasi yang anda inginkan (1/2/3/4): """)
if jenis_operasi == 1 :
  hasil = angka_pertama + angka_kedua
elif jenis_operasi == 2 :
  hasil = angka_pertama - angka_kedua
elif jenis_operasi == 3 :
  hasil = angka_pertama * angka_kedua
else :
  hasil = angka_pertama / angka_kedua
  
print("Hasil: " + hasil)