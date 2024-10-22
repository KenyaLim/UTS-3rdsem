jmlmatkul =input("Masukkan jumlah mata kuliah baru :")
for i in range(int(jmlmatkul)):
    namamatkul = input("Masukkan Nama Matkul : ")
    kode = input("Masukkan Kode Matkul : ")
    jmldosen = input("Masukkan jumlah Dosen : ")
    for i in range(int(jmldosen)):
        nama = input(f"Masukkan Nama Dosen {i+1} : ")
    jmlgrup = input(f"Masukkan jumlah grup : ")
    for i in range(int(jmlgrup)):
        grup =input(f"Masukkan nama grup ke {i+1}: ")
print("===Data berhasil ditambahkan===")
