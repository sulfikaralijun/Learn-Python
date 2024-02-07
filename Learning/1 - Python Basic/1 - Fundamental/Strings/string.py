# String ditandai dengan tanda kutip, baik itu
# tanda kutip tunggal atau tanda kutip ganda.
message = 'Ini adalah string'
message = "Ini juga adalah sebuah string"

print(message)

# Jika string berisi tanda kutip tunggal, maka gunakan 
# tanda kutip ganda untuk membungkus string, begitupun sebaliknya
message = "It's a string"
message = '"Beautiful is better than ugly.". Said Tim Peters'

print(message)

# Untuk menghindari tanda kutip, anda dapat mengunakan backslash '\'
message = 'It\'s a string'

print(message)

# tambahkan 'r' sebelum string jika ingin membuat semua karakter
# didalam string di anggap sebagai string tanpa pengecualian
path = r'C:\Python\bin'

print(path)

# untuk membuat string dengan beberapa baris, dapata menggunakan kutip 3
help_message = '''
Usage: mysql command
    -h hostname
    -d database name
    -u username
    -p password
'''

print(help_message)

# Gunakan f-string jika ingin menambahkan nilai varibel kedalam variable lain
name = 'John'
greeting = f'Hi {name}'

print(greeting)

# Untuk menggabungkan 2 variabel string, gunakan '+'
greeting = 'Good '