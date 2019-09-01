# -*-coding=utf-8-*-

import sys
import time
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
#from giderTablosu import GiderTablo as git
from tablolar import GiderTablo as git
from tablolar import Gider_Arsiv
from datetime import datetime


class Uyari(object):

    def __init__(self,uyari_kontrol,param_2):
        self.uyari_kontrol = uyari_kontrol
        self.param_2 = param_2
        self.format_1 = ''
        self.format_2 = ''
        self.format_3 =''
        self.pgen = 0
        self.pyuks = 0
        self.veri_mevcut = False
        self.uyari_kontrol_mekanizma()

    def uyari_kontrol_mekanizma(self):
        if self.uyari_kontrol == 1:
            self.format_1 = 'Tarih girilmedi'
            self.format_2 = 'Tarih girişi yapın'
            self.uyari_konum()
        elif self.uyari_kontrol == 2:
            self.format_1 = 'İşlenemedi!!!'
            self.format_2 = 'Veri zaten mevcut'
            self.veri_mevcut = True
            self.uyari_konum()
        elif self.uyari_kontrol == 3:
            self.format_1 = 'Gider işlenmedi'
            self.format_2 = '12 basamak sınırı'
            self.uyari_konum()
        elif self.uyari_kontrol == 4:
            self.format_1 = 'İçerik hatası'
            self.format_2 = 'Harf veya rakam girişi yapın'
            self.uyari_konum()
        elif self.uyari_kontrol == 5:
            self.format_1 = 'Gider işlenmedi'
            self.format_2 = 'Rakam girişi yapın'
            self.uyari_konum()
        elif self.uyari_kontrol == 6:
            self.format_1 = 'Tarih girilmedi'
            self.format_2 = "Girilen gün henüz yaşanmadı"
            self.uyari_konum()
        elif self.uyari_kontrol == 7:
            self.format_1= 'Gider türü seçilmedi'
            self.format_2 = 'Listeden seçin'
            self.uyari_konum()
        elif self.uyari_kontrol == 8:
            self.format_1 = 'Gider türü silinmedi'
            self.format_2 = 'Silmek istediğiniz öğeyi seçin'
            self.uyari_konum()
        elif self.uyari_kontrol == 9:
            self.format_1 = 'İçerik hatası'
            self.format_2 = '16 karakter sınırı'
            self.uyari_konum()



    def uyari_konum(self):
        self.uyari_pencere = Tk()
        if self.veri_mevcut == True:
            self.pgen = 460
            self.pyuks = 100
        elif self.veri_mevcut == False:
            self.pgen = 320
            self.pyuks = 85



        self.ekrangen = self.uyari_pencere.winfo_screenwidth()
        self.ekranyuks = self.uyari_pencere.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 2
        self.y = (self.ekranyuks - self.pyuks) / 2

        self.uyari_pencere.geometry('%dx%d+%d+%d' % (self.pgen, self.pyuks,
                                               self.x, self.y))
        self.uyari()


    def uyari(self):

        'uyari penceresi'
        self.uyari_pencere.tk_setPalette('#9fb6cd')
        self.uyari_pencere.resizable(width=FALSE, height=FALSE)
        self.uyari_pencere.bind('<FocusOut>',self.uyari_cikis)
        self.uyari_pencere.bind('<Return>',self.uyari_cikis)
        self.uyari_pencere.bind('<Escape>',self.uyari_cikis)
        self.uyari_titlE = self.uyari_pencere.title('UYARI')
        self.uyari_etiket = Label(self.uyari_pencere, text='{}!!!'.format(
                            self.format_1), font='Courier 12 bold', fg='#cd2626')
        self.uyari_etiket.pack()
        self.uyari_etiket_2 = Label(self.uyari_pencere, text='{}!'.format(self.format_2),
                           font='Courier 12 bold', fg='black')
        self.uyari_etiket_2.pack()
        if self.veri_mevcut == True:
            self.uyari_etiket_3 = Label(self.uyari_pencere,text='{}'.format(self.param_2),
                                        font='Courier 12 bold')
            self.uyari_etiket_3.pack()

        self.veri_mevcut = False


    def uyari_cikis(self,event=None):
        self.uyari_pencere.destroy()


