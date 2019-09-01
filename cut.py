# -*- coding: utf-8 -*-

import sys
import time
import gelir_ekle
import gider_ekle
import araclar
import veriTabani
from kayitlar import Kontrol
#import not_defteri_yedek
from tkinter import *
from tkinter import ttk
#from PIL import ImageTk
from tkinter import font
from datetime import datetime


class Main_veriTabani():
    veri_list = []
    def __init__(self,veri):
        self.veri = veri
        self.veri_list.append(self.veri)
        self.veri = 0

class Main(object):

    def __init__(self):
        self.penGuiAr()
        self.sayac = [] #Input /GelirTablo değişkeni.
        self.gider_sayac = [] #Output /GiderTablo değişkeni.
        self.depo = '' #Tools /makina değişkeni
        self.veriTabani_yarat()

        

    def konum(self,gen,yuks,penc):
        self.pgen = gen
        self.pyuks = yuks
        self.penc = penc



        self.ekrangen = self.penc.winfo_screenwidth()
        self.ekranyuks = self.penc.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 7
        self.y = (self.ekranyuks - self.pyuks) / 2.5

        self.penc.geometry('%dx%d+%d+%d' % (self.pgen, self.pyuks,
                                               self.x, self.y))
        

    def penGuiAr(self):
        self.pencere = Tk()
        self.pencere.tk_setPalette('#9fb6cd')
        self.pencere.resizable(width=FALSE, height=FALSE)
        self.pencere.bind('<Escape>',self.cikis)
        self.pencere.geometry('299x260+30+40')

        self.baslik = self.pencere.title('CUT TASARIM')

        self.cerceve_1 = Frame(self.pencere)
        self.cerceve_1['bd'] = 2
        self.cerceve_1['relief'] = GROOVE
        self.cerceve_1.grid(column=0,row=0,padx=5,pady=5,sticky=NW)
        self.etiket = Label(self.cerceve_1,)
        self.etiket['text'] = 'Cut'
        self.etiket['font'] = 'Courier 27 '
        self.etiket.grid(column=0,row=0,sticky=NW)
 


        self.cerceve_2 = Frame()   # Birinci sıra tuş takımı..
        self.cerceve_2['bd'] = 2
        self.cerceve_2['relief'] = 'groove'
        self.cerceve_2.grid(column=0 ,row=2,pady=5)

        self.menu_liste = [
            'Gelir Ekle', 'Gider Ekle',
            'İzle', 'Veri Tabanı',
            'Not Defteri', 'Araçlar']
        self.sira = 1
        self.sutun = 0

        for i in self.menu_liste:
            self.komut = lambda x=i: self.btns(x)
            self.btn_one = Button(self.cerceve_2)
            self.btn_one['text'] = i
            if sys.platform == 'win32':
                self.btn_one['width'] = 13
            else:
                self.btn_one['width'] = 11
            self.btn_one['height'] = 1
            self.btn_one['relief'] = GROOVE
            self.btn_one['font'] = 'Arial'
            self.btn_one['bg'] = '#e0eeee'
            self.btn_one['fg'] = '#1c1c1c'
            self.btn_one['command'] = self.komut
            self.btn_one.grid(row=self.sira,
                              column=self.sutun,
                              ipadx=8, ipady=2,
                              pady=1, padx=2)
            self.sutun += 1
            if self.sutun > 1:
                self.sutun = 0
                self.sira += 1


        self.cerceve_3 = Frame()   # ikinci sıra tuşlar.
        self.cerceve_3['bd'] = 2
        self.cerceve_3['relief'] = 'groove'
        self.cerceve_3.grid(column=0 ,row=3,pady=5)

        self.menu_liste_2 = ['Bilgilendirme','Çıkış']
        self.sira_2 = 1
        self.sutun_2 = 0

        for p in self.menu_liste_2:
            self.komut_2 = lambda x=p: self.btns_2(x)
            self.btn_two = Button(self.cerceve_3)
            self.btn_two['text'] = p
            if sys.platform == 'win32':
                self.btn_two['width'] = 13
            else:
                self.btn_two['width'] = 11
            self.btn_two['height'] = 1
            self.btn_two['relief'] = GROOVE
            self.btn_two['font'] = 'Arial'
            self.btn_two['bg'] = '#e0eeee'
            self.btn_two['fg'] = '#1c1c1c'
            self.btn_two['command'] = self.komut_2
            self.btn_two.grid(row=self.sira_2,
                              column=self.sutun_2,
                              ipadx=8, ipady=2,
                              pady=1, padx=2)
            self.sutun_2 += 1
            if self.sutun_2 > 1:
                self.sutun_2 = 0
                self.sira_2 += 1

    def btns_kontrol(self):
        from cut import Main_veriTabani
        self.gelen = Main_veriTabani.veri_list
        for i in self.gelen:
            if i == 'Gelir Ekle':
                self.gelir_anahtar = True
            elif i == 'Gider Ekle':
                self.gider_anahtar = True
            elif i == 'Araçlar':
                self.araclar_anahtar = True
            elif i == 'Veri Tabanı':
                self.kayitlar_anahtar = True
            else:
                self.gelir_anahtar = False
                self.gider_anahtar = False
                self.kayitlar_anahtar = False
                self.araclar_anahtar = False


    def btns(self, tus):  # Tuşa basıldığında..
        self.tus = tus
        if self.tus == 'Gelir Ekle':
            self.yolla = veriTabani.VeriTabani_7(1,self.tus)
            self.btns_kontrol()
            if self.gelir_anahtar == False:
                self.gelir = gelir_ekle.Gelir_ekle()


        if self.tus == 'Gider Ekle':
            self.yolla = veriTabani.VeriTabani_7(1,self.tus)
            self.btns_kontrol()
            if self.gider_anahtar == False:
                self.gider = gider_ekle.Gider_ekle()

        if self.tus == 'Araçlar':
            self.yolla = veriTabani.VeriTabani_7(1,self.tus)
            self.btns_kontrol()
            if self.araclar_anahtar == False:
                self.hsp_mk = araclar.Hesap_mk()

        if self.tus == 'Not Defteri':
            return None
           # self.not_def = not_defteri_yedek.defter()

        if self.tus == 'Veri Tabanı':
            self.yolla = veriTabani.VeriTabani_7(1,self.tus)
            self.btns_kontrol()
            if self.kayitlar_anahtar == False:
                self.kayit = Kontrol()


    def btns_2(self, tus_2):  # Tuşa basıldığında..
        self.tus_2 = tus_2
        if self.tus_2 == 'Çıkış':
            self.kapa = self.cikis()

        if self.tus_2 == 'Bilgilendirme':
            return None

    def cikis(self,event=None):
        self.yolla_delete = veriTabani.VeriTabani_7(0,'')
        self.pencere.destroy()

    def veriTabani_yarat(self):
        self.vt_yarat = veriTabani.VeriTabani_yarat()




if __name__ == '__main__':
    uyg = Main()
    mainloop()
