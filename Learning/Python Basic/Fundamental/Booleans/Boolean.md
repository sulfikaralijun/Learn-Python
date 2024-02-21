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
```bash
>>> 20 > 10
True
>>> 20 < 10
False
```
Selain itu, membandingkan dua string menghasilkan nilai boolean:
```bash
>>> 'a' < 'b'
True
>>> 'a' > 'b'
False
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
Seperti yang dapat Anda lihat dengan jelas dari keluaran, beberapa nilai bernilai `True` dan nilai lainnya bernilai `False`.

## Nilai-nilai yang Salah dan Benar
Ketika suatu nilai dievaluasi menjadi `True`, itu benar. Dan jika suatu nilai bernilai `False`, itu salah.

Berikut ini adalah nilai-nilai salah di Python:
- Angka nol (`0`)
- String Kosong `''`
- `False`
- `None`
- List kosong `[]`
- Tuple kosong `()`
- Dictionary kosong `{}`
Nilai-nilai yang benar adalah nilai-nilai lain yang tidak salah.

**Perhatikan bahwa Anda akan mempelajari lebih lanjut tentang `None`, `list`, `tuple`, dan `dictionary` dalam tutorial mendatang.**

## Ringkasan
- Tipe data boolean Python memiliki dua nilai: `True` dan `False`.
- Gunakan fungsi `bool()` untuk menguji apakah suatu nilai adalah `True` atau `False`.
- Nilai yang salah bernilai `False`, sedangkan nilai yang benar bernlai `True`.
- Nilai yang salah adalah angka nol, string kosong, False, None, List kosong, Tuple kosong, dan