class Gider_ekle(object):
    def __init__(self):
        self.gider_liste_kontrol = False
        self.gider_veri_tarih = 0
        self.gider_veri_gider = 0
        self.gider_Item_sakla_1 = []
        self.gider_Item_sakla_2 = []
        self.tarih_gider_sayi = []
        self.tarih_gider_gun = []
        self.tarih_gider_ay = []
        self.liste_gider_sil = 0
        self.gider_item_yolla = []
        self.param_1 = 'P1:'
        self.param_2 = [] # for uyari()
        self.sistem_saati_yil = datetime.now().year
        self.sistem_saati_ay = datetime.now().strftime('%m')
        self.sistem_saati_gun = datetime.now().strftime('%d')
        self.bugun = datetime.now().strftime('%d.%m.%Y')
        self.bugun_vt = datetime.now().strftime('%Y.%m.%d')
        self.gui_gider_ekle_total = 0
        self.pgen = 0
        self.pyuks = 0
        self.yeni_pencere_gider()


    def konum(self,gen,yuks,penc):
        self.pgen = gen
        self.pyuks = yuks
        self.penc = penc



        self.ekrangen = self.penc.winfo_screenwidth()
        self.ekranyuks = self.penc.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 2
        self.y = (self.ekranyuks - self.pyuks) / 2.6

        self.penc.geometry('%dx%d+%d+%d' % (self.pgen, self.pyuks,
                                               self.x, self.y))


    def yeni_pencere_gider(self):
        self.gider_pencere = Tk()
        self.gider_pencere.tk_setPalette('#9fb6cd')
        self.konum(350,405,self.gider_pencere)

        self.gider_pencere.resizable(width=FALSE, height=FALSE)
        self.titlE = self.gider_pencere.title('CUT GİDER GİR')
        self.kapa = self.gider_pencere.protocol('WM_DELETE_WINDOW', self.gider_cikis)
        self.gider_pencere.bind('<Return>',self.gider_kontrol_mekanizma)
        self.gider_pencere.bind('<Escape>',self.gider_cikis)
        self.etiket_gider = Label(
            self.gider_pencere, text='Gider Türü Liste', font='Courier 12 bold')
        self.etiket_gider.grid(column=0,row=0)
        self.liste_gider = Listbox(self.gider_pencere,height=12,width=22)
        self.liste_gider['relief'] = 'raised'
        self.liste_gider['font'] = 'Arial 11'
        self.liste_gider['bg'] = '#f2f2f2'
        self.liste_gider['fg'] = "black"
        self.liste_gider.bind('<Double-Button-1>', self.gider_gosterici)
        self.liste_gider.grid(column=0,row=1, ipady=50)



        self.gider_tarih_cerceve = Frame(self.gider_pencere)
        self.gider_tarih_cerceve['relief'] = 'groove'
        self.gider_tarih_cerceve['bd'] = 1
        self.gider_tarih_cerceve.grid(column=1,row=1,padx=5,pady=5,ipady=22,sticky=N)

        self.gui_gider_tarih_label = Label(self.gider_tarih_cerceve, text='Tarih Ekle',
                                           font='Courier 12 bold')
        self.gui_gider_tarih_label.grid(padx=5,pady=7)

        self.gider_ic_cerceve =  Frame(self.gider_tarih_cerceve)
        self.gider_ic_cerceve['bd'] = 2
        self.gider_ic_cerceve['relief'] = 'groove'
        self.gider_ic_cerceve.grid(padx=5, pady=5, ipady=9)
        self.gui_gider_bugun = StringVar(self.gider_pencere)
        self.gui_gider_bugun.set(self.bugun)
        self.gider_tarih_gosterInt = IntVar(self.gider_pencere)
        self.gider_tarih_gosterInt.set(1)
        self.gui_gider_tar_bugun = Checkbutton(self.gider_ic_cerceve,width=10,
                                               variable=self.gider_tarih_gosterInt,
                                               textvariable=self.gui_gider_bugun,
                                               font='Courier 12 bold')
        self.gui_gider_tar_bugun.grid(sticky=W)
        self.gui_gider_tarih_ekle_1 = ttk.Combobox(
            self.gider_ic_cerceve, font="Arial 11", width=3)
        self.gui_gider_tarih_ekle_1.grid(sticky=NW,row=1,padx=5)
        self.sayac(1, 31)
        self.tarih_gider_gun.extend(self.tarih_gider_sayi)
        self.gui_gider_tarih_ekle_1['value'] = (self.tarih_gider_gun)
        self.tarih_gider_sayi.clear()

        self.gider_gui_tarih_ekle_2 = Label(self.gider_ic_cerceve,
                                                font='Courier 12 bold', width=3)
        self.gider_gui_tarih_ekle_2['text'] = self.sistem_saati_ay
        self.gider_gui_tarih_ekle_2.grid(row=1)

        self.gider_gui_tarih_ekle_3 = Label(self.gider_ic_cerceve,
                                                font='Courier 12 bold', width=5)
        self.gider_gui_tarih_ekle_3['text'] = self.sistem_saati_yil
        self.gider_gui_tarih_ekle_3.grid(sticky=E,row=1,padx=2)

        self.gui_gider_label = Label(self.gider_tarih_cerceve, text='Gider Ekle',
                                     font='Courier 12 bold')
        self.gui_gider_label.grid(padx=5,row=4,pady=7)
        self.gui_gider_ekle = Entry(self.gider_tarih_cerceve,width=16,
                                    font="Arial 11",
                                    bg='#f2f2f2', fg='black')
        self.gui_gider_ekle.grid(pady=7,row=5)
        if sys.platform == 'win32':
            self.gui_gider_btn = Button(self.gider_tarih_cerceve, text='Tamam',width=13,
                                        font='Arial 12',
                                        bg='#e0eeee',
    ##                                    bg='#cfcfcf',
                                        fg='#1c1c1c',
                                        command=self.gider_kontrol_mekanizma)
        else:
            self.gui_gider_btn = Button(self.gider_tarih_cerceve, text='Tamam',width=11,
                                        font='Arial 12',
                                        bg='#e0eeee',
    ##                                    bg='#cfcfcf',
                                        fg='#1c1c1c',
                                        command=self.gider_kontrol_mekanizma)
        self.gui_gider_btn.grid(pady=2)

        self.p1 = StringVar(self.gider_pencere)
        self.p1.set(self.param_1)
        self.etiket_param = Label(self.gider_tarih_cerceve,
                                   textvariable=self.p1,
                                   font='Courier 12 bold')
        self.etiket_param.bind('<Double-Button-1>', self.gider_gosterici)
        self.etiket_param.grid(sticky=W,pady=10)


        self.cerceve_gider_2 = Frame(self.gider_pencere,width=20)
        self.cerceve_gider_2['bd'] = 2
        self.cerceve_gider_2['relief'] = 'groove'
        self.cerceve_gider_2.grid(column=0,row=2,padx=3)
        if sys.platform == 'win32':
            self.btn_gider_pen2 = Button(self.cerceve_gider_2, text='Ekle',width=9,
                                         font='Arial 12',
                                         bg='#e0eeee', fg='#1c1c1c',
                                         command=self.nesne_gir_gider)
            self.btn_gider_sil = Button(self.cerceve_gider_2, text='Sil',width=9,
                                        font='Arial 12',
                                        bg='#e0eeee', fg='#1c1c1c',
                                        command=self.gider_sil)
            self.btn_gider_pen = Button(self.gider_pencere, text="Çıkış",width=13,
                                        font='Arial 12',
                                        bg='#e0eeee', fg='#1c1c1c',
                                        command=self.gider_cikis)
        else:
            self.btn_gider_pen2 = Button(self.cerceve_gider_2, text='Ekle',width=7,
                                         font='Arial 12',
                                         bg='#e0eeee', fg='#1c1c1c',
                                         command=self.nesne_gir_gider)
            self.btn_gider_sil = Button(self.cerceve_gider_2, text='Sil',width=7,
                                        font='Arial 12',
                                        bg='#e0eeee', fg='#1c1c1c',
                                        command=self.gider_sil)
            self.btn_gider_pen = Button(self.gider_pencere, text="Çıkış",width=11,
                                        font='Arial 12',
                                        bg='#e0eeee', fg='#1c1c1c',
                                        command=self.gider_cikis)
        self.btn_gider_pen2.grid(column=0,row=0)
        self.btn_gider_sil.grid(column=1,row=0)

        self.btn_gider_pen.grid(column=1,row=2,sticky=S)
        self.giderListe_kontrol()
        self.hatirla_sysclock()


    def hatirla_sysclock(self):
        self.strVar = StringVar(self.gider_pencere)
        self.strVar.set('Tarih kontrol:')
        self.hatirla_label = Label(self.gider_pencere,textvariable=self.strVar)
        self.hatirla_label['font'] = 'Arial 10 bold'
        self.hatirla_label.grid(column=0,row=5,sticky=W)
        self.strVar_2 = StringVar(self.gider_pencere)
        self.strVar_2.set(self.bugun)
        self.hatirla_label_2 = Label(self.gider_pencere,textvariable=self.strVar_2)
        self.hatirla_label_2['font'] = 'Arial 10 bold'
        self.hatirla_label_2.grid(column=0,row=5,sticky=SE)
        self.hatirla_label.after(9000,self.tarih_kont_close)
        self.hatirla_label.after(9000,self.tarih_kont_close)

  #      self.pencere4 = Toplevel(self.gider_pencere)
  #      self.pencere4.transient(self.gider_pencere)
  #      self.pencere4_titlE = self.pencere4.title('HATIRLATMA')
  #      self.konum(345,100,self.pencere4)
