# -*- coding: utf-8 -*-


import sqlite3
import os
import datetime
from datetime import datetime

deneme_var = ''



class VeriTabani_yarat():
    'cut.py için gelir ve gider tablo yaratır'
    def __init__(self):
        self.dosya = 'Cut.db'
        self.dosya_mevcut = os.path.exists(self.dosya)
        self.veriTabani_olustur()
        self.tablo_yarat()

    def veriTabani_olustur(self):
        with sqlite3.connect(self.dosya) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()

    def tablo_yarat(self):
        if not self.dosya_mevcut:
            self.im.execute("""CREATE TABLE IF NOT EXISTS Gelir_Tablo
                             (Tarih, Gelir_Türü, Müşteriler, Gelirler)""")
            self.im.execute("""CREATE TABLE IF NOT EXISTS Gider_Tablo
        (tarih,gider_Türu,  gelir)""")
            self.vt.commit()





class VeriTabani():  # TEST = 0

    def __init__(self, gelen_veri):
        self.gelen_veri = gelen_veri
        self.dosya = 'Cut.db'
        self.dosya_mevcut = os.path.exists(self.dosya)
        self.veriTabani_olustur()

    def veriTabani_olustur(self):
        with sqlite3.connect(self.dosya) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            self.veriTabani_kontrol_mekanizmasi()

    def veriTabani_kontrol_mekanizmasi(self):

        if len(self.gelen_veri) == 4:
            self.veriTabanina_gelir_ekle()
        else:
            if len(self.gelen_veri) == 3:
                self.veriTabanina_gider_ekle()

    def veriTabanina_gelir_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Gelir_Tablo
                         (Tarih, Gelir_Türü, Müşteriler, Gelirler)""")
        if not self.dosya_mevcut:
            for veri in self.gelen_veri:
                self.im.execute(
                    """INSERT INTO Gelir_Tablo VALUES(?,?,?,?)""", veri)
                self.vt.commit()
        else:
            self.im.execute("""SELECT * FROM Gelir_Tablo""")
            self.veriler_gelir_hepsi = self.im.fetchall()
##            g1 = [g1 for g1 in self.gelen_veri]
            for veri in [tuple(self.gelen_veri)]:
                if not veri in self.veriler_gelir_hepsi:
                    self.im.execute("""INSERT INTO Gelir_Tablo VALUES(?,?,?,?)""", (veri))

                elif veri in self.veriler_gelir_hepsi:
                    from gelir_ekle import Uyari
                    self.uyari_mesaj = Uyari(2,self.gelen_veri)

            self.sirali_tablo()
            self.vt.commit()



    def sirali_tablo(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Gelir_Tablo (Tarih,Gelir_Türü,Müşteriler,Gelirler) ;""")
        self.im.execute("""INSERT INTO Sirali_Gelir_Tablo ( Tarih, Gelir_Türü, Müşteriler, Gelirler)
                    SELECT *  FROM Gelir_Tablo ORDER BY Tarih ;""")

        self.im.execute("""DROP TABLE Gelir_Tablo ;""")
        self.im.execute("""ALTER TABLE Sirali_Gelir_Tablo RENAME TO Gelir_Tablo;""")
        self.vt.commit()



    def veriTabanina_gider_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Gider_Tablo
    (tarih,gider_Türu,  gelir)""")
        if not self.dosya_mevcut:
            for veri in self.gelen_veri:
                self.im.execute(
                    """INSERT INTO Gider_Tablo VALUES(?, ?, ?)""", veri)
                self.vt.commit()

        else:
            self.im.execute("""SELECT * FROM Gider_Tablo """)
            self.veriler_gider_hepsi = self.im.fetchall()
            for veri in [tuple(self.gelen_veri)]:
                if not veri in self.veriler_gider_hepsi:
                    self.im.execute(
                        """INSERT INTO Gider_Tablo VALUES(?, ?, ?)""", (veri))
                elif veri in self.veriler_gider_hepsi:
                    from gider_ekle import Uyari
                    self.uyari_mesaj = Uyari(2,self.gelen_veri)

            self.sirali_tablo_2()
            self.vt.commit()

    def sirali_tablo_2(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Gider_Tablo (Tarih,Gider_Türü,Giderler) ;""")
        self.im.execute("""INSERT INTO Sirali_Gider_Tablo (Tarih,Gider_Türü,Giderler)
                    SELECT *  FROM Gider_Tablo ORDER BY Tarih ASC;""")

        self.im.execute("""DROP TABLE Gider_Tablo ;""")
        self.im.execute("""ALTER TABLE Sirali_Gider_Tablo RENAME TO Gider_Tablo;""")
        self.vt.commit()



