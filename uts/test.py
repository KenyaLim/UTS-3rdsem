from RakSepatu import RakSepatu

print (">> Inisialisasi Rak")
rakSepatuKu = RakSepatu("Nicho",43,5)

print ("\n>> Tes Beli Sepatu")
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 5
rakSepatuKu.beliSepatu("Court Royale 2", "Nike", "Putih", 42.5, "Sneakers") # Berhasil beli
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 4
rakSepatuKu.beliSepatu("NMD OG", "Addidas", "Hitam", 43, "Running") # Berhasil beli
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 3
rakSepatuKu.beliSepatu("505", "New Balance", "Merah",36,"Sneakers") # Berhasil beli
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 2
rakSepatuKu.beliSepatu("Velocity Nitro", "Puma","Hitam",43.5, "Running") # Berhasil beli
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 1
rakSepatuKu.beliSepatu("Court Royale 2", "Nike", "Hitam", 43, "Sneakers") # Gagal beli, Sudah punya
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 1
rakSepatuKu.beliSepatu("Curry 6","Under Armour","Ungu",46,"Basketball") # Berhasil beli
print (f"Sisa slot kosong : {rakSepatuKu.sisaSlotKosong()}") # 0
rakSepatuKu.beliSepatu("Go Walk 6","Sketchers","Putih",43,"Lifestyle") # Gagal beli, Rak Penuh
print()
rakSepatuKu.detailRak()

print ("\n>> Tes Pakai Sepatu")
rakSepatuKu.pakaiSepatu("Jordan 1 OG") # Sepatu tidak ada
rakSepatuKu.pakaiSepatu("Court Royale 2")# Sepatu berhasil dipakai, Kondisi menjadi kotor
rakSepatuKu.pakaiSepatu("505") # Sepatu tidak muat, Kondisi tetap baru
rakSepatuKu.pakaiSepatu("Velocity Nitro") # Sepatu berhasil dipakai, Kondisi menjadi kotor
print()
rakSepatuKu.detailRak()

print ("\n>> Tes Cuci Sepatu")
rakSepatuKu.cuciSepatu("Dunk Low") # Sepatu tidak ada
rakSepatuKu.cuciSepatu("Court Royale 2") # Menjadi bersih
rakSepatuKu.cuciSepatu("Curry 6") # Sepatu masih baru, tidak perlu dicuci
rakSepatuKu.cuciSepatu("Court Royale 2") # Sepatu masih bersih, tidak perlu dicuci
print()
rakSepatuKu.detailRak()

print ("\n>> Tes Jual Sepatu")
rakSepatuKu.jualSepatu("Court Vision Mid") # Sepatu tidak ada
rakSepatuKu.jualSepatu("Curry 6") # Sepatu terjual
rakSepatuKu.jualSepatu("Curry 6") # Sepatu sudah dijual
rakSepatuKu.beliSepatu("Ultraboost Light","Addidas","Putih", 45,"Running") # Berhasil beli
print()
rakSepatuKu.detailRak()