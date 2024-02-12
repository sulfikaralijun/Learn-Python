# Python Numbers

Dalam materi ini, Anda akan belajar tentang angka di Python dan cara menggunakannya dalam program.
Python mendukung `integers`, `floats`, dan bilangan `complex`. Materi ini hanya membahas integers dan floats.

## Integers (Bilangan Bulat)
Bilangan bulat adalah bilangan seperti -2, -1, 0, 1, 2, dan 3 dan bertipe `int`.
Anda dapat meggunakan operator Matematika seperti `+`, `-`, `*`, dan `/` untuk membentuk ekspresi yang menyertakan bilangan bulat. Misalnya: 
```bash
>>> 20 + 10
30
>>> 20 - 10
10
>>> 20 * 10
200
>>> 20 / 10
2.0
```
Untuk menghitung eksponen, Anda menggunakan dua simbol perkalian (`**`). Misalnya:
```bash
>>> 3 ** 3
27
```
Untuk mengubah urutan operasi, Anda menggunakan tanda kurung `()`. Misalnya:
```bash
>>> 20 / (10 + 10)
1.0
```

## Floats (Bilangan Desimal)
Bilangan apa pun yang memiliki koma desimal adalah bilangan floating-point. Istilah float berarti titik desimal dapat muncul di posisi mana pun dalam suatu bilangan.
Secara umum, Anda dapat menggunakan float seperti bilangan bulat. Misalnya:
```bash
>>> 0.5 + 0.5
1.0
>>> 0.5 - 0.5
0.0
>>> 0.5 / 0.5
1.0
>>> 0.5 * 0.5
0.25
```
Pembagian dua bilangan bulat selalu menghasilkan float:
```bash
>>> 20 / 10
2.0
```
Jika Anda mencampur bilangan bulat dan float dalam operasi aritmatika apa pun, hasilnya adalah float:
```bash
>>> 1 + 2.0
3.0
```
Karena representasi internal dari float, Python akan mencoba merepresentasikan
hasilnya setepat mungkin. Namun, Anda mungkin mendapatkan hasil yang tidak Anda
harapkan. Misalnya:
```bash
>>> 0.1 + 0.2
0.30000000000000004
```
Ingatlah hal ini saat Anda melakukan penghitungan dengan float. Dan Anda akan
mempelajari cara menangani situasi seperti ini di tutorial selanjutnya.

## Garis bawah dalam angka
Jika angkanya besar, akan sulit dibaca. Misalnya:
```bash
count = 10000000000