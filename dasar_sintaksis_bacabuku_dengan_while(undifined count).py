"""
perulangan dengan while sampai paham
"""
jumlah_buku = 10
print('ibu berkata, baca semua bukumu sampai paham')
jumlah_baca = 0

jumlah_baca_paham = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_baca_paham}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_baca_paham == 9:
        print(f"buku ke {jumlah_baca_paham + 1} belum di pahami")
    else:
        jumlah_baca_paham = jumlah_baca_paham + 1
        print(f'buku ke {jumlah_baca_paham} yang sudah dibaca dan dpahami')


print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_baca_paham} buku ')
if jumlah_baca_paham == jumlah_buku:
    print (f'jumlah buku yang sudah dibaca dan dipahami {jumlah_baca_paham}')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, '
          f'Budi hanya bisa memahami {jumlah_baca_paham}')