class VeriTabani_2():  # Sadece gelirListeyi işler
    def __init__(self, gelirListe_veri):
        self.gelirListe_veri = gelirListe_veri
        self.fark = []
        self.dosya_2 = 'Cut.db'
        self.dosya_2_mevcut = os.path.exists(self.dosya_2)
        self.veriTabani_2_olustur()

    def veriTabani_2_olustur(self):
        with sqlite3.connect(self.dosya_2) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            self.veriTabanina_gelir_liste_ekle()

    def veriTabanina_gelir_liste_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Gelir_Türü (Gelir_Türü_Liste)""")
        if not self.dosya_2_mevcut:
            for i in self.gelirListe_veri:
                self.im.executemany("""INSERT INTO Tablo_Gelir_Türü VALUES(?)""", (i,))
                self.vt.commit()

        else:


            self.im.execute("""SELECT * FROM Tablo_Gelir_Türü""")
            self.veriler_gelir_hepsi = [r[0] for r in self.im.fetchall()]
            for j in self.gelirListe_veri:
                if not j in self.veriler_gelir_hepsi:
                    if not j in self.fark:
                        self.fark.append(j)
            for jml in self.gelirListe_veri:
                if jml in self.veriler_gelir_hepsi:
                    if not jml in self.fark:
                        self.fark.append(jml)
            self.im.execute("""DELETE FROM Tablo_Gelir_Türü""")
            for K in self.fark:
                self.im.executemany("""INSERT INTO Tablo_Gelir_Türü VALUES (?)""", (K,))
            self.sirali_tablo_3()
            self.vt.commit()


    def sirali_tablo_3(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Tablo_Gelir_Türü
                    (Gelir_Türü_Liste)""")
        self.im.execute("""INSERT INTO Sirali_Tablo_Gelir_Türü(Gelir_Türü_Liste)
                    SELECT *  FROM Tablo_Gelir_Türü ORDER BY Gelir_Türü_Liste ASC;""")
        self.im.execute("""DROP TABLE Tablo_Gelir_Türü ;""")
        self.im.execute("""ALTER TABLE Sirali_Tablo_Gelir_Türü RENAME TO
                         Tablo_Gelir_Türü;""")
        self.vt.commit()



class VeriTabani_2B():
    def __init__(self,musteriler_veri):
        self.musteriler_veri =musteriler_veri
        self.fark_1 = []
        self.dosya_2B = 'Cut.db'
        self.dosya_2B_mevcut = os.path.exists(self.dosya_2B)
        self.veriTabani_2B_olustur()

    def veriTabani_2B_olustur(self):
        with sqlite3.connect(self.dosya_2B) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            self.veriTabanina_musteri_ekle()

    def veriTabanina_musteri_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Müşteriler
                         (Müşteriler_Liste)""")
        if not self.dosya_2B_mevcut:
            for i in self.musteriler_veri:
                self.im.executemany("""INSERT INTO Tablo_Müşteriler VALUES(?)""", (i,))
                self.vt.commit()

        else:
            self.im.execute("""SELECT * FROM Tablo_Müşteriler""")
            self.musteriler_hepsi = [f[0] for f in self.im.fetchall()]
            for j in self.musteriler_veri:
                if not j in self.musteriler_hepsi:
                    if not j in self.fark_1:
                        self.fark_1.append(j)
            for jml in self.musteriler_veri:
                if jml in self.musteriler_hepsi:
                    if not jml in self.fark_1:
                        self.fark_1.append(jml)
            self.im.execute(""" DELETE FROM Tablo_Müşteriler""")
            for JJ in self.fark_1:
                self.im.executemany(
                            """INSERT INTO Tablo_Müşteriler VALUES (?)""",
                    (JJ,))
            self.sirali_tablo_4()
            self.vt.commit()
##

    def sirali_tablo_4(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Tablo_Müşteriler
                    (Müşteriler_Liste)""")
        self.im.execute("""INSERT INTO Sirali_Tablo_Müşteriler(Müşteriler_Liste)
                    SELECT *  FROM Tablo_Müşteriler ORDER BY Müşteriler_Liste ASC;""")
        self.im.execute("""DROP TABLE Tablo_Müşteriler;""")
        self.im.execute("""ALTER TABLE Sirali_Tablo_Müşteriler RENAME TO
                         Tablo_Müşteriler;""")
        self.vt.commit()

