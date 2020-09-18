# -*-coding=utf-8-*-

import os
import sys
import time
import xlsxwriter
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from veriTabani import VeriTabani_5 as db_lite_5
from datetime import datetime
from datetime import timedelta
from tkinter import filedialog as tf


def topluKayan_liste(*func_list):
    ''' çoklu fonksiyonları beraber çalıştır'''
    return lambda *args, **kw: [func(*args, **kw) for func in func_list]
    None


class Kayitlar(object):
    """ self.var1 : liste sıra numarası verir
        self.toplam : toplama değişkeni
        self.row_select: satırlar için bool işlemi yapar
        self.pencere : gui
        """

    def __init__(self, row_select=True, **kwargs):
        self.var1 = 0
        self.toplam = 0

        self.row_select = row_select
        self.columns = ['no', 'liste1', 'liste2', 'liste3']
        self.tarihler_liste = []
        self.musteriler_liste = []
        self.gelir_turu_liste = []
        self.gider_turu_liste = []
        self.sayac_num = []
        self.tarih_d = []
        self.tarih_m = []
        self.tarih_Y = []
        self.tarih_d2 = []
        self.tarih_m2 = []
        self.tarih_Y2 = []
        self.tarih_YY = int(datetime.today().strftime('%Y'))

        self.kayitlar_pencere = Tk()

        self.kayit_pen()



    def konum(self,gen,yuks,penc):
        'modülün ekrandaki konumunu hesaplar'
        self.pgen = gen
        self.pyuks = yuks
        self.penc = penc

        self.ekrangen = self.penc.winfo_screenwidth()
        self.ekranyuks = self.penc.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 2
        self.y = (self.ekranyuks - self.pyuks) / 2

        self.penc.geometry('%dx%d+%d+%d' % (self.pgen, self.pyuks,
                                               self.x, self.y))

    def kayit_pen(self):
        'Tüm gui ayarları'
        if sys.platform == 'win32':
            self.konum(908,480,self.kayitlar_pencere)
        else:
            self.konum(1000,490,self.kayitlar_pencere)
        self.kayitlar_pencere.tk_setPalette('#9fb6cd')
        self.kayitlar_pencere.resizable(width=FALSE, height=FALSE)
        self.kayitlar_pencere_titlE = self.kayitlar_pencere.title("""CUT VERİ
TABANI""")
        self.kayitlar_pencere.bind("<Escape>",self.cikis)
        self.param_pencere = Frame(self.kayitlar_pencere)
        self.param_pencere['bd'] = 2
        self.param_pencere['relief'] = 'flat'
        self.param_pencere['height'] = 2

        self.param_pencere.place(relx=0.3, rely=0.0,
                relheight=0.20,relwidth=0.37)

        self.param_1 = StringVar(self.kayitlar_pencere)
        self.param_1.set('P 1:')
        self.param_2 = StringVar(self.kayitlar_pencere)
        self.param_2.set('P 2:')
        self.param_3 = StringVar(self.kayitlar_pencere)
        self.param_3.set('P 3:')
        self.param_4 = StringVar(self.kayitlar_pencere)
        self.param_4.set('P 4:')

        'ttk için stil '
       # self.boldStyle = ttk.Style ()
       # 
       # self.boldStyle.configure("Bold.TCheckbutton",height=2, 
       #                          font = ('Courier','12','bold'),
       #                          background = '#9fb6cd')
       #                         


        self.etiket_kayitlar = Label(self.param_pencere,
                                     textvariable=self.param_1,
                                     font='Courier 12 bold')
        self.etiket_kayitlar.place(rely=0.1)
        self.etiket_kayitlar_2 = Label(self.param_pencere,
                                       textvariable=self.param_2,
                                     font='Courier 12 bold')
        self.etiket_kayitlar_2.place(relx=0.5,rely=0.1)
        self.etiket_kayitlar_3 = Label(self.param_pencere,
                                       textvariable=self.param_3,
                                       font='Courier 12 bold')
        self.etiket_kayitlar_3.place(rely=0.6)
        self.etiket_kayitlar_4 = Label(self.param_pencere,
                                       textvariable=self.param_4,
                                       font='Courier 12 bold')
        self.etiket_kayitlar_4.place(relx=0.5,rely=0.6)

        self.tablo_sec_pen = Frame(self.kayitlar_pencere,
                height=3)
        self.tablo_sec_pen['bd'] = 2
        self.tablo_sec_pen['relief'] = 'groove'
        self.tablo_sec_pen.grid(column=0,row=0,padx=2,pady=2,sticky=NW)
        self.etiket_kombo = Label(self.tablo_sec_pen,
                                      text='Tablo seçin:',
                                      font='Courier 12 bold',
                                      bg='#9fb6cd',width=16)

        self.etiket_kombo.grid(column=0, row=0,padx=2,pady=2, sticky=NW)

        self.kombo = ttk.Combobox(self.tablo_sec_pen,width=15)
        self.kombo['values'] = ('Gelir Tablo', 'Gider Tablo')
        self.kombo['font'] = 'arial 12'
        self.kombo.grid(column=0, row=1,padx=2,pady=2, sticky='we')



        self.btn_kombo = Button(self.tablo_sec_pen,
                                text='Bağlan / Yenile',
                                font='Arial 11 ',
                                bg='#e0eeee',
                                fg='#1c1c1c',
                                width=21,
                                command=self.kontrol)

        self.btn_kombo.grid(column=0,row=2,padx=2,pady=2,sticky=NW)

        'parametreler '
        self.cerceve_kombo_3 = Frame(self.kayitlar_pencere)
        self.cerceve_kombo_3['bd'] = 2
        self.cerceve_kombo_3['relief'] = 'groove'
        self.cerceve_kombo_3.grid(column=0, row=1, padx=2, pady=2)

        self.cerceve_kombo_4 = Frame(self.kayitlar_pencere)
        self.cerceve_kombo_4['bd'] = 2
        self.cerceve_kombo_4['relief'] = 'sunken'
        self.cerceve_kombo_4.grid(column=1, row=1, padx=5,
                pady=2,sticky=NW)

        self.tablo_stunlar()
        self.etiket_toplam = Label(
            self.cerceve_kombo_3, text='Toplam : ', font='Courier 13 bold')
        self.etiket_toplam.grid(column=0,row=11,sticky=W)
        self.veri_sil = Button(self.kayitlar_pencere,text='Veri Sil',
                               width=11,
                               font='Arial 11',
                               bg = '#e0eeee',
                               fg = '#1c1c1c',
                              command=self.kalici_sil)
        self.veri_sil.grid(column=1,row=0,padx=35,pady=10,sticky='se')
        self.cikis = Button(self.kayitlar_pencere,text='Çıkış',
                               width=11,
                            font='Arial 11',
                            bg = '#e0eeee',
                            fg = '#1c1c1c',
                              command=self.cikis)
        self.cikis.grid(column=1,row=2,padx=35,pady=10,sticky='se')
        self.cikti_al = Button(self.kayitlar_pencere,text='Kaydet',
                               width=11,
                            font='Arial 11',
                            bg = '#e0eeee',
                            fg = '#1c1c1c',
                              command=self.kaydet)
        self.cikti_al.grid(column=1,row=2,pady=10,sticky='sw')
        self.lb_hepsi()
        self.scrollbar()
        self.row_select_one()

    def tablo_stunlar(self,*args,**kwargs):
        self.etiket_Tablo = Label(self.cerceve_kombo_3,
                                      text='Tablo parametreleri :',
                                      font='Courier 12 bold',
                                      bg='#9fb6cd')
        self.etiket_Tablo.grid(row=0, pady=3)

        self.liste_kombo = Listbox(self.cerceve_kombo_3, height=2)
        self.liste_kombo['relief'] = 'raised'
        self.liste_kombo['font'] = 'arial 12'
        self.liste_kombo['bg'] = '#f2f2f2'
        self.liste_kombo.grid(row=2,sticky='we')
        self.liste_kombo.bind("<Double-Button-1>", self.gosterici_2)

        self.diger_parametreler = Label(self.cerceve_kombo_3,
                                        text='Diğer Parametreler: ',
                                        font='Courier 11 bold')
        self.diger_parametreler.grid(pady=3,row=3)

        self.guncel = Label(self.cerceve_kombo_3,
                            text='Yeni Liste:',
                           font='Courier 9 bold')
        self.guncel.grid(pady=3,padx=1,row=4,sticky='w')

        self.param_str = StringVar(self.kayitlar_pencere)
        self.param_kombo_1 = ttk.Combobox(self.cerceve_kombo_3,
                                          textvariable=self.param_str,
                                         width=15)
        self.param_kombo_1.bind("<<ComboboxSelected>>" ,self.gosterici_2)
        self.param_kombo_1['values'] = ()
        self.param_kombo_1.grid(pady=3, padx=2,row=4,sticky='e')
        
        self.eski = Label(self.cerceve_kombo_3,
                            text='Eski Liste:',
                           font='Courier 9 bold')
        self.eski.grid(pady=3,padx=1,row=5,sticky='w')

        self.param_str2 = StringVar(self.kayitlar_pencere)
        self.param_kombo_2 = ttk.Combobox(self.cerceve_kombo_3,
                                          textvariable=self.param_str2,
                                         width=15)
        self.param_kombo_2.bind("<<ComboboxSelected>>" ,self.gosterici_2)
        self.param_kombo_2['values'] = ()
        self.param_kombo_2.grid(pady=3, padx=2,row=5,sticky='e')
        
        self.tarihler_cerceve = Frame(self.cerceve_kombo_3)
        self.tarihler_cerceve['bd'] = 2
        self.tarihler_cerceve['relief'] = 'groove'
        self.tarihler_cerceve.grid(pady=2,row=6,sticky=NW)
        self.kontrol_var = StringVar(self.kayitlar_pencere)
        self.kontrol_var.set('1:Başlar')
        self.kontrol_int = IntVar()
        self.kontrol_int.set(1)
        self.kontrol_kutusu_tarih = Label(self.tarihler_cerceve,width=10,
                                           textvariable=self.kontrol_var,
                                             font='Courier 11 bold')
        self.kontrol_kutusu_tarih.pack(side='left',padx=1,expand=YES,fill=X)



        self.etiket_Tablo_2slash = Label(self.tarihler_cerceve,
                                         text='~')
        self.etiket_Tablo_2slash.pack(side='left')
        self.kontrol_var2 = StringVar(self.kayitlar_pencere)
        self.kontrol_var2.set('2:Bugün')
        self.kontrol_kutusu_tarih2 = Label(self.tarihler_cerceve,width=10,
                                           textvariable=self.kontrol_var2,
                                           font='Courier 11 bold')
        self.kontrol_kutusu_tarih2.pack(side='left',expand=YES,fill=X)

        self.wt_combo_cerceve = Frame(self.cerceve_kombo_3)
        self.wt_combo_cerceve['bd'] = 2
        self.wt_combo_cerceve['relief'] = 'groove'
        self.wt_combo_cerceve.grid(pady=2, row=7, sticky= NE )

        self.wt_combo_cerceve2 = Frame(self.cerceve_kombo_3)
        self.wt_combo_cerceve2['bd'] = 2
        self.wt_combo_cerceve2['relief'] = 'groove'
        self.wt_combo_cerceve2.grid(pady=4, row=8, sticky= NE )
        self.wt_label = Label(self.cerceve_kombo_3,text='1:Tarih',
                             font='Courier 9 bold')
        self.wt_label.grid(pady=2,row=7,sticky=NW)
        self.wt_label2 = Label(self.cerceve_kombo_3,text='2:Tarih',
                              font='Courier 9 bold')
        self.wt_label2.grid(pady=4,row=8,sticky=NW)

        self.wt_combo()

    def wt_combo(self):
        self.sayac(1,31)
        self.tarih_d.extend(self.sayac_num)
        self.tarih_kombo = ttk.Combobox(self.wt_combo_cerceve,width=4)
        self.tarih_kombo['value'] = (self.tarih_d)
        self.tarih_kombo.pack(side='left')        
        self.sayac_num.clear()

        self.sayac(1,12)
        self.tarih_m.extend(self.sayac_num)
        self.tarih_kombo_2 = ttk.Combobox(self.wt_combo_cerceve,width=4)
        self.tarih_kombo_2['value'] = (self.tarih_m)
        self.tarih_kombo_2.pack(side='left')
        self.sayac_num.clear()

        self.sayac(self.tarih_YY,self.tarih_YY+20)
        self.tarih_Y.extend(self.sayac_num)
        self.tarih_kombo_3 = ttk.Combobox(self.wt_combo_cerceve,width=5)
        self.tarih_kombo_3['value'] = (self.tarih_Y)
        self.tarih_kombo_3.pack(side='left')
        self.sayac_num.clear()

        self.sayac(1,31)
        self.tarih_d2.extend(self.sayac_num)
        self.tarih_kombo_4 = ttk.Combobox(self.wt_combo_cerceve2,width=4)
        self.tarih_kombo_4['value'] = (self.tarih_d2)
        self.tarih_kombo_4.pack(side='left')        
        self.sayac_num.clear()

        self.sayac(1,12)
        self.tarih_m2.extend(self.sayac_num)
        self.tarih_kombo_5 = ttk.Combobox(self.wt_combo_cerceve2,width=4)
        self.tarih_kombo_5['value'] = (self.tarih_m2)
        self.tarih_kombo_5.pack(side='left')
        self.sayac_num.clear()

        self.sayac(self.tarih_YY,self.tarih_YY+20)
        self.tarih_Y2.extend(self.sayac_num)
        self.tarih_kombo_6 = ttk.Combobox(self.wt_combo_cerceve2,width=5)
        self.tarih_kombo_6['value'] = (self.tarih_Y2)
        self.tarih_kombo_6.pack(side='left')
        self.sayac_num.clear()




        self.btn_getir = Button(self.cerceve_kombo_3, width=9,
                                text='Bul',
                                font='Arial 11 ',
                                bg='#e0eeee',
                                fg='#1c1c1c', command=self.bul)
        self.btn_getir.grid(pady=7, padx=2, row=10, sticky=E)

        self.btn_geri_al = Button(self.cerceve_kombo_3, width=9,
                                  text='Geri Al',
                                  font='Arial 11 ',
                                  bg='#e0eeee',
                                  fg='#1c1c1c',command=self.geri_al)
        self.btn_geri_al.grid(pady=7, padx=2, row=10, sticky=W)

    def lb_hepsi(self, **kwargs):
        ''' Bütün tablo listboxları kapsar'''

        self.lb0 = Listbox(self.cerceve_kombo_4,
                           borderwidth=0,
                           highlightthickness=0, width=8,height=17,
                           exportselection=not self.row_select, **kwargs)
        self.lb0['font'] = 'arial 12'
        self.lb0['bg'] = '#f2f2f2'
        self.lb0.grid(column=0, row=0)
        self.lb1 = Listbox(self.cerceve_kombo_4,
                           borderwidth=0,
                           highlightthickness=0, width=15,height=17,
                           exportselection=not self.row_select, **kwargs)
        self.lb1['font'] = 'arial 12'
        self.lb1['bg'] = '#f2f2f2'
        self.lb1.grid(column=1, row=0)
        self.lb2 = Listbox(self.cerceve_kombo_4,
                           borderwidth=0,
                           highlightthickness=0, width=21,height=17,
                           exportselection=not self.row_select, **kwargs)
        self.lb2['font'] = 'arial 12'
        self.lb2['bg'] = '#f2f2f2'
        self.lb2.grid(column=2, row=0)
        self.lb3 = Listbox(self.cerceve_kombo_4,
                           borderwidth=0,
                           highlightthickness=0, width=20,height=17,
                           exportselection=not self.row_select, **kwargs)
        self.lb3['font'] = 'arial 12'
        self.lb3['bg'] = '#f2f2f2'
        self.lb3.grid(column=3, row=0)
        self.lb4 = Listbox(self.cerceve_kombo_4,
                           borderwidth=0,
                           highlightthickness=0, width=9,height=17,
                           exportselection=not self.row_select, **kwargs)
        self.lb4['font'] = 'arial 12'
        self.lb4['bg'] = '#f2f2f2'
        self.lb4.grid(column=4, row=0)

        self.lb0.insert(0, 'no ')
        self.lb1.insert(0, 'liste - 1')
        self.lb2.insert(0, "liste - 2")
        self.lb3.insert(0, 'liste - 3')
        self.lb4.insert(0, 'liste - 4')

    def scrollbar(self):
        self.kaydirma_cubuk_Y = Scrollbar(
            self.cerceve_kombo_4, orient="vertical")
        self.kaydirma_cubuk_Y.config(bg='#e5e5e5',command=self.yview)
        self.kaydirma_cubuk_Y.grid(column=5, row=0, sticky=N+S)
        self.lb0.config(yscrollcommand=self.yscroll)
        self.lb1.config(yscrollcommand=self.yscroll)
        self.lb2.config(yscrollcommand=self.yscroll)
        self.lb3.config(yscrollcommand=self.yscroll)
        self.lb4.config(yscrollcommand=self.yscroll)

    def yscroll(self, *args):
        'liste kutuları kaydırma verileri sıfırlama'
        if self.lb0.yview() != self.lb1.yview() or self.lb2.yview() or self.lb3.yview() or self.lb4.yview():
            self.lb0.yview_moveto(args[0])
        if self.lb1.yview() != self.lb0.yview() or self.lb2.yview() or self.lb3.yview() or self.lb4.yview():
            self.lb1.yview_moveto(args[0])
        if self.lb2.yview() != self.lb0.yview() or self.lb1.yview() or self.lb3.yview() or self.lb4.yview():
            self.lb2.yview_moveto(args[0])
        if self.lb3.yview() != self.lb0.yview() or self.lb1.yview() or self.lb2.yview() or self.lb4.yview():
            self.lb3.yview_moveto(args[0])
        if self.lb4.yview() != self.lb0.yview() or self.lb1.yview() or self.lb2.yview() or self.lb3.yview():
            self.lb4.yview_moveto(args[0])
        self.kaydirma_cubuk_Y .set(*args)

    def yview(self, *args):
        'liste kutaları veri topla'
        self.lb0.yview(*args)
        self.lb1.yview(*args)
        self.lb2.yview(*args)
        self.lb3.yview(*args)
        self.lb4.yview(*args)

    def row_select_one(self, **kwargs):
        'satırlar seçildiginde bilgi toplar'
        self.boxes = []
        if self.row_select:
            self.lb0.bind('<<ListboxSelect>>', self.selected)
            self.lb1.bind('<<ListboxSelect>>', self.selected)
            self.lb2.bind('<<ListboxSelect>>', self.selected)
            self.lb3.bind('<<ListboxSelect>>', self.selected)
            self.lb4.bind('<<ListboxSelect>>', self.selected)
        self.boxes.append(self.lb0)
        self.boxes.append(self.lb1)
        self.boxes.append(self.lb2)
        self.boxes.append(self.lb3)
        self.boxes.append(self.lb4)
        pass

    def selected(self, event=None):
        'satır bilgilerini eşitler'
        row = event.widget.curselection()[0]
        for lbox in self.boxes:
            lbox.select_clear(0, END)
            lbox.select_set(row)


    def modul_kapa(self):
        from veriTabani import VeriTabani_7
        self.modul_kapanir = VeriTabani_7(2,'Veri Tabanı')

    def cikis(self,even=None):
        self.modul_kapa()
        self.kayitlar_pencere.destroy()
        pass


