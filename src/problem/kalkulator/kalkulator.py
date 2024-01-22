print("======= KALKULATOR ========")

# mengambil input angka pertama
angka_pertama = int(input("Masukkan angka pertama: "))

# mengambil input angka kedua
angka_kedua = int(input("Masukkan angka kedua: "))

# mengambil
jenis_operasi = int(input("""Pilih operasi yang anda inginkan:
1. Penjumlah
2. Pengurangan
3. Perkalian
4. Pembagian

Masukkan nomor operasi yang anda inginkan (1/2/3/4): """))
  
if jenis_operasi == 1 :
  hasil = angka_pertama + angka_kedua
elif jenis_operasi == 2 :
  hasil = angka_pertama - angka_kedua
elif jenis_operasi == 3 :
  hasil = angka_pertama * angka_kedua
elif jenis_operasi == 4 :
  hasil = angka_pertama / angka_kedua
else:
  print("Operasi yang anda pilih tidak tersedia")
print(f"Hasil : {hasil}")