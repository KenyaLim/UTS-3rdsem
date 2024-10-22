class Sepatu:
    def __init__(self, nama, merek, warna, ukuran, jenis, kondisi = "Baru"):
        self.nama = nama
        self.merek = merek
        self.warna = warna
        self.ukuran = ukuran
        self.jenis = jenis
        self.kondisi = kondisi
    def getNama(self):
        return self.nama
    def getMerek(self):
        return self.merek
    def getWarna(self):
        return self.warna
    def getUkuran(self):
        return self.ukuran
    def getJenis(self):
        return self.jenis
    def getKondisi(self):
        return self.kondisi
    def setNama(self, nama):
        self.nama = nama
    def setMerek(self, merek):
        self.merek = merek
    def setWarna(self, warna):
        self.warna = warna
    def setUkuran(self, ukuran):
        self.ukuran = ukuran
    def setJenis(self, jenis):
        self.jenis = jenis
    def setKondisi(self, kondisi):
        self.kondisi = kondisi
    def isMuat(self,ukuranKaki):
        if abs(ukuranKaki - self.ukuran) <= 0.5:
            return True
        else:
            return False
    def detailSepatu(self):
        print (f"""Nama Sepatu \t: {self.nama} 
Merek Sepatu \t: {self.merek} 
Warna Sepatu \t: {self.warna} 
Ukuran Sepatu \t: {self.ukuran} 
Jenis Sepatu \t: {self.jenis} 
Kondisi Sepatu \t: {self.kondisi}\n""")