class Kontrol(Kayitlar):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.tepe_yazi = []
        self.bul_islem = False
        self.tepe_yazi_2 = []
        self.param_onay = False
        self.param_onay_2 = False
        self.farklar = []
        self.farklar_2 = []
        self.bugun = datetime.today().strftime('%d.%m.%Y')
        self.limit = 0
        self.limit_2 =  int(datetime.today().strftime('%m'))
        self.limit_3 = int(datetime.today().strftime('%Y'))
        self.limit_4 = 0
        self.limit_5 = 0
        self.limit_6 = 0
        self.limit_7 = 0
        self.tablo_silici = 0
        self.sayac_num = []
        self.for_atama = []
        self.for_atama2 = []
        self.for_atama3 = []
        self.for_atama4 = []
        self.for_atama5 = []
        self.ilk = datetime.today().replace(day=1,
                                            month=self.limit_2,
                                            year=self.limit_3).strftime('%d.%m.%Y')
        self.gelir_tablo = False
        self.gider_tablo = False
        self.tablo_parametreler_islem = False
        self.yolla_to_islem = False
        self.web_adres ='www.cuttasarim.com' 

    def sayac(self,num, end_num):
        self.sayac_num.append(str(num).zfill(2))
        if num == end_num:
            return None
        else:
            return self.sayac(num+1, end_num)

    def kontrol(self):
        'Tablo seçer'
        if self.gelir_tablo == False:
            if self.kombo.get() == 'Gelir Tablo':

                self.tablo_sil()
                self.Gelir_Tablo_izle = db_lite_5(self.kombo.get(), self.limit,
                                                  self.limit_2,self.limit_3,
                                                  self.limit_4,self.limit_5,
                                                  self.limit_6,self.limit_7,
                                                 self.tablo_silici)
                self.gelir_tablo_izle_gui()
                self.izle()
                self.veritabani_listeler()
                self.tablo_parametreler_islem = True
                self.gelir_tablo = True
                self.gider_tablo = False
                self.geri_al()
        if self.gider_tablo == False:
            if self.kombo.get() == 'Gider Tablo':
                self.tablo_sil()
                self.Gelir_Tablo_izle = db_lite_5(self.kombo.get(), self.limit,
                                                  self.limit_2,self.limit_3,
                                                  self.limit_4,self.limit_5,
                                                  self.limit_6,self.limit_7,
                                                 self.tablo_silici)
                self.gider_tablo_izle_gui()
                self.izle()
                self.veritabani_listeler()
                self.tablo_parametreler_islem = True
                self.gider_tablo = True
                self.gelir_tablo = False
                self.geri_al()

    def param_bool(self):
        'p1 p2 ve p3 p4 iceriklerini kontrol eder'
        if len(self.tepe_yazi) == 2:
            if len(self.tepe_yazi_2) == 0:
                return self.bul_p1_p2()
            elif len(self.tepe_yazi_2) == 2:
                return self.bul_hepsi()
        elif len(self.tepe_yazi) < 1:
            self.bul_t1_t2()
            pass

    def bul_t1_t2(self):
        if self.spesifik_aralik:
            self.tablo_sil()
            self.parametre_izle = db_lite_5(self.kombo.get(),self.limit,
                                            self.limit_2,self.limit_3,
                                            self.limit_4,self.limit_5,
                                            self.limit_6,self.limit_7,
                                           self.tablo_silici)
            self.sil(self.kombo.get(),self.limit,
                          self.limit_2,self.limit_3,
                          self.limit_4,self.limit_5,
                          self.limit_6,self.limit_7)
            if self.kombo.get() == 'Gelir Tablo':
                self.gelir_tablo_izle_gui()
            elif self.kombo.get() == 'Gider Tablo':
                self.gider_tablo_izle_gui()

            self.geri_al()
            self.limit = 0
            self.bul_islem = True #veri sil icin anahtar

    def bul_p1_p2(self):
        'p1 ve p2 aramalarını veri tabanına yollar'
        if self.tepe_yazi[0] == 'Gelir Türü':
            self.limit_4 = self.tepe_yazi[1]
            self.tablo_sil()
            self.sil(self.kombo.get(),self.limit,
                          self.limit_2,self.limit_3,
                          self.limit_4,self.limit_5,
                          self.limit_6,self.limit_7)
            self.parametre_izle = db_lite_5(self.kombo.get(), self.limit,
                                          self.limit_2,self.limit_3,
                                          self.limit_4,self.limit_5,
                                            self.limit_6,self.limit_7,
                                           self.tablo_silici)
            self.gelir_tablo_izle_gui()
            self.geri_al()
            self.limit_4 = 0
            self.bul_islem = True #veri sil icin anahtar
        elif self.tepe_yazi[0] == 'Müşteriler':
                self.limit_5 = self.tepe_yazi[1]
                self.tablo_sil()
                self.parametre_izle = db_lite_5(self.kombo.get(), self.limit,
                                              self.limit_2,self.limit_3,
                                              self.limit_4,self.limit_5,
                                                self.limit_6,self.limit_7,
                                               self.tablo_silici)
                self.sil(self.kombo.get(),self.limit,
                              self.limit_2,self.limit_3,
                              self.limit_4,self.limit_5,
                              self.limit_6,self.limit_7)
                #self.gelir_tablo_parametre_izle()
                self.gelir_tablo_izle_gui()
                self.geri_al()
                self.limit_5 = 0
                self.bul_islem = True #veri sil icin anahtar
        elif self.tepe_yazi[0] == 'Gider Türü':
                self.limit_6 = self.tepe_yazi[1]
                self.tablo_sil()
                self.parametre_izle = db_lite_5(self.kombo.get(), self.limit,
                                              self.limit_2,self.limit_3,
                                              self.limit_4,self.limit_5,
                                                self.limit_6,self.limit_7,
                                               self.tablo_silici)
                self.sil(self.kombo.get(),self.limit,
                              self.limit_2,self.limit_3,
                              self.limit_4,self.limit_5,
                              self.limit_6,self.limit_7)
                #self.gider_tablo_parametre_izle()
                self.gider_tablo_izle_gui()
                self.geri_al()
                self.limit_6 = 0
                self.bul_islem = True #veri sil icin anahtar


    def bul_hepsi(self):
        'p1 p2 p3 p4 aramalarını veri tabanına yollar'
        if self.tepe_yazi[0] == 'Gelir Türü':
            self.limit_4 = self.tepe_yazi[1]
            if self.tepe_yazi_2[0] == 'Müşteriler':
                self.limit_5 = self.tepe_yazi_2[1]
        elif self.tepe_yazi[0] == 'Müşteriler':
            self.limit_5 = self.tepe_yazi[1]
            if self.tepe_yazi_2[0] == 'Gelir Türü':
                self.limit_6 = self.tepe_yazi_2[1]
                self.limit_4 = 0.1
        self.tablo_sil()
        self.parametre_izle = db_lite_5(self.kombo.get(), self.limit,
                                      self.limit_2,self.limit_3,
                                      self.limit_4,self.limit_5,
                                        self.limit_6,self.limit_7,
                                       self.tablo_silici)
        self.sil(self.kombo.get(),self.limit,
                      self.limit_2,self.limit_3,
                      self.limit_4,self.limit_5,
                      self.limit_6,self.limit_7)
        self.gelir_tablo_izle_gui()
        self.geri_al()
        self.limit_4 = 0
        self.limit_5 = 0
        self.limit_6 = 0
        self.bul_islem = True #veri sil icin anahtar

    def spesifik_araliklar(self):
        'kullanıcı kendi tarihini belirlemisse..'
        self.spesifik_aralik = all([self.tarih_kombo.get(),
                                    self.tarih_kombo_2.get(),
                                    self.tarih_kombo_3.get()])
        self.spesifik_aralik2 = all([self.tarih_kombo_4.get(),
                                     self.tarih_kombo_5.get(),
                                     self.tarih_kombo_6.get()])
    def bul(self):
        'seçili paramatreleri arar'
        if self.kombo.get():
           # if self.isaretle.get() == 1:
            self.spesifik_araliklar()
            if self.spesifik_aralik == False:
                pass
            else:
                self.tk = self.tarih_kombo.get()
                self.tk2 = self.tarih_kombo_2.get()
                self.tk3 = self.tarih_kombo_3.get()
                self.tk4 = self.tarih_kombo_4.get()
                self.tk5 = self.tarih_kombo_5.get()
                self.tk6 = self.tarih_kombo_6.get()
                self.limit = self.tk3+'.'+self.tk2+'.'+self.tk
                if self.spesifik_aralik2:
                    self.limit_7 = self.tk6+'.'+self.tk5+'.'+self.tk4
            self.param_bool()



    def gosterici(self, event):
        'bos döndür'
        return None

    def gosterici_2(self, event):
        'birlikte ara;  onayı bilgi mesajı verir.'
        if len(self.tepe_yazi) == 0:
            self.liste_get_active = self.liste_kombo.get(ACTIVE)
            self.param_1.set(self.liste_kombo.get(ACTIVE))
            self.etiket_kayitlar.configure(textvariable=self.param_1,
                                                         fg='#1c0f45')

            self.etiket_kayitlar.update()
            self.gosterici_to_parametreler()
            self.secilen_param()
        elif self.param_onay == True:
            'p:3 ve p:4 işlemleri'
            self.liste_get_active = self.liste_kombo.get(ACTIVE)
            if self.liste_get_active != self.tepe_yazi[0]:
                self.param_3.set(self.liste_get_active)
                self.etiket_kayitlar_3.configure(textvariable=self.param_3,
                                                 fg='#1c0f45')
                self.etiket_kayitlar_3.update()

                self.param_onay_2 = True
                self.gosterici_to_parametreler()


                self.secilen_param()

    def secilen_param(self):
        if len(self.tepe_yazi) == 0:
            if self.param_kombo_1.get():
                self.param_2.set(self.param_kombo_1.get())

                self.etiket_kayitlar_2.configure(fg='#1c0f45')
                self.etiket_kayitlar_2.update()
                self.tepe_yazi += self.liste_get_active,self.param_kombo_1.get()
                self.param_onay = True
                self.param_kombo_1.delete(0,END)
                self.param_kombo_1['values'] = ()
                self.param_kombo_2.delete(0,END)
                self.param_kombo_2['values'] = ()
            elif self.param_kombo_2.get():
                self.param_2.set(self.param_kombo_2.get())
                self.etiket_kayitlar_2.configure(fg='#1c0f45')
                self.etiket_kayitlar_2.update()
                self.tepe_yazi += self.liste_get_active,self.param_kombo_2.get()
                self.param_onay = True
                self.param_kombo_2.delete(0,END)
                self.param_kombo_2['values'] = ()
                self.param_kombo_1.delete(0,END)
                self.param_kombo_1['values'] = ()
                

        elif self.param_onay_2 == True:
           if self.param_kombo_1.get():
                self.param_p4 = self.param_kombo_1.get()
                self.param_4.set(self.param_p4)
                self.etiket_kayitlar_4.configure(fg='#1c0f45')
                self.etiket_kayitlar_4.update()
                self.tepe_yazi_2 += self.liste_get_active,self.param_kombo_1.get()
                self.param_kombo_1.delete(0,END)
                self.param_kombo_1['values'] = ()
                self.param_kombo_2.delete(0,END)
                self.param_kombo_2['values'] = ()
           elif self.param_kombo_2.get():
                self.param_p4 = self.param_kombo_2.get()
                self.param_4.set(self.param_p4)
                self.etiket_kayitlar_4.configure(fg='#1c0f45')
                self.etiket_kayitlar_4.update()
                self.tepe_yazi_2 += self.liste_get_active,self.param_kombo_2.get()
                self.param_kombo_2.delete(0,END)
                self.param_kombo_2['values'] = ()
                self.param_kombo_1.delete(0,END)
                self.param_kombo_1['values'] = ()




    def gosterici_to_parametreler(self):
        if self.liste_get_active == 'Müşteriler':
            self.musteri_parametreler()
            self.eski_musteri_parametreler()
        elif self.liste_get_active == 'Gelir Türü':
            self.gelir_turu_parametreler()
            self.eski_gelir_turu_parametreler()
        elif self.liste_get_active == 'Gider Türü':
            self.gider_turu_parametreler()
            self.eski_gider_turu_parametreler()

    def izle(self,*args,**kwargs):
        'Güncel tarih aralıklarını etiket(label) olarak gösterir'
        self.kontrol_var.set(self.ilk)
        self.kontrol_var2.set(self.bugun)


    def tablo_liste_baslik_renk(self):
        self.lb0.itemconfig(0, {'fg': 'black'})
        self.lb1.itemconfig(0, {'fg': '#8b4726'})
        self.lb2.itemconfig(0, {'fg': '#8b7500'})
        self.lb3.itemconfig(0, {'fg': '#1c6071'})
        self.lb4.itemconfig(0, {'fg': '#8b658b'})

    def tablo_gelir_baslik(self):
        self.lb0.insert(0, 'Sıra ')
        self.lb1.insert(0, 'Tarih')
        self.lb2.insert(0, "Gelir Türü")
        self.lb3.insert(0, 'Müşteriler')
        self.lb4.insert(0, 'Gelir')

    def tablo_gider_baslik(self):
        self.lb0.insert(0, 'Sıra ')
        self.lb1.insert(0, 'Tarih')
        self.lb2.insert(0, "Gider Türü")
        self.lb3.insert(0, 'Gider')
        self.lb4.insert(0, '----')

    def gelir_tablo_parametreler(self):
        self.liste_kombo.insert(END, 'Gelir Türü')
        self.liste_kombo.insert(END, 'Müşteriler')
        self.tarihler_liste.clear()

    def tarihi_ters_cevir(self,get):
        'gelir ve gider tabloya ait tarihi ters çevirir.;show:%d%m%Y'
        self.get = get
        self.c = self.get[::-1]
        self.c_1 = self.c[:2][::-1]+self.c[2:3]
        self.c_2 = self.c[3:5][::-1]+self.c[5:6]
        self.c_3 = self.c[6:10][::-1]
        self.yeni_tarih = self.c_1+self.c_2+self.c_3
        for fix in [self.yeni_tarih]:
            self.lb1.insert(END,fix)
            self.for_atama2.append(fix)  #xlsx için tarihi ters ceviren liste = 1


    def gelir_tablo_izle_gui(self):
        'veri tabanından alnan tablo '
        self.tablo_gelir_baslik()
        self.tablo_liste_baslik_renk()
        self.gelir_tablo_parametreler()
        self.for_atama2.clear()  #xlsx için tarihi ters ceviren liste = 0
        from kayitlar import Postaci
        if Postaci.Ppostaci_kayitlar:
            for get in Postaci.Ppostaci_kayitlar:
                self.var1 += 1
                self.lb0.insert(END, str(self.var1))
                self.tarihi_ters_cevir(get[0])
               # self.tarihler_liste.append(get[0])
                self.lb2.insert(END, get[1])
                self.lb3.insert(END, get[2])
                self.lb4.insert(END, get[3])
                self.toplam += float(get[3])
        else:
            self.lb1.insert(END,'veri yok!')
            self.lb1.itemconfig(END, {'fg': 'red'})
            self.lb2.insert(END,'veri yok!')
            self.lb3.insert(END,'veri yok!')
            self.lb3.itemconfig(END, {'fg': 'red'})
            self.lb4.insert(END,'veri yok!')
        self.for_atama = Postaci.Ppostaci_kayitlar
       # Postaci.Ppostaci_kayitlar.clear()
        return self.topla()



    def gider_tablo_izle_gui(self):
        'veri tabanından alınan tablo'
        self.tablo_gider_baslik()
        self.tablo_liste_baslik_renk()
        self.gider_tablo_parametreler()
        self.for_atama2.clear() #xlsx için tarihi ters ceviren liste = 0
        from kayitlar import Postaci
        if Postaci.Ppostaci_kayitlar:
            for get2 in Postaci.Ppostaci_kayitlar:
                self.var1 += 1
                self.lb0.insert(END, self.var1)
                self.tarihi_ters_cevir(get2[0])
               # self.tarihler_liste.append(get2[0])
                self.lb2.insert(END, get2[1])
                self.lb3.insert(END, get2[2])
                self.lb4.delete(0, END)
                self.toplam += float(get2[2])
        else:
            self.lb1.insert(END,'veri yok!')
            self.lb1.itemconfig(END, {'fg': 'red'})
            self.lb2.insert(END,'veri yok!')
            self.lb3.insert(END,'veri yok!')
            self.lb3.itemconfig(END, {'fg': 'red'})
        self.for_atama = Postaci.Ppostaci_kayitlar
        #Postaci.Ppostaci_kayitlar.clear()
        return self.topla()



    def gider_tablo_parametreler(self):
        self.liste_kombo.insert(END, 'Gider Türü')
        self.tarihler_liste.clear()


    def veritabani_listeler(self):
        from veriTabani import VeriTabani_6
        self.liste_cek = VeriTabani_6()
        from kayitlar import Postaci2
        self.gelir_turu_liste = Postaci2.postaci_gelir_liste
        self.musteriler_liste = Postaci2.postaci_musteriler_liste
        self.gider_turu_liste = Postaci2.postaci_gider_liste
        self.gelir_arsiv = Postaci2.postaci_gelir_arsiv
        self.musteri_arsiv = Postaci2.postaci_musteri_arsiv
        self.gider_arsiv = Postaci2.postaci_gider_arsiv



    def musteri_parametreler(self):
        'müşteriler diger_parametreler listesini oluşturur'
        self.farklar.clear()
        self.farklar_2.clear()
        for get4 in self.musteriler_liste:
            if not get4 in self.farklar:
                self.farklar.append(get4)
                if not get4 in self.farklar_2:
                    self.farklar_2.append(get4)


        self.param_kombo_1['values'] = (self.farklar_2)
        from kayitlar import Postaci2
        self.liste_sil = Postaci2.postaci_musteriler_liste.clear()


    def eski_musteri_parametreler(self):
        'silinmiş olan musteri paratreleri listeler'
        self.farklar.clear()
        self.farklar_2.clear()
        for get7 in self.musteri_arsiv:
            if not get7 in self.farklar:
                self.farklar.append(get7)
                if not get7 in self.farklar_2:
                    self.farklar_2.append(get7)
        self.param_kombo_2['values'] = (self.farklar_2)
        from kayitlar import Postaci2
        self.liste_sil = Postaci2.postaci_musteri_arsiv.clear()

    def gelir_turu_parametreler(self):
        'gelir türü diger_parametreler listesini oluşturur'
        self.farklar.clear()
        self.farklar_2.clear()
        for get5 in self.gelir_turu_liste:
            if not get5 in self.farklar:
                self.farklar.append(get5)
                if not get5 in self.farklar_2:
                    self.farklar_2.append(get5)


        self.param_kombo_1['values'] = (self.farklar_2)
        from kayitlar import Postaci2
        self.liste_sil = Postaci2.postaci_gelir_liste.clear()

    def eski_gelir_turu_parametreler(self):
        'silinen gelir türü parametreleri listesi'
        self.farklar.clear()
        self.farklar_2.clear()
        for get8 in self.gelir_arsiv:
            if not get8 in self.farklar:
                self.farklar.append(get8)
                if not get8 in self.farklar_2:
                    self.farklar_2.append(get8)

        self.param_kombo_2['values'] = (self.farklar_2)
        from kayitlar import Postaci2
        self.liste_sil = Postaci2.postaci_gelir_arsiv.clear()

    def gider_turu_parametreler(self):
        'gider türü diger_parametreler listesini oluşturur'
        for get6 in self.gider_turu_liste:
            if not get6 in self.farklar:
                self.farklar.append(get6)
                if not get6 in self.farklar_2:
                    self.farklar_2.append(get6)

        self.param_kombo_1['values'] = (self.farklar_2)
        from kayitlar import Postaci2
        self.liste_sil = Postaci2.postaci_gider_liste.clear()

    def eski_gider_turu_parametreler(self):
        'silinen gider turu listesi'
        self.farklar.clear()
        self.farklar_2.clear()
        for get9 in self.gider_arsiv:
            if not get9 in self.farklar:
                self.farklar.append(get9)
                if not get9 in self.farklar_2:
                    self.farklar_2.append(get9)

        self.param_kombo_2['values'] = (self.farklar_2)
        from kayitlar import Postaci2
        self.liste_sil = Postaci2.postaci_gider_arsiv.clear()



    def tablo_sil(self):
        'Tablo geçişlerinde bağlı değişkenleri sıfırlar'
        from kayitlar import Postaci
        self.lb0.delete(0, END)
        self.lb1.delete(0, END)
        self.lb2.delete(0, END)
        self.lb3.delete(0, END)
        self.lb4.delete(0, END)
        self.liste_kombo.delete(0, END)
        Postaci.Ppostaci_kayitlar.clear()
        self.var1 = 0
        self.toplam = 0
        self.farklar.clear()
        self.farklar_2.clear()
        self.param_kombo_1['values'] = ()
        self.param_kombo_2['values'] = ()
        self.limit_2 =  int(datetime.today().strftime('%m'))
        self.limit_3 = int(datetime.today().strftime('%Y'))


    def tablo_sil_parametreler(self):
        'çagırılmış olan tablo nesnelerini Listbox tan siler'
        from kayitlar import Postaci
        self.lb0.delete(0, END)
        self.lb1.delete(0, END)
        self.lb2.delete(0, END)
        self.lb3.delete(0, END)
        self.lb4.delete(0, END)
        self.liste_kombo.delete(0, END)

        self.var1 = 0
        self.toplam = 0
        self.farklar.clear()
        self.farklar_2.clear()


    def topla(self):
        'çağırılan tablonun sayı değerlerini topla'
        self.etiket_toplam['text'] = 'Toplam: {} tl'.format(
            round(self.toplam, 2))
        self.etiket_toplam['font'] = 'Courier 13 bold'
        self.etiket_toplam['fg'] = '#1c0f45'


    def geri_al(self,*args,**kwargs):
        'parametre listesini ekrandan ve listerden siler'
        self.gelir_tablo = False
        self.gider_tablo = False
        self.tablo_parametreler_islem = True
        self.veritabani_listeler()
        self.limit = 0
        self.limit_7 = 0
        self.limit_2 =  int(datetime.today().strftime('%m'))
        self.limit_3 = int(datetime.today().strftime('%Y'))
        self.izle()
        self.tarih_kombo.delete(0,END)
        self.tarih_kombo_2.delete(0,END)
        self.tarih_kombo_3.delete(0,END)
        self.tarih_kombo_4.delete(0,END)
        self.tarih_kombo_5.delete(0,END)
        self.tarih_kombo_6.delete(0,END)
        self.param_1.set('P 1:')
        self.param_2.set('P 2:')
        self.param_3.set('P 3:')
        self.param_4.set('P 4:')
        self.tepe_yazi.clear()
        self.tepe_yazi_2.clear()
        self.param_kombo_1['values'] = ()
        self.param_kombo_2['values'] = ()
        self.tablo_silici = 0
        self.bul_islem = False


    def yeni_atama(self):
        'xlsx icin yeni listenin başına ters çevrilmiş tarih ekler'
        self.a = 0
        for k in self.for_atama2:
            self.for_atama3[self.a][0] = k
            self.a += 1

        


    def kaydet(self):
        'tabloyu .xlsx dosya olarak kaydet'
        if self.kombo.get():
            self.getcwd = os.getcwd()
            self.isdir = os.path.isdir(self.getcwd+'/Cut_xlsx')
            if self.isdir == False:
                self.mkdir = os.mkdir(self.getcwd+'/Cut_xlsx')
            self.dosya_ayar = ayarlar = {}
            ayarlar['initialdir'] = self.getcwd+'/Cut_xlsx'
            ayarlar['defaultextension'] = '.xlsx'
            ayarlar['filetypes'] = [('Exel dosyası','*.xlsx'),('Bütün dosyalar', '.*')]
            ayarlar['parent'] = self.kayitlar_pencere
            ayarlar['title'] = 'Dosya seç'

            self.dosya_kaydet = tf.asksaveasfilename( **self.dosya_ayar)
            if self.dosya_kaydet:
                for i in self.for_atama:
                    i = list(i)
                    self.for_atama3.append(i)
                self.yeni_atama()
                for m in self.for_atama3:
                    self.for_atama4.append(tuple(m))

                self.kaydedilen = xlsxwriter.Workbook(self.dosya_kaydet)
                self.worksheet  = self.kaydedilen.add_worksheet(self.kombo.get())
                self.bold = self.kaydedilen.add_format({'bold': True})
                self.money = self.kaydedilen.add_format({'num_format': '0.0TL'})
                self.worksheet.set_column(
                    'A:A', # column width Tarih
                    11)
                self.row = 1
                self.col = 0
                if len(self.for_atama4[0]) == 4:
                    self.worksheet.write('A1', 'Tarih', self.bold)
                    self.worksheet.write('B1', 'Gelir Türü', self.bold)
                    self.worksheet.write('C1', 'Müşteriler', self.bold)
                    self.worksheet.set_column(
                        1, # column width gelir_tur
                        2, # column width mus
                        17
                    )
                    self.worksheet.write('D1', 'Gelir',self.bold)
                    for tarih, gelir_Tur,mus,gelir in (self.for_atama4):
                        self.worksheet.write(self.row, self.col,     tarih)
                        self.worksheet.write(self.row, self.col + 1, gelir_Tur)
                        self.worksheet.write(self.row, self.col + 2, mus)
                        self.worksheet.write(self.row, self.col + 3, gelir,self.money)
                        self.row += 1
                    self.worksheet.write(self.row, 0, 'Toplam',self.bold)
                    self.worksheet.write(self.row, 3, self.toplam,self.money)
                    self.worksheet.write(self.row+2,1, self.web_adres)
                elif len(self.for_atama4[0]) == 3:
                    self.worksheet.write('A1', 'Tarih', self.bold)
                    self.worksheet.write('B1', 'Gider Türü', self.bold)
                    self.worksheet.set_column(
                        'B:B', # column Tarih
                        17)
                    self.worksheet.write('C1', 'Gider',self.bold)
                    for tarih, gider_Tur,gider in (self.for_atama4):
                        self.worksheet.write(self.row, self.col,     tarih)
                        self.worksheet.write(self.row, self.col + 1, gider_Tur)
                        self.worksheet.write(self.row, self.col + 2, gider,self.money)
                        self.row += 1
                    self.worksheet.write(self.row, 0, 'Toplam',self.bold)
                    self.worksheet.write(self.row, 2, self.toplam,self.money)
                    self.worksheet.write(self.row+2,1, self.web_adres)

                self.kaydedilen.close()

    def sil(self,Tablo,*args):
        'olası tablo silme işlemi için değişkenleri tutar.'
        self.Tablo = Tablo
        self.yoket = [*args][0]
        self.yoket_2 = [*args][1]
        self.yoket_3 =[*args][2]
        self.yoket_4 = [*args][3]
        self.yoket_5 = [*args][4]
        self.yoket_6 = [*args][5]
        self.yoket_7 = [*args][6]

    def kalici_sil(self):
        if self.bul_islem == True:
            self.uyari()
        else:
            if self.kombo.get():
                from kayitlar import Uyari_2
                self.uyari_2 = Uyari_2()

    def kalici_sil_anahtar(self):
        self.tablo_silici = 1
        self.kalici_sil_islem()

    def kalici_sil_islem(self):
        if bool(self.tablo_silici) == True:
            self.delete = db_lite_5(self.Tablo,self.yoket,
                                    self.yoket_2,self.yoket_3,
                                    self.yoket_4,self.yoket_5,
                                    self.yoket_6,self.yoket_7,
                                    self.tablo_silici)
            if self.Tablo == 'Gelir Tablo':
                    self.tablo_sil()
                    self.tablo_gelir_baslik()
                    self.tablo_liste_baslik_renk()
                    self.lb1.insert(END,'veri silindi!')
                    self.lb1.itemconfig(END, {'fg': 'red'})
                    self.lb2.insert(END,'veri silindi!')
                    self.lb3.insert(END,'veri silindi!')
                    self.lb3.itemconfig(END, {'fg': 'red'})
                    self.lb4.insert(END,'veri silindi!')
            elif self.Tablo == 'Gider Tablo':
                    self.tablo_sil()
                    self.tablo_gider_baslik()
                    self.tablo_liste_baslik_renk()
                    self.lb1.insert(END,'veri silindi!')
                    self.lb1.itemconfig(END, {'fg': 'red'})
                    self.lb2.insert(END,'veri silindi!')
                    self.lb3.insert(END,'veri silindi!')
                    self.lb3.itemconfig(END, {'fg': 'red'})

            self.Tablo = ''
            self.yoket = 0
            self.yoket_2 = 0
            self.yoket_3 = 0
            self.yoket_4 = 0
            self.yoket_5 = 0
            self.yoket_6 = 0
            self.yoket_7 = 0
            self.bul_islem = False
            self.tablo_silici = 0


    def uyari(self):
        self.uyari_root = Tk()
        self.uyari_root.tk_setPalette('#9fb6cd')
        self.uyari_root.geometry('470x150')
        self.metin = "Tablonuzdan, veri silme talebinde bulundunuz."
        self.metin2 = "Devam ederseniz, tablo üzerindeki verileriniz,"
        self.metin3 = "kalıcı olarak SİLİNECEKTİR!"
        self.sil_onay = 'Yok et'
        self.uyari_gui()

    def uyari_gui(self):
        self.uyarStr = StringVar(self.uyari_root)
        self.uyarStr.set(self.metin)
        self.uyarStr2 = StringVar(self.uyari_root)
        self.uyarStr2.set(self.metin2)
        self.uyarStr3 = StringVar(self.uyari_root)
        self.uyarStr3.set(self.metin3)
        self.uyari_root.title('Uyari')
        self.uyari_b = Label(self.uyari_root,text='UYARI!!!',font='Courier 11 bold')
        self.uyari_b['fg'] = '#cd2626'
        self.uyari_b.grid(column=0,row=0,pady=3,sticky=N)

        self.uyari_l = Label(self.uyari_root,textvariable=self.uyarStr)
        self.uyari_l['font'] = 'Courier 11 bold'
        self.uyari_x = Label(self.uyari_root,textvariable=self.uyarStr2)
        self.uyari_x['font'] = 'Courier 11 bold'
        self.uyari_y = Label(self.uyari_root,textvariable=self.uyarStr3)
        self.uyari_y['font'] = 'Courier 11 bold'
        self.uyari_l.grid(column=0,row=1,padx=30)
        self.uyari_x.grid(column=0,row=2,padx=30)
        self.uyari_y.grid(column=0,row=3,padx=30)

        self.uyari_cikis = Button(self.uyari_root,text='İptal')
        self.uyari_cikis['width'] = 9
        self.uyari_cikis['font'] = 'Arial 11 bold'
        self.uyari_cikis['bg'] = '#e0eeee',
        self.uyari_cikis['fg'] = '#1c1c1c',
        self.uyari_cikis['command'] = self.uyari_root.destroy
       # self.uyari_cikis.grid(column=0,row=5,ipady=3)
        self.uyari_cikis.place(relx=0.1,rely=0.7)
        self.uyari_kabul = Button(self.uyari_root,text='Sil')
        self.uyari_kabul['width'] = 9
        self.uyari_kabul['font'] = 'Monospace 11 bold'
        self.uyari_kabul['bg'] = '#e0eeee',
        self.uyari_kabul['fg'] = '#1c1c1c',
        self.uyari_kabul['command'] = self.buton_sil
       # self.uyari_kabul.grid(column=0,row=5,ipady=3)
        self.uyari_kabul.place(relx=0.7,rely=0.7)

    def buton_sil(self):
        self.kalici_sil_anahtar()
        self.buton_iptal()

    def buton_iptal(self,event=None):
        self.uyari_root.destroy()
        