def veriTabani_2B_listeler():
    'müşteriler  listesi'
    with sqlite3.connect('Cut.db') as vt:
        vt.text_factory = str
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Müşteriler
                         (Müşteriler_Liste)""")
        im.execute("""SELECT * FROM Tablo_Müşteriler""")
        musteriler_vt2B= [r[0] for r in im.fetchall()]
        vt.commit()

        im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Gelir_Türü
                         (Gelir_Türü_Liste)""")
        im.execute("""SELECT * FROM Tablo_Gelir_Türü""")
        gelirliste_icerik_vt4 = [r[0] for r in im.fetchall()]
        from gelir_ekle import Postaci
        posta_elemani = Postaci(gelirliste_icerik_vt4,musteriler_vt2B)
        vt.commit()

class VeriTabani_2C():
    'silinen liste nesnelerini yedekler'
    def __init__(self,*args):
        self.gelen_veri = [*args]
        self.sil = [*args][0]
        self.sil1 = [*args][1]
        self.fark_1 = []
        self.dosya_2C = 'Cut.db'
        self.dosya_2C_mevcut = os.path.exists(self.dosya_2C)
        self.vt_2C_olustur()

    def vt_2C_olustur(self):
        with sqlite3.connect(self.dosya_2C) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            if self.sil == 1:
                self.gelir_turu_ekle()
            elif self.sil == 2:
                self.musteri_ekle()
            elif self.sil == 3:
                self.gider_ekle()

    def gelir_turu_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Gelir_Tablo_Arşiv
                         (Gelir_Arşiv)""")
        if not self.dosya_2C_mevcut:
            self.im.execute("""INSERT INTO Gelir_Tablo_Arşiv VALUES(?)""",
                            (self.sil1))
            self.vt.commit()
        else:
            self.im.execute("""SELECT * FROM Gelir_Tablo_Arşiv where
                            Gelir_Arşiv = (?)""",(self.sil1,))
            self.goster = self.im.fetchone()
            if self.goster:
                return None
            else:
                self.im.execute("""INSERT INTO Gelir_Tablo_Arşiv VALUES(?)""",
                                (self.sil1,))
            self.siralanmis_gelir_arsiv()
            self.vt.commit()

    def siralanmis_gelir_arsiv(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Gelir_Tablo_Arşiv
                    (Gelir_Arşiv)""")
        self.im.execute("""INSERT INTO Sirali_Gelir_Tablo_Arşiv(Gelir_Arşiv)
                    SELECT *  FROM Gelir_Tablo_Arşiv ORDER BY Gelir_Arşiv ASC;""")
        self.im.execute("""DROP TABLE Gelir_Tablo_Arşiv;""")
        self.im.execute("""ALTER TABLE Sirali_Gelir_Tablo_Arşiv RENAME TO
                         Gelir_Tablo_Arşiv;""")
        self.vt.commit()


    def musteri_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Musteri_Tablo_Arşiv
                         (Musteri_Arşiv)""")
        if not self.dosya_2C_mevcut:
            for i in self.gelir_args:
                self.im.execute("""INSERT INTO Musteri_Tablo_Arşiv VALUES(?)""",
                                (i,))
                self.vt.commit()
        else:
            self.im.execute("""SELECT * FROM Musteri_Tablo_Arşiv where Musteri_Arşiv = (?)""",
                            (self.sil1,))
            self.goster = self.im.fetchone()
            if self.goster:
                return None
            else:
                self.im.execute("""INSERT INTO Musteri_Tablo_Arşiv VALUES (?)""",
                    (self.sil1,))
            self.siralanmis_Musteri_arsiv()
            self.vt.commit()

    def siralanmis_Musteri_arsiv(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Musteri_Tablo_Arşiv
                    (Musteri_Arşiv)""")
        self.im.execute("""INSERT INTO Sirali_Musteri_Tablo_Arşiv(Musteri_Arşiv)
                    SELECT *  FROM Musteri_Tablo_Arşiv ORDER BY Musteri_Arşiv ASC;""")
        self.im.execute("""DROP TABLE Musteri_Tablo_Arşiv;""")
        self.im.execute("""ALTER TABLE Sirali_Musteri_Tablo_Arşiv RENAME TO
                         Musteri_Tablo_Arşiv;""")
        self.vt.commit()

    def gider_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Gider_Tablo_Arşiv
                         (Gider_Arşiv)""")
        if not self.dosya_2C_mevcut:
            for i in self.gelir_args:
                self.im.execute("""INSERT INTO Gider_Tablo_Arşiv VALUES(?)""", (i,))
                self.vt.commit()
        else:
            self.im.execute("""SELECT * FROM Gider_Tablo_Arşiv where Gider_Arşiv = (?)""",
                           (self.sil1,))
            self.goster = self.im.fetchone()
            if self.goster:
                return None
            else:
                self.im.execute("""INSERT INTO Gider_Tablo_Arşiv VALUES (?)""",
                    (self.sil1,))
            self.siralanmis_Gider_arsiv()
            self.vt.commit()

    def siralanmis_Gider_arsiv(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Sirali_Gider_Tablo_Arşiv
                    (Gider_Arşiv)""")
        self.im.execute("""INSERT INTO Sirali_Gider_Tablo_Arşiv(Gider_Arşiv)
                    SELECT *  FROM Gider_Tablo_Arşiv ORDER BY Gider_Arşiv ASC;""")
        self.im.execute("""DROP TABLE Gider_Tablo_Arşiv;""")
        self.im.execute("""ALTER TABLE Sirali_Gider_Tablo_Arşiv RENAME TO
                         Gider_Tablo_Arşiv;""")
        self.vt.commit()

