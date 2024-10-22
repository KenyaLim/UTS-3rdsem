import json

def tambahmatkul():
    with open('matkul.json', 'r') as datafile:
        data = json.load(datafile)

    jmlmatkul = int(input("Masukkan jumlah mata kuliah baru: "))
    for i in range(jmlmatkul):
        matkulbaru = {}  
        
        namamatkul = input("Masukkan Nama Matkul: ")
        kode = input("Masukkan Kode Matkul: ")
        jmldosen = int(input("Masukkan jumlah Dosen: "))

        dosen_list = [] 
        for j in range(jmldosen):
            nama = input(f"Masukkan Nama Dosen {j + 1}: ")
            dosen_list.append(nama)

        jmlgrup = int(input("Masukkan jumlah grup: "))
        grup_list = []
        for k in range(jmlgrup):
            grup = input(f"Masukkan nama grup ke-{k + 1}: ")
            grup_list.append(grup)

        matkulbaru['kode'] = kode
        matkulbaru['dosen'] = dosen_list
        matkulbaru['grup'] = grup_list

        data[namamatkul] = matkulbaru

    with open('matkul.json', 'w') as datafile:
        json.dump(data, datafile, indent=4)

    print("=== Data berhasil ditambahkan ===")

tambahmatkul()