if __name__ == '__main__':
    uyg = Kontrol()
    mainloop()


class Postaci():
    Ppostaci_kayitlar = []

    def __init__(self, tablom):
        self.tablom = tablom
        self.Ppostaci_kayitlar.extend(self.tablom)
        self.tablom.clear()
# self.posta_al()

    @classmethod
    def posta_al(self):
        self.Ppostaci_kayitlar.extend(self.tablom)

class Postaci2():
    'parametre listeleri'
    postaci_gelir_liste = []
    postaci_musteriler_liste = []
    postaci_gider_liste = []
    postaci_gelir_arsiv = []
    postaci_musteri_arsiv = []
    postaci_gider_arsiv = []

    def __init__(self,*args):
        self.liste1 = args[0]
        self.liste2 = args[1]
        self.liste3 = args[2]
        self.gelir_turu_ars = args[3]
        self.musteri_ars = args[4]
        self.gider_turu_ars = args[5]

        self.postaci_gelir_liste.extend(self.liste1)
        self.postaci_musteriler_liste.extend(self.liste2)
        self.postaci_gider_liste.extend(self.liste3)
        self.postaci_gelir_arsiv.extend(self.gelir_turu_ars)
        self.postaci_musteri_arsiv.extend(self.musteri_ars)
        self.postaci_gider_arsiv.extend(self.gider_turu_ars)
        self.liste1.clear()
        self.liste2.clear()
        self.liste3.clear()
        self.gelir_turu_ars.clear()
        self.musteri_ars.clear()
        self.gider_turu_ars.clear()