###        self.pencere4.geometry('300x100')

  #      self.etiket_4 = Label(self.pencere4,
  #                            text='Hatırlatma!!',
  #                            font= 'Courier 12 bold',
  #                            fg='blue')
  #      self.etiket_4.pack()
  #      self.etiket_5 = Label(self.pencere4,
  #                            text='Sistem tarihiniz doğru mu?',
  #                            font='Courier 12 bold',
  #                            fg='black')
  #      self.etk5 = StringVar(self.pencere4)
  #      self.etk5.set(self.bugun)
  #      self.etiket_5.pack()
  #      self.etiket_6 = Label(self.pencere4,
  #                            textvariable=self.etk5,
  #                            font='Courier 12 bold',
  #                            fg='#1c0f45')
  #      self.etiket_6.pack()
  #      self.pencere4.bind('<FocusOut>',self.hatirlatma_close)
  #      self.pencere4.bind('<Return>',self.hatirlatma_close)
  #      self.pencere4.bind('<Escape>',self.hatirlatma_close)
  #      self.pencere4.after(2000, self.hatirlatma_close)


  #  def hatirlatma_close(self,event=None):
  #      self.pencere4.destroy()

    def tarih_kont_close(self):
        self.strVar.set('')
        self.strVar_2.set('')



    def sayac(self, sayi, son):
        "manuel tarih girisi icin gün sayısı oluşturur"
        self.tarih_gider_sayi.append(str(sayi).zfill(2))
        if sayi == son:
            return None
        else:
            return self.sayac(sayi+1, son)

    def giderListe_kontrol(self):
        from veriTabani import veriTabani_4_giderliste_olustur
        self.giderliste_icerik = veriTabani_4_giderliste_olustur()
        from gider_ekle import Postaci
        self.gider_Item_sakla_2.extend(Postaci.Ppostaci)
        self.sil_2_Ppostaci = Postaci.Ppostaci.clear()
        for pstci in self.gider_Item_sakla_2:
            self.liste_gider.insert(END, pstci)

    def nesne_gir_gider(self):
        self.gider_pencere3 = Toplevel()
        self.konum(300,100,self.gider_pencere3)
