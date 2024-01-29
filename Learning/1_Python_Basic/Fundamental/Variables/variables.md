# Python Variable

Pada bagian ini, Anda akan mempelajari tentang Variabel di Python, dan bagaimana menggunakan variabel secara efektif.

## Apa itu varibel di python
Variabel di Python adalah tempat penyimpanan untuk menyimpan nilai atau data. Dengan menggunakan variabel, kita dapat memberikan nama yang mudah diingat untuk merepresentasikan nilai yang disimpan. Contoh penggunaan variabel dalam Python dapat dilihat pada kode berikut:
```python
# Contoh penggunaa variabel di Python
name = 'Sulfikar' # Variabel name dengan nilai 'Sulfikar' (tipe data String) 
age = 17          # Variabel age dengan nilai 17 (tipe data Integer)

# Menampilkan nilai variabel
print('Nama: ', name)
print('Umur: ', age)
```
Output:
```bash
Nama: Sulfikar
Umur: 17
```
dalam contoh diatas, variabel `name` dan `age` digunakan untuk menyimpan informasi tentang seseorang. Variabel-variabel ini kemudian dapat digunakan dan diakses di berbagai bagian dalam program Python.

Nilai pada variabel di Python dapat di ubah sesuai dengan yang dibutuhkan, seperti pada contoh berikut:
```python
message = 'Hello World!'
print(message)

message = 'Good Bye!'
print(message)
```
Pada contoh tersebut, `message` adalah sebuah variable yang memiliki nilai awal `Hello World`, kemudian nilai akan berubah menjadi `Good Bye!` pada baris ke-4.
Anda juga dapat mengubah nilai pada variabel walaupun tipe datanya berbeda,  tetapi <span style="color:red;">*</span>
**disarankan tidak melakukan hal ini, karena bukan cara yang efektif**, contohnya:
```python
age = 17
age = 'tujuh belas'
```
dari pada melakukan seperti itu, anda dapat membuat variable baru untuk nilai yang tipe datamya berbeda seperti pada code berikut:
```python
age = 17
text_age = 'tujuh belas'
```


## Membuat variabel
Untuk mendefinisikan suatu variabel, Anda menggunakan sintaks berikut:
```plaintext
variabel_name = value
```
`=` adalah operator penugasan, Dalam sintaks ini, Anda menetapkan `value` ke `variabel_name`. Nilainya bisa berupa __string__, __number__, dll. Berikut ini contoh mendefiniskan variabel bernama `counter` dan memberikan nilai 1 sebagai valuenya.
```python
counter = 1
```

## Penamaan variabel
Saat anda memberi nama variabel, Anda harus mematuhi beberapa aturan. Jika tidak, Anda akan mendapatkan kesalahan pada kode anda.

Berikut ini adalah aturan variabel yang harus anda ingat:
- Nama variabel hanya boleh berisi huruf, angka, dan garis bawah (`_`). Mereka bisa dimulai dengan huruf atau garis bawah (`_`), bukan dengan angka.
- Nama variabel tidak boleh mengandung spasi. Untuk memisahkan kata dalam variabel, Anda dapat menggunakan garis bawah misalnya `first_name`.
- Nama variabel tidak boleh sama dengan kata kunci, kata cadangan, dan fungsi bawaan di Python.

Berikut cara membuat nama variabel yang baik:
- Nama variabel harus singkat dan deskriptif. Misalnya, `last_name` nama variabelnya lebih deskriptif dibanding `ln`.
- Gunakan garis bawah (`_`) untuk memisahkan beberapa kata dalam nama variabel.
- Hindari penggunaan huruf `l` dan huruf besar `O` karena mirip dengan angka `1` dan `0`.

## Ringkasan
- Variabel adalah label yang dapat anda berikan nilai padanya. Nilai suatu variabel dapat berubah sepanjang program.
- Gunakan `variable_name = value` untuk membuat variabel.
- Nama variabel