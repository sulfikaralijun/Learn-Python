# Python Boolean

Dalam tutorial ini, Anda akan belajar tentang tipe data boolean di Python, nilai falsy dan truthy.

## Pengenalan tipe data Boolean
Dalam pemrograman, Anda sering kali ingin memeriksa apakah suatu kondisi benar atau tidak dan melakukan beberapa tindakan berdasarkan hasilnya.

Untuk merepresentasikan benar atau salah, Python memberi Anda tipe data boolean. Nilai booelean memiliki nama teknis sebagai `bool`.

Tipe data boolean memiliki dua nilai: `True` dan `False`.

Perhatikan bahwa nilai boolean `True` dan `False` dimulai dengan huruf kapital (`T`) dan (`F`).

Contoh berikut mendefinisikan dua variabel boolean:
```python
is_active = True
is_admin = False
```
Saat Anda membandingkan dua angka, Python mengembalikan hasilnya sebagai nilai boolean. Misalnya:
```python
print(20 > 10)
print(20 < 10)
```
Output:
```bash
True
False
```
Selain itu, membandingkan dua string menghasilkan nilai boolean:
```bash
>>> 'a' < 'b'
```

## Fungsi bool()
Untuk mengetahui apakah suatu nilai `True` atau `False`, Anda menggunakan `bool()` fungsi tersebut. Misalnya:
```bash
>>> bool('Hi')
True
>>> bool('')
False
>>> bool(100)
True
>>> bool(0)
False
```
Seperti yang dapat Anda lihat dengan jelas dari keluaran,