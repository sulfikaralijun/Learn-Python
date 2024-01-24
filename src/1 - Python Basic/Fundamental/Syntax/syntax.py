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
#123variabel = 15  # Diawali dengan angka (kode ini saya comment karena dapat menyebabkan error)
