"""
perulangan dengan while sampai paham
"""
book_count = 10
print('ibu berkata, baca semua bukumu sampai paham')
read_count = 0

understood_count = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"buku ke {understood_count + 1} belum di pahami")
    else:
        understood_count = understood_count + 1
        print(f'buku ke {understood_count} yang sudah dibaca dan dpahami')


print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count} buku ')
if understood_count == book_count:
    print (f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, '
          f'Budi hanya bisa memahami {understood_count}')