class VeriTabani_2D():
    'silinen liste nesnelerini yedekler'
    def __init__(self,*args):
        self.gelen_veri = [*args]
        self.sil = [*args][0]
        self.sil1 = [*args][1]
        self.fark_1 = []
        self.dosya_2D = 'Cut.db'
        self.dosya_2D_mevcut = os.path.exists(self.dosya_2D)
        self.vt_2D_olustur()

    def vt_2D_olustur(self):
        with sqlite3.connect(self.dosya_2D) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            if self.sil == 1:
                self.gelir_turu_ara()
            elif self.sil == 2:
                self.musteri_ara()
            elif self.sil == 3:
                self.gider_ara()

    def gelir_turu_ara(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Gelir_Tablo_Arşiv
                         (Gelir_Arşiv)""")
        self.im.execute("""DELETE  FROM Gelir_Tablo_Arşiv where
                        Gelir_Arşiv = (?)""",(self.sil1,))
        self.vt.commit()


    def musteri_ara(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Musteri_Tablo_Arşiv
                         (Musteri_Arşiv)""")
        self.im.execute("""DELETE  FROM Musteri_Tablo_Arşiv where
                        Musteri_Arşiv = (?)""",(self.sil1,))
        self.vt.commit()


    def gider_ara(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Gider_Tablo_Arşiv
                         (Gider_Arşiv)""")
        self.im.execute("""DELETE  FROM Gider_Tablo_Arşiv where
                        Gider_Arşiv = (?)""",(self.sil1,))
        self.vt.commit()




class VeriTabani_3():
    'gider listesi'

    def __init__(self, giderListe_veri):
        self.giderListe_veri = giderListe_veri
        self.fark_3 = []
        self.dosya_3 = 'Cut.db'
        self.dosya_3_mevcut = os.path.exists(self.dosya_3)
        self.veriTabani_3_olustur()

    def veriTabani_3_olustur(self):
        with sqlite3.connect(self.dosya_3) as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            self.veriTabanina_gider_liste_ekle()

    def veriTabanina_gider_liste_ekle(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Gider_Türü
                         (Gider_Türu_Liste)""")
        if not self.dosya_3_mevcut:
            for c in self.giderListe_veri:
                self.im.executemany("""INSERT INTO Tablo_Gider_Türü VALUES(?)""",
                                    (c,))
                self.vt.commit()

        else:
            self.im.execute("""SELECT * FROM Tablo_Gider_Türü""")
            self.veriler_gider_hepsi = [f[0] for f in self.im.fetchall()]
            for j in self.giderListe_veri:
                if not j in self.veriler_gider_hepsi:
                    if not j in self.fark_3:
                        self.fark_3.append(j)
            for kml in self.giderListe_veri:
                if kml in self.veriler_gider_hepsi:
                    if not kml in self.fark_3:
                        self.fark_3.append(kml)
            self.im.execute("""DELETE FROM Tablo_Gider_Türü""")
            for KK in self.fark_3:
                self.im.executemany("""INSERT INTO Tablo_Gider_Türü VALUES (?)""",
                                    (KK,))
            self.sirali_tablo_5()
            self.vt.commit()

    def sirali_tablo_5(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS
        Sirali_Tablo_Gider_Türü (Gider_Türu_Liste)""")
        self.im.execute("""INSERT INTO Sirali_Tablo_Gider_Türü (Gider_Türu_Liste)
                    SELECT *  FROM Tablo_Gider_Türü ORDER BY Gider_Türu_Liste ASC;""")
        self.im.execute("""DROP TABLE Tablo_Gider_Türü;""")
        self.im.execute("""ALTER TABLE Sirali_Tablo_Gider_Türü RENAME TO
                         Tablo_Gider_Türü;""")
        self.vt.commit()





def veriTabani_4_giderliste_olustur():
    with sqlite3.connect('Cut.db') as vt:
        vt.text_factory = str
        im = vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Gider_Türü
                         (Gider_Türu_Liste)""")
        im.execute("""SELECT * FROM Tablo_Gider_Türü""")
        giderliste_icerik_vt4 = [s[0] for s in im.fetchall()]
        from gider_ekle import Postaci
        posta_elemani = Postaci(giderliste_icerik_vt4)
        vt.commit()





