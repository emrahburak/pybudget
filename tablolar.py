#-*-coding:utf-8-*-

from veriTabani import VeriTabani as dblite
from veriTabani import VeriTabani_2C as dblite_2C
from veriTabani import VeriTabani_2D as dblite_2D

class GelirTablo():
    gelirTuru = []
    #total_gelir = []
    #genel_Musteri_Liste = [] 
    
    def __init__(self,gelir_Item):
        self.gelir_Item = gelir_Item
        self.gelir_tarihi = []
        self.musteriler = []
        self.gelir = []
        self.veriler= []
        self.gelir_turu_ekle()

    @classmethod
    def gelirTuru_sayisi(cls):
        pass        

    def gelir_turu_ekle(self):
        self.gelirTuru.append(self.gelir_Item)
        

    def tarih_gelir_ekle(self,tarih):
        self.gelir_tarihi.append(tarih)
        

    def musteri_ekle(self,musteri):
        self.musteriler.append(musteri)
        

    def gelir_ekle(self,gelir):
        self.gelir.append(gelir)
        
        

    def veriTabanına_yolla(self):
        self.veriler.extend(self.gelir_tarihi)
        self.veriler.append(self.gelir_Item)
        self.veriler.extend(self.musteriler)
        self.veriler.extend(self.gelir)
        self.dbliteCut = dblite(self.veriler)
        
##        self.veriler = []



class GiderTablo():
    giderTuru = []
    
    def __init__(self,gider_Item):
        self.gider_Item = gider_Item
        self.gider_Tarihi = []
        self.gider = []
        self.gider_veriler = []
        self.gider_turu_ekle()

    @classmethod
    def giderTuru_sayisi(cls):
        pass
        

    def gider_turu_ekle(self):
        self.giderTuru.append(self.gider_Item)

    def tarih_gider_ekle(self,tarih):
        self.gider_Tarihi.append(tarih)

    def gider_ekle(self,gider):
        self.gider.append(gider)


    def veriTabanına_yolla(self):
         self.gider_veriler.extend(self.gider_Tarihi)
         self.gider_veriler.append(self.gider_Item)
         self.gider_veriler.extend(self.gider)
         self.gider_dbliteCut = dblite(self.gider_veriler)
        

class G_Arsiv():
    def __init__(self,*args):
        self.gelir_turu = 1
        if [*args][0] == [1]:
            self.yolla_to = dblite_2D(self.gelir_turu,[*args][1])
        elif [*args][0] == [0]:
            self.yolla_to = dblite_2C(self.gelir_turu,[*args][1])
        


class M_Arsiv():
    def __init__(self,*args):
        self.musteri = 2
        if [*args][0] == [1]:
            self.yolla_to2 = dblite_2D(self.musteri,[*args][1])
        elif [*args][0] == [0]:
            self.yolla_to2 = dblite_2C(self.musteri,[*args][1])


class Gider_Arsiv():
    def __init__(self,*args):
        self.gider = 3
        if [*args][0] == [1]:
            self.yolla_to3 = dblite_2D(self.gider,[*args][1])
        elif [*args][0] ==[0]:
            self.yolla_to3 = dblite_2C(self.gider,[*args][1])