class Uyari_2(object):
    
    def __init__(self):
        self.uyari_root = Tk()
        self.uyari_root.tk_setPalette('#9fb6cd')
        self.uyari_root.geometry('520x150')
        self.metin = "Tablonuz, ani silme talebine karşı koruma altındadır.."
        self.metin2 = "Veri silme talebi için 'Tablo parametreleri' ve "
        self.metin3 = "'Bul' butonunu kullanın... "
        self.uyari_gui()

    def uyari_gui(self):
        self.uyarStr = StringVar(self.uyari_root)
        self.uyarStr.set(self.metin)
        self.uyarStr2 = StringVar(self.uyari_root)
        self.uyarStr2.set(self.metin2)
        self.uyarStr3 = StringVar(self.uyari_root)
        self.uyarStr3.set(self.metin3)
        self.uyari_root.title('Uyari')
        self.uyari_b = Label(self.uyari_root,text='UYARI!!!',font='Courier 11 bold')
        self.uyari_b['fg'] = '#cd2626'
        self.uyari_b.grid(column=0,row=0,pady=3,sticky=N)

        self.uyari_l = Label(self.uyari_root,textvariable=self.uyarStr)
        self.uyari_l['font'] = 'Courier 11 bold'
        self.uyari_x = Label(self.uyari_root,textvariable=self.uyarStr2)
        self.uyari_x['font'] = 'Courier 11 bold'
        self.uyari_y = Label(self.uyari_root,textvariable=self.uyarStr3)
        self.uyari_y['font'] = 'Courier 11 bold'
        self.uyari_l.grid(column=0,row=1,padx=30)
        self.uyari_x.grid(column=0,row=2,padx=30)
        self.uyari_y.grid(column=0,row=3,padx=30)

        self.uyari_kabul = Button(self.uyari_root,text='Tamam')
        self.uyari_kabul['width'] = 9
        self.uyari_kabul['font'] = 'Monospace 11 bold'
        self.uyari_kabul['bg'] = '#e0eeee',
        self.uyari_kabul['fg'] = '#1c1c1c',
        self.uyari_kabul['command'] = self.buton_tamam
       # self.uyari_kabul.grid(column=0,row=5,ipady=3)
        self.uyari_kabul.place(relx=0.7,rely=0.7)

    def buton_tamam(self,event=None):
        self.uyari_root.destroy()
        



