"""
perulangan dengan while sampai paham
"""
jumlah_buku = 10
print('ibu berkata, baca semua bukumu sampai paham')
total_jumlah_baca = 0
jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum di pahami")
    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} yang sudah dibaca dan dpahami')


print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku ')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print (f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, '
          f'Budi hanya bisa memahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')