##        self.gider_pencere3.geometry('250x100')
        self.nesne_gir_titlE = self.gider_pencere3.title('NESNE GİR')
        self.giris_gider_label = Label(self.gider_pencere3, text='gider türü gir',
                                       font='Courier 12 bold')
        self.giris_gider_label.pack()
        self.giris_gider = Entry(
            self.gider_pencere3, font='Arial 13', bg='#f2f2f2', fg='black')
        self.giris_gider.pack(expand=YES,fill=X)
        self.gider_cerceve3 = Frame(self.gider_pencere3)
        self.gider_cerceve3.pack(padx=1, pady=5)
        self.giris_gider_btn = Button(self.gider_pencere3, text='Tamam',
                                      font='Arial 12',
                                      bg='#e0eeee', fg='#1c1c1c',
                                      command=self.ekle_gider)
        self.giris_gider_btn.pack(side=LEFT, expand=YES, fill=X)
        self.kapa_gider_btn = Button(self.gider_pencere3, text='çıkış',
                                     font='Arial 12',
                                     bg='#e0eeee', fg='#1c1c1c',
                                     command=self.gider_pencere3.destroy)
        self.kapa_gider_btn.pack(side=RIGHT, expand=YES, fill=X)
        self.gider_pencere3.bind('<Return>',self.ekle_gider)
        self.gider_pencere3.bind('<Escape>',self.cikis_pencere3)

    def cikis_pencere3(self,event=None):
        return self.gider_pencere3.destroy()

    def ekle_gider(self,event=None):
        if not self.giris_gider.get():
            self.giris_gider.insert(END, 'Veri Yok!')
        if not 'Veri Yok!' in self.giris_gider.get():
            if len(self.giris_gider.get()) >= 17:
                self.uyari = Uyari(9,self.param_2)
            elif len(self.giris_gider.get()) <= 16:
                self.veri_islem_gider = self.giris_gider.get().replace('i', 'İ').upper()
                if self.veri_islem_gider.isalnum() == True:
                    self.gider_Item_sakla_1.append(self.veri_islem_gider)
                    self.yolla_to3 = Gider_Arsiv([1],self.veri_islem_gider)
                    for i in self.gider_Item_sakla_1:
                        if not i in self.gider_Item_sakla_2:
                            self.gider_Item_sakla_2.append(i)
                            self.giris_gider.delete(0, END)
                            self.liste_gider.delete(0, END)
                            for s in self.gider_Item_sakla_2:
                                self.liste_gider.insert(END, s)
                    self.gider_liste_tazele()

                else:
                    self.uyari = Uyari(4,self.param_2)
