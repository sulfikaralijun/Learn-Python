# Python Syntax
Python adalah bahasa pemrograman yang menggunakan whitespace (spasi, tab,
indentasi) untuk menentukan struktur kode. Hal ini berbeda dari banyak bahasa
pemrograman lain yang menggunakan tanda baca seperti semicolon (;)***sebenarnya
bisa menggunakan semicolon**.

## Whitespace

Whitespace digunakan untuk menentukan blok kode di Python. Misalnya, dalam kode
berikut:
```python
def main():
  i = 1
  while i < 10:
    print(i)
    i += 1

main()
```
Kode tersebut akan mencetak angka dari 1 hingga 9. Blok kode `while` dimulai
dengan spasi 4 karakter dan berakhir dengan spasi 4 karakter.

## Comments

Comments digunakan untuk menjelaskan kode. Comments dimulai dengan tanda pagar
(#). Misalnya, kode berikut:
```python
# Ini adalah komentar satu baris

# Ini adalah komentar multi baris
# yang terbentang
# lebih dari satu baris
```

## Continuation of statements

Statements (pernyataan) di Python dapat terbentang lebih dari satu baris. Hal
ini dilakukan dengan menggunakan karakter backslash (`\`). Misalnya, kode berikut:
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

## Identifiers

Identifiers dalam Python adalah nama yang digunakan untuk mengidentifikasi variabel, fungsi, kelas, atau objek lain dalam program. Identifiers sangat penting dalam bahasa pemrograman karena digunakan untuk memberikan nama pada elemen-elemen program sehingga dapat diidentifikasi dan digunakan dengan mudah. Berikut adalah beberapa aturan dan contoh mengenai penggunaan identifiers dalam Python:

### Pendefinisian Identifiers:
- Identifiers dapat terdiri dari huruf (`a-z`, `A-Z`), angka (`0-9`), dan underscore (`_`).
- Nama identifier tidak boleh diawali dengan angka.
- Karakter khusus seperti `@`, `$`, dan `%` tidak diperbolehkan dalam identifier.
