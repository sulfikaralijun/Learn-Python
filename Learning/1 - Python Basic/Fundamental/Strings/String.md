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
```