##
    def gider_sil(self):
        self.liste_gider_sil = self.liste_gider.get(ACTIVE)
        if bool(self.liste_gider_sil) == False:
            self.etiket_gider.configure(text='liste', fg='black')
        elif self.gider_liste_kontrol == False:
            self.uyari = Uyari(8,self.param_2)
        else:
            for i in self.gider_Item_sakla_1:
                if self.liste_gider_sil in i:
                    self.gider_Item_sakla_1.remove(self.liste_gider_sil)
            for z in self.gider_Item_sakla_2:
                if self.liste_gider_sil in z:
                    self.gider_Item_sakla_2.remove(self.liste_gider_sil)
            self.p1.set('siliniyor...')
            self.etiket_param.configure(fg='blue',font='Courier 12 bold')
            self.etiket_gider.update()
            time.sleep(0.8)
            self.p1.set('P1')
            self.etiket_param.configure(fg='black')
            self.liste_gider.delete(ACTIVE)
            self.gider_liste_kontrol = False
            if isinstance(self.liste_gider_sil,(str)):
                self.yolla_to3 = Gider_Arsiv([0],self.liste_gider_sil)
                self.gider_liste_tazele()

    def gider_gosterici(self, event):
        self.liste_gider_get_active = self.liste_gider.get(ACTIVE)
        self.p1.set(self.liste_gider_get_active)
        if len(self.liste_gider.get(ACTIVE)) <= 13:
            self.etiket_param.configure(fg='#1c0f45',font='Courier 12 bold')
        elif len(self.liste_gider.get(ACTIVE)) >= 13:
            self.etiket_param.configure(fg='#1c0f45',font='Arial 9 bold')

        self.etiket_param.update()
        self.gider_liste_kontrol = True

    def gider_veri_kontrol_fonksiyon(self):
        if self.gider_tarih_gosterInt.get() == 1:
            self.gider_veri_tarih = 1
        elif self.gider_tarih_gosterInt.get() == 0:
            if bool(self.gui_gider_tarih_ekle_1.get()) == False:
                self.uyari = Uyari(1,self.param_2)
            else:
                if bool(self.gui_gider_tarih_ekle_1.get()) == True:
                    if self.gui_gider_tarih_ekle_1.get() > self.sistem_saati_gun:
                        self.uyari = Uyari(6,self.param_2)
                    else:
                        self.gider_veri_tarih = 1

        try:
            if len(str(self.gui_gider_ekle.get())) < 13:
                self.gui_gider_ekle_total = float(self.gui_gider_ekle.get())
                if isinstance(self.gui_gider_ekle_total, (float)):
                    self.gider_veri_gider = 1
            else:
                self.uyari = Uyari(3,self.param_2)
                self.gider_veri_gider = 0

        except ValueError:
            self.uyari = Uyari(5,self.param_2)
            self.gider_veri_gider = 0

    def gider_veri_islem(self):
        'giderTablo.py >>'
        self.gui_gider_liste = git(self.liste_gider_get_active)
        if self.gider_tarih_gosterInt.get() == 1:
            self.gui_gider_liste.tarih_gider_ekle(self.bugun_vt)
        elif self.gider_tarih_gosterInt.get() == 0:
            self.gui_gider_liste.tarih_gider_ekle(str(self.sistem_saati_yil)+
                                                      '.' +str(self.sistem_saati_ay)+'.' +
                                              self.gui_gider_tarih_ekle_1.get())
        self.gui_gider_liste.gider_ekle(self.gui_gider_ekle_total)

        self.gui_gider_tarih_ekle_1.delete(0, END)
        self.gui_gider_ekle.delete(0, END)

        self.gider_veri_tarih = 0
        self.gider_veri_gider = 0

    def gider_kontrol_mekanizma(self,event=None):
        if self.gider_liste_kontrol == True:
            self.gider_veri_kontrol_fonksiyon()
            if all([self.gider_veri_tarih, self.gider_veri_gider]) == True:
                return self.gui_gider_tamam()

        else:
            self.uyari = Uyari(7,self.param_2)

    def gui_gider_tamam(self):
        self.gider_veri_islem()
        self.gider_liste_kontrol = False
        if self.gider_liste_kontrol == False:
            self.p1.set('işleniyor...')
            self.etiket_param.configure(fg='blue',font='Courier 12 bold')
            self.etiket_param.update()
            time.sleep(1)
            self.gui_veriler = self.gui_gider_liste.veriTabanına_yolla()
            self.p1.set('P1:')
            self.etiket_param.configure(fg='black')
            if self.gider_tarih_gosterInt.get() == 0:
                self.gider_tarih_gosterInt.set(1)

    def gider_liste_tazele(self):
        from veriTabani import VeriTabani_3 as dblite_3
        for i in self.gider_Item_sakla_2:
            i = (i,)
            self.gider_item_yolla.append(i)
        self.gider_liste_gonder = dblite_3(self.gider_item_yolla)

    def modul_kapa(self):
        'butonlar icin cut.py ye veri gönderir'
        from veriTabani import VeriTabani_7
        self.modul_kapanir = VeriTabani_7(2,'Gider Ekle')


    def gider_cikis(self,event=None):
        self.gider_liste_tazele()
        self.modul_kapa()
        self.gider_Item_sakla_1.clear()
        self.gider_Item_sakla_2.clear()
        self.liste_gider.delete(0, END)
        self.gider_pencere.destroy()


if __name__ == '__main__':
    uyg = Gider_ekle()
    mainloop()



class Postaci():
    Ppostaci = []

    def __init__(self, listem):
        self.listem = listem
        self.Ppostaci.extend(self.listem)
        self.listem.clear()

# self.posta_al()

    @classmethod
    def posta_al(self):
        self.Ppostaci.extend(self.listem)





