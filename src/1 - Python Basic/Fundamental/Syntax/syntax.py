# mengimpor module keyword
import keyword

# mendefinisikan fungsi main
def main():
    i = 1
    max = 5
    while (i < max):
        print(i)
        i = i + 1

# memanggil fungsi main
main()

# Ini adalah komentar satu baris

# Ini adalah komentar multi baris
# yang terbentang
# lebih dari satu baris

# Continuation statement
a = True
b = False
c = True
if a == True and b == False and \
    c == True:
  print("Continuation of statements")

# menampilakn keyword yang ada pada python versi sekarang (3.10)
print(keyword.kwlist)

# Contoh Identifiers yang Benar
namaVariabel = 20
hitung_jumlah = 8
_nilai = "Halo"
KelasMobil = "Sedan"

# Contoh Identifiers yang Salah

# (kode ini saya comment karena dapat menyebabkan error)
# 123variabel = 15  # Diawali dengan angka
# nilai@ = 7        # Mengandung karakter khusus
# Variabel Baru = 3 # Mengandung spasi
# class = "Python"  # Menggunakan kata kunci yang sudah ada

# Pemberian Nama yang Dapat Dimengerti
hitung_gaji = 5000
nama_pengguna = "JohnDoe"

# Camel Case untuk Nama Kelas
class KendaraanBermotor:
    def __init__(self, jenis):
        self.jenis = jenis
        
mobil = KendaraanBermotor('Mobil')
print(mobil.jenis)

# Snake Case untuk Variabel dan Fungsi
nama_pengguna = "JohnDoe"
def hitung_total_gaji(gaji_pokok, tunjangan):
    return gaji_pokok + tunjangan

print(nama_pengguna)
gaji_pokok = hitung_total_gaji(1200, 500)
print(gaji_pokok)

# String Literals
string_single = 'Ini adalah sebuah string yang menggunakan single quote'
string_double = "Ini adalah string lain yang menggunakan double quote"
string_triple = '''
Ini adalah string,
ini menggunakan triple quote
'''

print(string_single)
print(string_double)
print(string_triple)