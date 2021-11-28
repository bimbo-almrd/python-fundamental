#sekuensial
print('ibu memberi perintah, "beli 1 botol susu dan beli 6 telur jika ada"')
print('"anak menjawab "ok"')
print('maka budi berangkat ke toko')
print('budi berbelanja')

#percabangan
print('ibu memberi perintah, "beli 1 botol susu dan beli 6 telur jika ada"')
print('"anak menjawab "ok"')
print('maka budi berangkat ke toko')
jumlah_botol_susu = 173
jumlah_telur = 200
print(f"jumlah botol susu {jumlah_botol_susu } btl")
print(f"jumlah telur {jumlah_telur } btr")
if jumlah_botol_susu > 0:
    print("budi membeli satu botol susu")
else:
    print("budi tidak membeli 1 botol susu")
print('budi bertanya ke pemilik toko "apakah ada telur?"')
if jumlah_telur == 0:
    print('budi membeli 1 botol susu dan 6 butir telur')
else:
    print("budi tidak membeli telur")
print('budi pulang ke rumah')
print('budi menyerahkan belanjaan kepada ibu')