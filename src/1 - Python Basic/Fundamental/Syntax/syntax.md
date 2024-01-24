# Python Syntax
Python adalah bahasa pemrograman yang menggunakan whitespace (spasi, tab,
indentasi) untuk menentukan struktur kode. Hal ini berbeda dari banyak bahasa
pemrograman lain yang menggunakan tanda baca seperti semicolon (;)***sebenarnya
bisa menggunakan semicolon**.

## Whitespace and Indentation

Jika Anda pernah bekerja dalam bahasa pemrograman lain seperti `Java`, `C#`, atau `C`/`C++`, Anda pasti tahu bahwa bahasa-bahasa ini menggunakan titik koma (`;`) untuk memisahkan pernyataan.

Namun, Python menggunakan `whitespace` dan `indentation` untuk membangun struktur kode.
Perhatikan cuplikan code python berikut:
```python
def main():
  i = 1
  while i < 10:
    print(i)
    i += 1

main()
```
Makna dari kode tersebut tidak terlalu penting untuk Anda saat ini. Yang perlu diperhatikan adalah bagaimana struktur kodenya dibuat.

Di setiap baris, tidak ada penggunaan titik koma untuk mengakhiri pernyataan. Selain itu, kita menggunakan indentasi untuk memberi tahu komputer cara menyusun kodenya.

Kelebihan penggunaan lekukan dan spasi dalam menulis kode Python adalah:
- Tidak perlu khawatir melewatkan awal atau akhir bagian tertentu dari kode. Ini berbeda dengan bahasa pemrograman lain seperti `Java` atau `C#`.
- Gaya penulisan kodenya tetap konsisten. Jika Anda bekerja bersama developer lain, kodenya akan terlihat sama seperti milik Anda.
- Kode menjadi lebih mudah dibaca dan jelas, dibandingkan dengan bahasa pemrograman lain.

## Comments

Comments digunakan untuk menjelaskan kode. Ketika Python interpreter mengeksekusi kode, ia mengabaikan komentar. Comments dimulai dengan tanda pagar
(`#`). Misalnya, kode berikut:
```python
# Ini adalah komentar satu baris

# Ini adalah komentar multi baris
# yang terbentang
# lebih dari satu baris
```

## Continuation of statements

Statements (pernyataan) di Python dapat terbentang lebih dari satu baris. Hal
ini dilakukan dengan menggunakan karakter backslash (`\`). Misalnya, pada kode berikut:
```python
if a == True and b == False and \
    c == True:
  print("Continuation of statements")
```
Kode tersebut akan mencetak "Continuation of statements" jika `a` dan `c` bernilai
`True`.

## Keywords

Keywords adalah kata-kata yang memiliki arti khusus dalam bahasa pemrograman
Python. Misalnya, `def` digunakan untuk mendefinisikan fungsi, `while` digunakan
untuk membuat loop, dan `print()` digunakan untuk mencetak teks.
Berikut ini adalah beberapa daftar kata kunci di Python:
```python
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```
Python adalah bahasa yang tumbuh dan berkembang. Jadi kata kuncinya akan terus bertambah dan berubah.
Python menyediakan modul khusus untuk membuat daftar kata kuncinya yang disebut `keyword`.
```python
import keyword

print(keyword.kwlist) 
```
## Identifiers

Identifiers dalam Python adalah nama yang digunakan untuk mengidentifikasi variabel, fungsi, kelas, atau objek lain dalam program. Identifiers sangat penting dalam bahasa pemrograman karena digunakan untuk memberikan nama pada elemen-elemen program sehingga dapat diidentifikasi dan digunakan dengan mudah. Berikut adalah beberapa aturan dan contoh mengenai penggunaan identifiers dalam Python:

### Pendefinisian Identifiers:
- Identifiers dapat terdiri dari huruf (`a-z`, `A-Z`), angka (`0-9`), dan underscore (`_`).
- Nama identifier tidak boleh diawali dengan angka.
- Karakter khusus seperti `@`, `$`, dan `%` tidak diperbolehkan dalam identifier.
- Identifiers bersifat **case-sensitive**, artinya huruf besar dan huruf kecil dianggap berbeda.

### Contoh Identifiers yang Benar:
- `namaVariabel`
- `hitung_jumlah`
- `_nilai`
- `KelasMobil`
```python
# Contoh Identifiers yang Benar
namaVariabel = 20
hitung_jumlah = 8
_nilai = "Halo"
KelasMobil = "Sedan"
```

### Contoh Identifiers yang Salah:
- `123variabel` (diawali dengan angka)
- `nilai@` (mengandung karakter khusus)
- `Variabel Baru` (mengandung spasi)
- `class` (menggunakan kata kunci yang sudah ada)
```python
# Contoh Identifiers yang Salah
123variabel = 15  # Diawali dengan angka
nilai@ = 7        # Mengandung karakter khusus
Variabel Baru = 3 # Mengandung spasi
class = "Python"  # Menggunakan kata kunci yang sudah ada
```

### Pemberian Nama yang Dapat Dimengerti:
- Nama identifier sebaiknya memiliki makna yang jelas dan menggambarkan fungsi atau tujuan dari variabel, fungsi, atau kelas tersebut.
- Gunakan kombinasi kata yang singkat namun bermakna, misalnya `hitung_gaji` untuk variabel yang menyimpan informasi mengenai penggajian.
```python
# Pemberian Nama yang Dapat Dimengerti
hitung_gaji = 5000
nama_pengguna = "JohnDoe"
```

### Camel Case vs. Snake Case:
- Python biasanya menggunakan **snake_case** untuk memberikan nama pada variabel dan fungsi. Contohnya: `nama_depan`, `hitung_total`.
- **CamelCase** juga digunakan terutama dalam penamaan kelas. Contohnya: `KelasMobil`, `HitungGaji`.
```python
# Camel Case untuk Nama Kelas
class KendaraanBermotor:
    def __init__(self, jenis):
        self.jenis = jenis

# Snake Case untuk Variabel dan Fungsi
nama_pengguna = "JohnDoe"
def hitung_total_gaji(gaji_pokok, tunjangan):
    return gaji_pokok + tunjangan
```

## String literals

Python menggunakan tanda kutip tunggal (`'`), ganda (`"`) dan tiga kali lipat (`'''` atau `"""`) untuk menunjukkan string literal.

Pastikan menggunakan tanda kutip yang sama untuk memulai dan mengakhiri string literal, misalnya, jika dimulai dengan tanda kutip tunggal (`'`), gunakan tanda kutip tunggal (`'`) juga untuk mengakhiri.
```python
string_single = 'Ini adalah sebuah string yang menggunakan single quote'
string_double = "Ini adalah string lain yang menggunakan double quote"
string_triple = '''
Ini adalah string,
ini menggunakan triple quote
'''
```

## Kesimpulan

- Python menggunakan `whitespace` (spasi, tab, indentasi) untuk menentukan struktur kode, berbeda dari beberapa bahasa pemrograman yang menggunakan tanda baca seperti semicolon(`;`).
