# Python String

Dalam tutorial ini, Anda akan belajar tentang string pada Python dan operasi dasarnya.

## Pengantar String Python

String adalah serangkaian karakter. Di Python, apapun didalam tanda kutip adalah string. Dan anada dapat menggunakan singgle quotes atau double quotes. Misalnya:

```python
message = 'This is a string in Python'
message = "This is also a string"
```

jika string berisi singgle quotes, Anda harus menempatkannya dalam double quotes seperti ini:

```python
message = "It's a string"
```

Dan ketika sebuah string berisi double quotes, Anda dapat menggunakan singgle quotes:

```python
message = '"Beautiful is better than ugly.". Said Tim Peters'
```

Untuk menghindari quotes, gunakan backslash (`\`). Misalnya:

```python
message = 'It\'s also a valid string'
```

Interpreter Python akan memperlakukan karakter backslash (`\`) secara khusus. Jika Anda tidak menginginkannya, Anda dapat menggunakan string mentah dengan menambahkan huruf `r` sebelum quotes pertama. Misalnya:

```python
message = r'C:\python\bin'
```

**Membuat string multiline**
untuk merentangkan string beberapa baris, Anda menggunakan triple quotes `"""..."""` atau `"'..."'`. Misalnya:

```python
help_message = '''
Usage: mysql command
    -h : hostname
    -d : database name
    -u : username
    -p : password
'''

print(help_message)
```

Ini akan menampilkan seperti dibawah ini jika Anda menjalankan program:

```bash
Usage: mysql command
    -h : hostname
    -d : database name
    -u : username
    -p : password
```

## Menggunakan variabel dalam string Python dengan f-string

Terkadang, Anda ingin menggunakan nilai [variabel](../Variables/Variables.md) dalam sebuah string.
Misalnya, Anda mungkin ingin menggunakan nilai variabel `name` didalam `message` variabel string:

```python
name = 'John'
message = 'Hi'
```

Untuk melakukannya, letakan huruf `f` sebelum quotes pembuka dan beri tanda kurung kurawal di sekitar nama variabel:

```python
name = 'John'
message = f'Hi {name}'

print(message)
```

Python akan mengganti `{name}` dengan nilai variabel `name`. Kode akan menampilkan yang berikut di layar:

```text
Hi John
```

`message` adalah format string, atau singkatnya f-string. Python memperkenalkan f-string di versi 3.6.

## Menggabungkan String Python

Saat Anda menempatkan string literal disamping satu sama lain, Python secara otomatis menggabungkan menjadi satu string. Misalnya:

```python
greeting = 'Good' 'Morning!'
print(greeting)
```

Output:

```text
Good Morning!
```

Untuk menggabungkan dua variabel string, gunakan operator `+`:

```python
greeting = 'Good'
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)
```

Output:

```text
Good Afternoon!
```

## Mengakses Elemen String

Karena String adalah rangkaian karakter, Anda dapat mengakses elemennya menggunakan indeks. Karakter pertama dalam string memiliki indeks nol.
Contoh berikut menunjukkan cara mengakses elemen menggunakan indeks:

```python
str = "Python String"
print(str[0]) # P
print(str[1]) # Y
```

Bagaimana hal tersebut bekerja:

- Pertama, buat variabel yang menampung string `"Python String"`.
- Kemudian, akses karakter pertama dan kedua dari string dengan menggunakan tanda kurung siku `[]` dan indeks.
  Jika Anda mwnggunakan indeks negatif, Python mengembalikan karakter mulai dari akhir string. Misalnya:

```python
str = 'Python String'
```
