from Sepatu import Sepatu

class RakSepatu():
    def __init__(self,pemilik,ukuranKaki,slotSepatu,sepatu = []):
        self.pemilik = pemilik
        self.ukuranKaki = ukuranKaki
        self.slotSepatu = slotSepatu
        self.sepatu = sepatu
    def getPemilik(self):
        return self.pemilik
    def getUkuranKaki(self):
        return self.ukuranKaki
    def getSlotSepatu(self):
        return self.slotSepatu
    def getSepatu(self):
        return self.sepatu
    def setPemilik(self,pemilik):
        self.pemilik = pemilik
    def setUkuranKaki(self,ukuranKaki):
        self.ukuranKaki = ukuranKaki
    def setSlotSepatu(self,slotSepatu):
        self.slotSepatu = slotSepatu
    def setSepatu(self,sepatu):
        self.sepatu = sepatu
    def jualSepatu(self,namaSepatu):
        for i in self.sepatu:
            if i.getNama() == namaSepatu:
                self.sepatu.remove(i)
                print (f"Sepatu {namaSepatu} berhasil dijual")
                return
        print (f"Tidak temukan sepatu dengan nama {namaSepatu}")
        return
    def beliSepatu(self,namaSepatu, merek, warna, ukuran, jenis):
        if self.sisaSlotKosong() > 0:
            for i in self.sepatu:
                if i.getNama() == namaSepatu:
                    print (f"Sudah memiliki sepatu dengan nama {namaSepatu}")
                    return
            sepatuBaru = Sepatu(namaSepatu,merek,warna,ukuran,jenis)
            self.sepatu.append(sepatuBaru)
            print (f"Berhasil membeli sepatu {namaSepatu}")
            return
        print (f"Rak sepatu sudah penuh, Gagal membeli sepatu bernama {namaSepatu}")
        return
    def pakaiSepatu(self,namaSepatu):
        for i in self.sepatu:
            if i.getNama() == namaSepatu:
                if i.isMuat(self.ukuranKaki):
                    i.setKondisi("Kotor")
                    print (f"Sepatu {i.getNama()} berhasil dipakai, Sepatu menjadi kotor")
                else:
                    print(f"Ukuran sepatu {i.getNama()} tidak pas, Sepatu tidak dapat digunakan")
                return
        print (f"Tidak temukan sepatu dengan nama {namaSepatu}")
        return
    def cuciSepatu(self,namaSepatu):
        for i in self.sepatu:
            if i.getNama() == namaSepatu:
                if i.getKondisi() == "Baru":
                    print (f"Sepatu {i.getNama()} masih baru")
                elif i.getKondisi() == "Bersih":
                    print(f"Sepatu {i.getNama()} masih bersih")
                else:
                    print (f"Sepatu {i.getNama()} sudah dicuci")
                    i.setKondisi("Bersih")
                return
        print (f"Tidak temukan sepatu dengan nama {namaSepatu}")
        return
    def sisaSlotKosong(self):
        return self.slotSepatu - len(self.sepatu)
    def detailRak(self):
        print (f"""== Rak Sepatu ==
Nama Pemilik \t\t\t: {self.pemilik}
Ukuran Kaki Pemilik \t: {self.ukuranKaki}
Slot Sepatu \t\t\t: {self.slotSepatu}
Sisa Slot Kosong \t\t: {self.sisaSlotKosong()}
""")
        index = 1
        for i in self.sepatu:
            print (f">> Sepatu {index}")
            i.detailSepatu()
            index += 1