#def vt3_gelirListe_Hepsi_sil():  # isim düzelt!!!
#    with sqlite3.connect('Cut.db') as vt:
#        im = vt.cursor()
#        im.execute("""DELETE FROM liste_Gider_Türü""")
#        vt.commit()


class VeriTabani_5():
    'kayitlar'
    def __init__(self,Tablo,*args):
        self.Tablo = Tablo
        self.limit = [*args][0]
        self.limit_2 = [*args][1]
        self.limit_3 =[*args][2]
        self.limit_4 = [*args][3]
        self.limit_5 = [*args][4]
        self.limit_6 = [*args][5]
        self.limit_7 = [*args][6]
        self.tablo_silici = [*args][7]
        self.var1 = 0
        self.var_2 = int(datetime.today().strftime('%m'))
        self.son = datetime.today().strftime('%Y.%m.%d')
        self.ilk = datetime.today().replace(day=1,
                month=self.limit_2,
                year=self.limit_3).strftime('%Y.%m.%d')
        self.genel_tablom = []
        self.liste1 = []
        self.liste2 = []
        self.liste3 = []
        self.vt6_calistir = False
        self.spesifik_aralik_tek = False
        self.veriTabani_5_olustur()

    def veriTabani_5_olustur(self):
        with sqlite3.connect('Cut.db') as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            self.vt5_param_kntrl()

    def tarihler_kontrol(self):
        'limit ve limit_7 yi kontrol eder'
        if isinstance(self.limit,(str))\
           and isinstance(self.limit_7,(int)):
              self.ilk = self.limit
              self.spesifik_aralik_tek = True
        elif isinstance(self.limit,(str))\
                and isinstance(self.limit_7,(str)):
                  self.ilk = self.limit
                  self.son = self.limit_7
                  self.spesifik_aralik_tek = False


    def vt5_param_kntrl(self):
        if isinstance(self.limit,(int))\
            and isinstance(self.limit_4, (int))\
            and isinstance(self.limit_5,(int))\
            and isinstance(self.limit_6,(int)):
            return self.vt5_tablolar()
        elif isinstance(self.limit,(str))\
            and isinstance(self.limit_4, (int))\
            and isinstance(self.limit_5,(int))\
            and isinstance(self.limit_6,(int)):
            return self.vt5_spesifik_araliklar()
        elif isinstance(self.limit_4, (str))\
                and isinstance(self.limit_5,(int)):
                  return self.vt5_gelir_turu()
        elif isinstance(self.limit_4, (int))\
                and isinstance(self.limit_5,(int))\
                and isinstance(self.limit_6,(str)):
                  return self.vt5_gider_turu()
        elif isinstance(self.limit_5, (str))\
                and isinstance(self.limit_4,(int)):
                  return self.vt5_musteriler()
        elif isinstance(self.limit_4,(str))\
            and isinstance(self.limit_5,(str)):
              return self.vt5_gelir_param()
        elif isinstance(self.limit_5,(str))\
                and isinstance(self.limit_6,(str))\
                and isinstance(self.limit_4,(float)):
                  return self.vt5_gelir_param2()
        

    def vt5_tablolar(self):
        if self.Tablo == 'Gelir Tablo':
            return self.veriTabani_5_Gelir_Tablo()
        elif self.Tablo == 'Gider Tablo':
            return self.veriTabani_5_Gider_Tablo()

    def vt5_spesifik_araliklar(self):
        if self.Tablo == 'Gelir Tablo':
            self.vt5_spcf_gelir()
        elif self.Tablo == 'Gider Tablo':
            self.vt5_spcf_gider()

    def vt5_spcf_gelir(self):
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Tarih = (?);""",(self.ilk,))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gelir_Tablo where Tarih =(?);""",(self.ilk,))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Tarih >= (?)
                                AND Tarih <= (?);""",(self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gelir_Tablo where Tarih >= (?) AND Tarih <= (?) ;""",(self.ilk,self.son))
        self.veriler_gelir_hepsi_spcfk = [i for i in self.im]
        from kayitlar import Postaci
        self.posta3_sinif = Postaci(self.veriler_gelir_hepsi_spcfk[::-1])
        self.vt.commit()

    def vt5_spcf_gider(self):
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gider_Tablo where Tarih = (?);""",(self.ilk,))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gider_Tablo where Tarih =(?);""",(self.ilk,))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gider_Tablo where Tarih >= (?)
                                AND Tarih <= (?);""",(self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gider_Tablo where Tarih >= (?) AND Tarih <= (?) ;""",(self.ilk,self.son))
        self.veriler_gelir_hepsi_spcfk = [i for i in self.im]
        from kayitlar import Postaci
        self.posta3_sinif = Postaci(self.veriler_gelir_hepsi_spcfk[::-1])
        self.vt.commit()


    def veriTabani_5_Gelir_Tablo(self):
        'aylık gelir tablo'
        self.im.execute(""" select * from Gelir_Tablo
        where Tarih >= (?) AND  Tarih <= (?) ;""",(self.ilk,self.son))

        self.veriler_gelir_hepsi = [s for s in self.im]

        from kayitlar import Postaci
        self.posta_sinif = Postaci(self.veriler_gelir_hepsi[::-1])
        self.vt.commit()

    def veriTabani_5_Gider_Tablo(self):
        'aylık gider tablo'
        self.im.execute(""" select * from Gider_Tablo
        where Tarih >= (?) AND  Tarih <= (?) ;""",(self.ilk,self.son))
        self.veriler_gider_hepsi = [ss for ss in self.im]
        from kayitlar import Postaci
        self.posta2_sinif = Postaci(self.veriler_gider_hepsi[::-1])
        self.vt.commit()
        pass

    def vt5_gelir_turu(self):
        'gelir Turu'
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Gelir_Türü =(?)
                                AND Tarih = (?);""",(self.limit_4,self.ilk))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gelir_Tablo where Gelir_Türü = (?)
                AND Tarih = (?) ;""",(self.limit_4,self.ilk))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Gelir_Türü =
                                (?) AND Tarih >= (?) AND Tarih <=
                                (?);""",(self.limit_4,self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gelir_Tablo where Gelir_Türü = (?)
                AND Tarih >= (?) AND  Tarih <= (?) ;""",(self.limit_4,self.ilk,self.son))

        self.veriler_gelir_hepsi_vt5A = [i for i in self.im]
        from kayitlar import Postaci
        self.posta3_sinif = Postaci(self.veriler_gelir_hepsi_vt5A[::-1])
        self.vt.commit()


    def vt5_musteriler(self):
        'Müşteriler'
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute(""" delete from Gelir_Tablo where Müşteriler = (?)
                AND Tarih = (?);""",(self.limit_5,self.ilk))
                self.vt.commit()
                return None
            else: 
                self.im.execute(""" select * from Gelir_Tablo where Müşteriler = (?)
            AND Tarih = (?);""",(self.limit_5,self.ilk))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute(""" delete from Gelir_Tablo where Müşteriler = (?)
                AND Tarih >= (?) AND  Tarih <= (?) ;""",(self.limit_5,self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gelir_Tablo where Müşteriler = (?)
                AND Tarih >= (?) AND  Tarih <= (?) ;""",(self.limit_5,self.ilk,self.son))


        self.veriler_gelir_hepsi_vt5B = [i for i in self.im]
        from kayitlar import Postaci
        self.posta4_sinif = Postaci(self.veriler_gelir_hepsi_vt5B[::-1])
        self.vt.commit()


    def vt5_gelir_param(self):
        'Gelir Türü ve Müşteriler , Gelir Türü öncelikli.'
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Gelir_Türü = (?)
                                AND Müşteriler = (?) AND Tarih = (?);""",(self.limit_4,
                                                                             self.limit_5,
                                                                             self.ilk))
                self.vt.commit()
                return None
            else:
                self.im.execute("""select * from Gelir_Tablo where Gelir_Türü = (?)
                                AND Müşteriler = (?) AND Tarih = (?);""",(self.limit_4,
                                                                             self.limit_5,
                                                                             self.ilk))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Gelir_Türü = (?)
                                AND Müşteriler = (?) AND Tarih >= (?)
                                AND Tarih <=(?);""",(self.limit_4,self.limit_5,
                                                     self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute("""select * from Gelir_Tablo where Gelir_Türü = (?)
                                AND Müşteriler = (?) AND Tarih >= (?)
                                AND Tarih <=(?);""",(self.limit_4,self.limit_5,
                                                     self.ilk,self.son))

        self.veriler_gelir_hepsi_vt5C = [i for i in self.im]
        from kayitlar import Postaci
        self.posta5_sinif = Postaci(self.veriler_gelir_hepsi_vt5C[::-1])
        self.vt.commit()
        pass

    def vt5_gelir_param2(self):
        'Gelir Türü ve Müşteriler , Müşteriler öncelikli.'
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Müşteriler= (?)
                                AND Gelir_Türü = (?) AND Tarih = (?);""",(self.limit_5,
                                                                            self.limit_6,
                                                                            self.ilk))
                self.vt.commit()
                return None
            else:
                self.im.execute("""select * from Gelir_Tablo where Müşteriler= (?)
                                AND Gelir_Türü = (?) AND Tarih = (?);""",(self.limit_5,
                                                                            self.limit_6,
                                                                            self.ilk))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute("""delete from Gelir_Tablo where Müşteriler= (?)
                                AND Gelir_Türü = (?) AND Tarih >= (?)
                                AND Tarih <=(?);""",(self.limit_5,self.limit_6,
                                                     self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute("""select * from Gelir_Tablo where Müşteriler= (?)
                                AND Gelir_Türü = (?) AND Tarih >= (?)
                                AND Tarih <=(?);""",(self.limit_5,self.limit_6,
                                                     self.ilk,self.son))

        self.veriler_gelir_hepsi_vt5C = [i for i in self.im]
        from kayitlar import Postaci
        self.posta5_sinif = Postaci(self.veriler_gelir_hepsi_vt5C[::-1])
        self.vt.commit()
        pass

    def vt5_gider_turu(self):
        'Gider_Türü'
        self.tarihler_kontrol()
        if self.spesifik_aralik_tek:
            if bool(self.tablo_silici) == True:
                self.im.execute(""" delete from Gider_Tablo where Gider_Türü = (?)
                AND Tarih = (?);""",(self.limit_6,self.ilk))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gider_Tablo where Gider_Türü = (?)
                AND Tarih = (?);""",(self.limit_6,self.ilk))
        else:
            if bool(self.tablo_silici) == True:
                self.im.execute(""" delete from Gider_Tablo where Gider_Türü = (?)
                AND Tarih >= (?) AND Tarih <= (?);""",(self.limit_6,self.ilk,self.son))
                self.vt.commit()
                return None
            else:
                self.im.execute(""" select * from Gider_Tablo where Gider_Türü = (?)
                AND Tarih >= (?) AND Tarih <= (?);""",(self.limit_6,self.ilk,self.son))

        self.veriler_gider_parametre = [ kk for kk in self.im]
        from kayitlar import Postaci
        self.posta6_sinif = Postaci(self.veriler_gider_parametre[::-1])
        self.vt.commit()
        pass


class VeriTabani_6():
    'arşiv listeleri için '
    def __init__(self):
        self.vt6()


    def vt6(self):
        with sqlite3.connect('Cut.db') as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()

            self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Gelir_Türü
                                 (Gelir_Türü_Liste)""")
            self.im.execute("""SELECT * FROM Tablo_Gelir_Türü""")
            self.g_liste= [r[0] for r in self.im.fetchall()]

            self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Müşteriler
                                  (Müşteriler_Liste)""")
            self.im.execute("""SELECT * FROM Tablo_Müşteriler""")
            self.m_liste= [r[0] for r in self.im.fetchall()]


            self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Gider_Türü
                                 (Gider_Türu_Liste)""")
            self.im.execute("""SELECT * FROM Tablo_Gider_Türü""")
            self.gi_liste = [s[0] for s in self.im.fetchall()]

            self.im.execute("""CREATE TABLE IF NOT EXISTS Gelir_Tablo_Arşiv
                         (Gelir_Arşiv)""")
            self.im.execute("""SELECT * FROM Gelir_Tablo_Arşiv""")
            self.ge_arsh_list = [k[0] for k in self.im.fetchall()]

            self.im.execute("""CREATE TABLE IF NOT EXISTS Musteri_Tablo_Arşiv
                             (Musteri_Arşiv)""")
            self.im.execute("""SELECT * FROM Musteri_Tablo_Arşiv""")
            self.m_arsh_list = [p[0] for p in self.im.fetchall()]
            self.im.execute("""CREATE TABLE IF NOT EXISTS Gider_Tablo_Arşiv
                             (Gider_Arşiv)""")
            self.im.execute("""SELECT * FROM Gider_Tablo_Arşiv""")
            self.gi_arsh_list = [t[0] for t in self.im.fetchall()]
            self.vt.commit()




            from kayitlar import Postaci2
            posta_elemani = Postaci2(self.g_liste,
                                     self.m_liste,self.gi_liste,
                                    self.ge_arsh_list,self.m_arsh_list,
                                    self.gi_arsh_list)

class VeriTabani_7():
    'butonların iki kere açılmasını kontrol eder'
    def __init__(self,*args):
        self.veri = [*args][0]
        self.veri2 = [*args][1]
        self.veri3 = 'veri yok'
        with sqlite3.connect('Cut.db') as self.vt:
            self.vt.text_factory = str
            self.im = self.vt.cursor()
            self.im.execute("""CREATE TABLE IF NOT EXISTS Tablo_Acik_Button
                                 (Button_Liste)""")
        if self.veri == 0:
            self.vt7_kapan()
        elif self.veri ==1:
            self.vt7()
        elif self.veri ==2:
            self.vt7_modul_kapa()


    def vt7(self):
            self.im.execute("""SELECT * FROM Tablo_Acik_Button where
                            Button_Liste = (?);""",(self.veri2,))

            self.goster = self.im.fetchone()
            if self.goster:
                from cut import Main_veriTabani
                self.yollanan = Main_veriTabani(self.veri2)
            else:
                from cut import Main_veriTabani
                self.yollanan = Main_veriTabani(self.veri3)
                self.im.execute("""INSERT INTO Tablo_Acik_Button VALUES(?)""",
                                (self.veri2,))

            self.vt.commit()


    def vt7_modul_kapa(self):
        self.im.execute("""DELETE From Tablo_Acik_Button where
                        Button_Liste=(?);""",(self.veri2,))
        self.vt.commit()


    def vt7_kapan(self):
        self.im.execute("""DELETE FROM Tablo_Acik_Button;""")
        self.vt.commit()

        

