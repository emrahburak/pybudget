# -*- coding: utf-8 -*-

import sys
import time
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
#from gelirTablosu import GelirTablo as gtb
from tablolar import GelirTablo as gtb
from tablolar import G_Arsiv 
from tablolar import M_Arsiv
from datetime import datetime




class Uyari(object):

    def __init__(self,uyari_kontrol,param_2):
        self.uyari_kontrol = uyari_kontrol
        self.param_2 = param_2
        self.format_1 = ''
        self.format_2 = ''
        self.format_3 =''
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
            self.format_1 = 'Gelir işlenmedi'
            self.format_2 = 'Rakam girişi yapın'
            self.uyari_konum()
        elif self.uyari_kontrol == 4:
            self.format_1 = 'İçerik hatası'
            self.format_2 = 'Harf veya rakam girişi yapın'
            self.uyari_konum()
        elif self.uyari_kontrol == 5:
            self.format_1 = 'Tarih girilmedi'
            self.format_2 = "Girilen gün henüz yaşanmadı"
            self.uyari_konum()
        elif self.uyari_kontrol == 6:
            self.format_1 = 'Gelir türü silinmedi'
            self.format_2 = 'Silmek istediğiniz öğeyi seçin'
            self.uyari_konum()
        elif self.uyari_kontrol == 7:
            self.format_1 = 'Müşteriler silinmedi'
            self.format_2 = 'Silmek istediğiniz öğeyi seçin'
            self.uyari_konum()
        elif self.uyari_kontrol == 8:
            self.format_1 = 'Gelir türü seçilmedi'
            self.format_2 = 'Listeden seçin'
            self.uyari_konum()
        elif self.uyari_kontrol == 9:
            self.format_1 = 'Müşteri seçilmedi'
            self.format_2 = 'Listeden seçin'
            self.uyari_konum()
        elif self.uyari_kontrol == 10:
            self.format_1 = 'Gelir İşlenmedi'
            self.format_2 = '12 basamak sınırı'
            self.uyari_konum()
        elif self.uyari_kontrol == 11:
            self.format_1 = 'İçerik hatası'
            self.format_2 = '16 karakter sınırı'
            self.uyari_konum()


    def uyari_konum(self):
        self.uyari_pencere = Tk()
        if self.veri_mevcut == True:
            self.pgen = 580
            self.pyuks = 100
        elif self.veri_mevcut == False:
            self.pgen = 320
            self.pyuks = 85


        self.ekrangen = self.uyari_pencere.winfo_screenwidth()
        self.ekranyuks = self.uyari_pencere.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 4.9
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


class Gelir_ekle(object):
    def __init__(self,*args,**kwagrs):

        self.liste_kontrol = False
        self.liste_2_kontrol = False
        self.ekle_sayac = []
        self.veri_tarih = 0
        self.veri_musteri = 0
        self.veri_gelir = 0
        self.gelir_Item_sakla_1 = []
        self.gelir_Item_sakla_2 = []
        self.gelir_Item_sakla_3 = []
        self.gelir_Item_sakla_4 = []
        self.item_yolla = []
        self.item_yolla2 = []
        self.tarih_sayi = []
        self.tarih_gun = []
        self.liste_sil = 0
        self.liste_2_sil = 0
       # self.tarih_ay = []
        self.param_2 = [] # for uyari
        self.sistem_saati_yil = datetime.now().strftime('%Y')
        self.sistem_saati_ay = datetime.now().strftime('%m')+'.'
        self.sistem_saati_gun = str(datetime.now().day)
        self.bugun = datetime.now().strftime('%d.%m.%Y')
        self.bugun_vt = datetime.now().strftime('%Y.%m.%d')
        self.gui_gelir_ekle_total = 0
        from gelir_ekle import Uyari
        self.yeni()


    def konum(self,gen,yuks,penc):
        self.pgen = gen
        self.pyuks = yuks
        self.penc = penc



        self.ekrangen = self.penc.winfo_screenwidth()
        self.ekranyuks = self.penc.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 4.9
        self.y = (self.ekranyuks - self.pyuks) / 1.7

        self.penc.geometry('%dx%d+%d+%d' % (self.pgen, self.pyuks,
                                               self.x, self.y))


    def yeni(self,*args,**kwargs):
        self.pencere2 = Tk()
        self.pencere2.tk_setPalette('#9fb6cd')
        self.konum(370,530,self.pencere2)
        self.pencere2.resizable(width=FALSE, height=FALSE)
        self.titlE = self.pencere2.title('CUT GELİR GİR',)
        self.kapa = self.pencere2.protocol('WM_DELETE_WINDOW', self.cikis)
        self.pencere2.bind('<Return>',self.kontrol_mekanizma)
        self.pencere2.bind('<Escape>',self.cikis)


        self.cbk_1b = BooleanVar(self.pencere2)
        self.cbk_1b.set(True)
        self.etiket_1b = Checkbutton(self.pencere2,text='Gelir Türü Liste',
                                     variable=self.cbk_1b, onvalue = True,
                                     offvalue=False,
                                    font='Courier 12 bold',
                                     command=self.liste_dgsA)

        self.etiket_1b.grid(column=0,row=0,pady=1)
        self.liste = Listbox(self.pencere2,width=22)
        self.liste['relief'] = 'raised'
        self.liste['font'] = 'Arial 11'
        self.liste['bg'] = '#f2f2f2'
        self.liste['fg'] = 'black'
        self.liste.bind("<Double-Button-1>", self.gosterici)
        self.liste.grid(column=0,row=1, ipady=7,pady=1)

        self.cbk_2b = BooleanVar(self.pencere2)
        self.cbk_2b.set(False)
        self.etiket_2 = Checkbutton(self.pencere2, text='Müşteriler',
                                    variable=self.cbk_2b,onvalue = True,
                                      font='Courier 12 bold',
                                    command=self.liste_dgsB)

        self.etiket_2.grid(column=0,row=2,sticky=W)

        self.liste_2 = Listbox(self.pencere2,width=22)
        self.liste_2['relief'] = 'raised'
        self.liste_2['font'] = 'Arial 11'
        self.liste_2['bg'] = '#f2f2f2'
        self.liste_2['fg'] = "black"
        self.liste_2.bind("<Double-Button-1>", self.gosterici_B)
        self.liste_2.grid(column=0,row=3,ipady=7)



        self.cerceve = Frame(self.pencere2)
        self.cerceve['bd'] = 2
        self.cerceve['relief'] = 'groove'
        self.cerceve.grid(column=2,row=1,padx=5, pady=5, ipady=9,sticky=NE)


        self.tarih_label = Label(self.cerceve, text='Tarih ekle:',
                                 font='Courier 12 bold')
        self.tarih_label.grid(padx=5)

        self.tarih_cerceve = Frame(self.cerceve)
        self.tarih_cerceve['relief'] = GROOVE
        self.tarih_cerceve['bd'] = 1
        self.tarih_cerceve.grid(pady=2, ipady=4,padx=5)

        self.gui_tarih_goster = StringVar(self.pencere2)
        self.gui_tarih_goster.set(self.bugun)
        self.gui_tarih_gosterInt = IntVar(self.pencere2)
        self.gui_tarih_gosterInt.set(1)
        self.gui_tarih = Checkbutton(self.tarih_cerceve,width=10,
                                     textvariable=self.gui_tarih_goster,
                                     variable=self.gui_tarih_gosterInt,
                                     font='Courier 12 bold')
        self.gui_tarih.grid(sticky=W)

        self.gui_tarih_ekle_1 = ttk.Combobox(
            self.tarih_cerceve, font="Arial 11",width=3)

        self.gui_tarih_ekle_1.grid(sticky=NW,row=1,padx=5)
        self.sayac(1, 31)
        self.tarih_gun.extend(self.tarih_sayi)
        self.gui_tarih_ekle_1['value'] = (self.tarih_gun)

       # self.tarih_sayi.clear()

        self.gui_tarih_ekle_2 = Label(
            self.tarih_cerceve, font='Courier 12 bold',)
        self.gui_tarih_ekle_2.grid(row=1)
        self.gui_tarih_ekle_2['text'] = self.sistem_saati_ay

        self.gui_tarih_ekle_3 = Label(
            self.tarih_cerceve, font='Courier 12 bold',)
        self.gui_tarih_ekle_3['text'] = self.sistem_saati_yil
        self.gui_tarih_ekle_3.grid(sticky=E,row=1,padx=2)


        self.gelir_label = Label(self.cerceve, text='Gelir ekle:',
                                 font='Courier 12 bold')
        self.gelir_label.grid(padx=5,pady=10)
        self.gui_gelir_ekle = Entry(self.cerceve, font="Arial 11" ,width=16)
        self.gui_gelir_ekle['bg'] = '#f2f2f2'
        self.gui_gelir_ekle['fg'] = "black"
        self.gui_gelir_ekle.grid(sticky=N)

        if sys.platform == 'win32':
            self.gelir_btn = Button(self.cerceve, text='Tamam',width=13,
                                    font='Arial 12',
                                    bg='#e0eeee',
                                    fg='#1c1c1c',
                                    command=self.kontrol_mekanizma)
        else:
            self.gelir_btn = Button(self.cerceve, text='Tamam',width=11,
                                    font='Arial 12',
                                    bg='#e0eeee',
                                    fg='#1c1c1c',
                                    command=self.kontrol_mekanizma)
        self.gelir_btn.grid(pady=5)

        self.etiket = Label(self.pencere2, text='p1:',
                            font='Courier 12 bold')
        self.etiket.grid(column=2,row=2,sticky=W)
        self.et3 = StringVar(self.pencere2)
        self.et3.set('p2:')
        self.etiket_3 = Label(self.pencere2,textvariable=self.et3,
                              font='Courier 12 bold')
        self.etiket_3.grid(column=2 ,row=3,sticky=W)

        self.cerceve_2 = Frame(self.pencere2)
        self.cerceve_2['bd'] = 2
        self.cerceve_2['relief'] = 'groove'
        self.cerceve_2.grid(column=0)

        if sys.platform == 'win32':
            self.btn_pen2 = Button(self.cerceve_2, text='Ekle',width=9,
                                   font='Arial 12',
                                   bg='#e0eeee', fg='#1c1c1c',
                                   command=self.nesne_gir)
            self.btn_sil = Button(self.cerceve_2, text='Sil',width=9,
                                  font='Arial 12',
                                  bg='#e0eeee', fg='#1c1c1c',
                                  command=self.sil_onay)
        else:
            self.btn_pen2 = Button(self.cerceve_2, text='Ekle',width=7,
                                   font='Arial 12',
                                   bg='#e0eeee', fg='#1c1c1c',
                                   command=self.nesne_gir)
            self.btn_sil = Button(self.cerceve_2, text='Sil',width=7,
                                  font='Arial 12',
                                  bg='#e0eeee', fg='#1c1c1c',
                                  command=self.sil_onay)
            
        self.btn_pen2.grid(column=0,)
        self.btn_sil.grid(column=1,row=0)

        if sys.platform == 'win32':
            self.btn_pen = Button(self.pencere2, text="Çıkış",width=13,
                                  font='Arial 12',
                                  bg='#e0eeee', fg='#1c1c1c',
                                  command=self.cikis)
        else:
            self.btn_pen = Button(self.pencere2, text="Çıkış",width=11,
                                  font='Arial 12',
                                  bg='#e0eeee', fg='#1c1c1c',
                                  command=self.cikis)
        self.btn_pen.grid(column=2,row=4)
        self.gelirListe_kontrol()
        self.hatirla_sysclock()


    def hatirla_sysclock(self):
        self.strVar = StringVar(self.pencere2)
        self.strVar.set('Tarih kontrol:')
        self.hatirla_label = Label(self.pencere2,textvariable=self.strVar)
        self.hatirla_label['font'] = 'Arial 10 bold'
        self.hatirla_label.grid(column=0,row=5,sticky=W)
        self.strVar_2 = StringVar(self.pencere2)
        self.strVar_2.set(self.bugun)
        self.hatirla_label_2 = Label(self.pencere2,textvariable=self.strVar_2)
        self.hatirla_label_2['font'] = 'Arial 10 bold'
        self.hatirla_label_2.grid(column=0,row=5,sticky=SE)
        self.hatirla_label.after(9000,self.tarih_kont_close)
        self.hatirla_label.after(9000,self.tarih_kont_close)

    #    self.pencere4 = Toplevel(self.pencere2)
    #    self.pencere4.tk_setPalette('#9fb6cd')
    #    self.pencere4.transient(self.pencere2)
    #    self.pencere4_titlE = self.pencere4.title('HATIRLATMA')
    #    self.konum(300,100,self.pencere4)


    #    self.etiket_4 = Label(self.pencere4,
    #                          text='Hatırlatma!!',
    #                          font= 'Courier 12 bold',
    #                          fg='blue')
    #    self.etiket_4.pack()
    #    self.etiket_5 = Label(self.pencere4,
    #                          text='Sistem tarihiniz doğru mu?',
    #                          font='Courier 12 bold',
    #                          fg='black')
    #    self.etk5 = StringVar(self.pencere4)
    #    self.etk5.set(self.bugun)
    #    self.etiket_5.pack()
    #    self.etiket_6 = Label(self.pencere4,
    #                          textvariable=self.etk5,
    #                          font='Courier 12 bold',
    #                          fg='#1c0f45')
    #    self.etiket_6.pack()
    #    self.pencere4.bind('<FocusOut>',self.hatirlatma_close)
    #    self.pencere4.bind('<Return>',self.hatirlatma_close)
    #    self.pencere4.bind('<Escape>',self.hatirlatma_close)
    #    self.run_after = True
    #    if self.run_after:
    #        self.after = self.pencere4.after(2000, self.hatirlatma_close)
 

    def tarih_kont_close(self):
        self.strVar.set('')
        self.strVar_2.set('')

   # def hatirlatma_close(self,event=None):
   #     self.run_after = False
   #     self.pencere4.destroy()



    def liste_dgsA(self):
        if self.cbk_1b.get() == True:
            self.cbk_2b.set(False)
        elif self.cbk_1b.get() == False:
            self.cbk_2b.set(True)


    def liste_dgsB(self):
        if self.cbk_2b.get() == True:
            self.cbk_1b.set(False)
        elif self.cbk_2b.get() == False:
            self.cbk_1b.set(True)


    def sayac(self,sayi, son):
        self.tarih_sayi.append(str(sayi).zfill(2))
        if sayi == son:
            return None
        else:
            return self.sayac(sayi+1, son)


    def gelirListe_kontrol(self):
        'gelir türü ve müşterilerin veri tabanından ilk girişi'
        from veriTabani import veriTabani_2B_listeler
        self.gelirliste_icerik = veriTabani_2B_listeler()
        from gelir_ekle import Postaci
        self.gelir_Item_sakla_2.extend(Postaci.Ppostaci)
        self.sil_Ppostaci = Postaci.Ppostaci.clear()
        self.gelir_Item_sakla_3.extend(Postaci.PTpostaci)
        self.sil_2PTpostaci = Postaci.PTpostaci.clear()
        for pstci in self.gelir_Item_sakla_2:
            self.liste.insert(END, pstci)
        for ptt in self.gelir_Item_sakla_3:
            self.liste_2.insert(END,ptt)


    def nesne_gir(self):
        self.pencere3 = Toplevel()
        self.nesne_gir_titlE = self.pencere3.title('NESNE GİR')
        self.konum(300,100,self.pencere3)
        if self.cbk_1b.get() == True:
            self.giris_label = Label(self.pencere3, text='gelir gir',
                                 font='Courier 12 bold')
            self.giris_label.pack()
        elif self.cbk_2b.get() == True:
            self.giris_label_2 = Label(self.pencere3,text='müşteri gir',
                                     font='Courier 12 bold')
            self.giris_label_2.pack()
        self.giris = Entry(self.pencere3, font='Arial 13')
        self.giris['bg'] = '#f2f2f2'
        self.giris['fg'] = "black"
        self.giris.pack(expand=YES,fill=X)
        self.cerceve3 = Frame(self.pencere3)
        self.cerceve3.pack(padx=1, pady=5)
        self.giris_btn = Button(self.pencere3, text='Tamam',
                                font='Arial 12',
                                bg='#e0eeee',  fg='#1c1c1c',
                                command=self.ekle_onay)
        self.giris_btn.pack(side=LEFT, expand=YES, fill=X)
        self.kapa_btn = Button(self.pencere3, text='çıkış',
                               font='Arial 12',
                               bg='#e0eeee', fg='#1c1c1c',
                               command=self.pencere3.destroy)
        self.kapa_btn.pack(side=RIGHT, expand=YES, fill=X)
        self.pencere3.bind('<Return>',self.ekle_onay)
        self.pencere3.bind('<Escape>',self.cikis_pencere3)

    def cikis_pencere3(self,event=None):
        return self.pencere3.destroy()


    def ekle_onay(self,event=None):
        if self.cbk_1b.get() == True:
            self.ekle()
        elif self.cbk_2b.get() == True:
            self.ekle_2()


    def ekle(self):
        if not self.giris.get():
            self.giris.insert(END, 'Veri Yok!')
        if not 'Veri Yok!' in self.giris.get():
            if len(self.giris.get()) >= 17:
                self.uyari = Uyari(11,self.param_2)
            elif len(self.giris.get()) <= 16:
                self.gelir_veri_islem = self.giris.get().replace('i','İ').upper()
                if self.gelir_veri_islem.isalnum() == True:
                   self.gelir_Item_sakla_1.append(self.gelir_veri_islem)
                   self.yolla_to = G_Arsiv([1],self.gelir_veri_islem) #to tablolar.py
                   for i in self.gelir_Item_sakla_1:
                        if not i in self.gelir_Item_sakla_2:
                            self.gelir_Item_sakla_2.append(i)
                            self.giris.delete(0, END)
                            self.liste.delete(0, END)
                            for s in self.gelir_Item_sakla_2:
                                self.liste.insert(END, s)
                   self.listeleri_tazele()
                else:
                    self.uyari = Uyari(4,self.param_2)


    def ekle_2(self):
        if not self.giris.get():
            self.giris.insert(END, 'Veri Yok!')
        if not 'Veri Yok!' in self.giris.get():
            if len(self.giris.get()) >= 17:
                   self.uyari = Uyari(11,self.param_2)
            elif len(self.giris.get()) <= 16:
                self.musteriler_islem = self.giris.get().replace('i','İ').upper()
                if self.musteriler_islem.isalnum() == True:
                    self.gelir_Item_sakla_4.append(self.musteriler_islem)
                    self.yolla_to2 = M_Arsiv([1],self.musteriler_islem) 
                    for x in self.gelir_Item_sakla_4:
                        if not x in self.gelir_Item_sakla_3:
                            self.gelir_Item_sakla_3.append(x)
                            self.giris.delete(0,END)
                            self.liste_2.delete(0,END)
                            for S in self.gelir_Item_sakla_3:
                                self.liste_2.insert(END,S)
                    self.listeleri_tazele()

                else:
                    self.uyari = Uyari(2,self.param_2)


    def sil_onay(self):
        if self.cbk_1b.get() == True:
            self.sil()
        elif self.cbk_2b.get() == True:
            self.sil_2()


    def sil(self):
        'gelir türü sil'
        self.liste_sil = self.liste.get(ACTIVE)
        if bool(self.liste_sil) == False:
            self.etiket.configure(text='liste', fg='black')
        elif self.liste_kontrol == False:
             self.uyari = Uyari(6,self.param_2)


        else:
            for i in self.gelir_Item_sakla_1:
                if self.liste_sil in i:
                    self.gelir_Item_sakla_1.remove(self.liste_sil)
            for z in self.gelir_Item_sakla_2:
                if self.liste_sil in z:
                    self.gelir_Item_sakla_2.remove(self.liste_sil)
            self.etiket.configure(text='siliniyor...', fg='blue')
            self.etiket.update()
            time.sleep(0.8)
            self.etiket.configure(text='p1', fg='black')
            self.liste.delete(ACTIVE)
            self.liste_kontrol = False
            if isinstance(self.liste_sil,(str)):
                self.yolla_to = G_Arsiv([0],self.liste_sil)
                self.listeleri_tazele()


    def sil_2(self):
        'müşteri sil'
        self.liste_2_sil = self.liste_2.get(ACTIVE)
        if bool(self.liste_2_sil) == False:
            self.etiket.configure(text='liste', fg='black')
        elif self.liste_2_kontrol == False:
             self.uyari = Uyari(7,self.param_2)

        else:
            for y in self.gelir_Item_sakla_4:
                if self.liste_2_sil in y:
                    self.gelir_Item_sakla_4.remove(self.liste_2_sil)
            for Z in self.gelir_Item_sakla_3:
                if self.liste_2_sil in Z:
                    self.gelir_Item_sakla_3.remove(self.liste_2_sil)
            self.et3.set('siliniyor...')
            self.etiket_3.configure(fg='blue')
            self.etiket_3.update()
            time.sleep(0.8)
            self.et3.set('p2:')
            self.etiket_3.configure(fg='black')
            self.etiket_3.update()
            self.liste_2.delete(ACTIVE)
            self.liste_2_kontrol = False
            if isinstance(self.liste_2_sil,(str)):
                self.yolla_to2 = M_Arsiv([0],self.liste_2_sil) 
                self.listeleri_tazele()


    def gosterici(self, event):
        'listede seçilen her öge için bilgi mesajı verir.'
        if self.cbk_1b.get() == True:
            self.etiket['text'] = '%s' % self.liste.get(ACTIVE)
            self.etiket['fg'] = '#1c0f45'
            if len(self.liste.get(ACTIVE)) <= 13:
                self.etiket['font'] = 'Courier 12 bold'
            elif len(self.liste.get(ACTIVE)) >=13:
                self.etiket['font'] = 'Arial 9 bold'
            self.liste_get_active = self.liste.get(ACTIVE)
            self.liste_kontrol = True


    def gosterici_B (self, event):
        'Müşteriler listesi (p2)'
        if self.cbk_2b.get() == True:
            self.liste_2_get_active = self.liste_2.get(ACTIVE)
            if self.liste_2.get(ACTIVE):
                self.et3.set(self.liste_2_get_active)
                if len(self.liste_2.get(ACTIVE)) <= 13:
                    self.etiket_3.configure(fg='#1c0f45',font='Courier 12 bold')
                elif len(self.liste_2.get(ACTIVE)) >= 13:
                    self.etiket_3.configure(fg='#1c0f45', font='Arial 9 bold')
                self.etiket_3.update()
                self.liste_2_kontrol = True


    def veri_kontrol_fonksiyon(self):
        'Tüm girişlerin kontrolü'
        if self.gui_tarih_gosterInt.get() == 1:
            self.veri_tarih = 1
        elif self.gui_tarih_gosterInt.get() == 0:
            if bool(self.gui_tarih_ekle_1.get()) == False:
                self.uyari = Uyari(1,self.param_2)
            else:
                if bool(self.gui_tarih_ekle_1.get()) == True:
                    if self.gui_tarih_ekle_1.get() > self.sistem_saati_gun:
                        self.uyari = Uyari(5,self.param_2)
                    else:
                        self.veri_tarih = 1


##        if not 'Veri Yok!' in self.gui_gelir_ekle.get():
        try:
            if len(str(self.gui_gelir_ekle.get())) < 13:
                self.gui_gelir_ekle_total = float(self.gui_gelir_ekle.get())
                if isinstance(self.gui_gelir_ekle_total, (float)):
                        self.veri_gelir = 1
            else:
                self.uyari = Uyari(10,self.param_2)
                self.veri_gelir = 0
        except ValueError:
            self.uyari = Uyari(3,self.param_2)
            self.veri_gelir = 0


    def veri_islem(self):
        'gelirTablo.py >>'
        self.gui_liste = gtb(self.liste_get_active)
        if self.gui_tarih_gosterInt.get() == 1:
            self.gui_liste.tarih_gelir_ekle(self.bugun_vt)
        elif self.gui_tarih_gosterInt.get() == 0:
            if int(self.gui_tarih_ekle_1.get()) > 0:
                self.gui_liste.tarih_gelir_ekle(str(self.sistem_saati_yil) +
                                                '.'+str(self.sistem_saati_ay) +
                                                self.gui_tarih_ekle_1.get())

        self.gui_liste.musteri_ekle(self.liste_2_get_active)
        self.gui_liste.gelir_ekle(self.gui_gelir_ekle_total)

        self.gui_tarih_ekle_1.delete(0, END)
        self.gui_gelir_ekle.delete(0, END)

        self.veri_tarih = 0
        self.veri_gelir = 0


    def kontrol_mekanizma(self,event=None):
        'gui tamam butonu 1. durak'
        if self.liste_kontrol and self.liste_2_kontrol == True:
            self.veri_kontrol_fonksiyon()
            if all([self.veri_tarih, self.veri_gelir]) == True:
               return self.tamam()

        else:
            if all([self.cbk_1b.get(),self.liste_kontrol]) == True:
                if self.liste_2_kontrol == False:
                    self.uyari = Uyari(9,self.param_2)
            if all([self.cbk_2b.get(),self.liste_2_kontrol]) == True:
                if self.liste_kontrol == False:
                    self.uyari = Uyari(8,self.param_2)
            elif self.cbk_1b.get() == True:
                if self.liste_kontrol == False:
                    self.uyari = Uyari(8,self.param_2)
            elif self.cbk_2b.get() == True:
                if self.liste_2_kontrol == False:
                    self.uyari = Uyari(9,self.param_2)


    def tamam(self):
        'gui tamam 2.durak'
        self.veri_islem()
        self.liste_kontrol = False
        self.liste_2_kontrol = False
        if all([self.liste_kontrol, self.liste_2_kontrol]) == False:
            self.etiket.configure(text='işleniyor...', fg='blue', font='Courier 12 bold')
            self.etiket.update()
            time.sleep(1)
            self.gui_veriler = self.gui_liste.veriTabanına_yolla()
            self.etiket.configure(text='p1:', fg='black', font='Courier 12 bold')
            self.et3.set('p2:')
            self.etiket_3.configure(fg='black',font='Courier 12 bold')
            self.etiket_3.update()
            if self.cbk_2b.get() == True:
                self.cbk_2b.set(False)
                self.cbk_1b.set(True)
            if self.gui_tarih_gosterInt.get() == 0:
                self.gui_tarih_gosterInt.set(1)

    
    def listeleri_tazele(self):
        from veriTabani import VeriTabani_2 as dblite_2
        from veriTabani import VeriTabani_2B as dblite_2B

        self.et3.set('p2:')
        self.etiket_3.configure(fg='black')
        self.etiket_3.update()
        for i in self.gelir_Item_sakla_2:
            i = (i,)
            self.item_yolla.append(i)
        for y in self.gelir_Item_sakla_3:
            y = (y,)
            self.item_yolla2.append(y)
        self.musteriler_liste_vt2B = dblite_2B(self.item_yolla2)
        self.gelir_liste_vt_2 = dblite_2(self.item_yolla)

    def modul_kapa(self):
        from veriTabani import VeriTabani_7
        self.modul_kapanir = VeriTabani_7(2,'Gelir Ekle')


    def cikis(self,event=None):
        self.listeleri_tazele()
        self.modul_kapa()
        self.gelir_Item_sakla_1.clear()
        self.gelir_Item_sakla_2.clear()
        self.gelir_Item_sakla_3.clear()
        self.gelir_Item_sakla_4.clear()
        self.liste.delete(0, END)
        self.liste_2.delete(0,END)
       # self.hatirlatma_close()
        self.pencere2.destroy()



if __name__ == '__main__':
    uyg = Gelir_ekle()
    mainloop()





class Postaci():
    Ppostaci = []
    PTpostaci = []

    def __init__(self, listem,listem_2):
        self.listem = listem
        self.listem_2 = listem_2
        self.Ppostaci.extend(self.listem)
        self.PTpostaci.extend(self.listem_2)
        self.listem.clear()
        self.listem_2.clear()


    @classmethod
    def posta_al(self):
        self.Ppostaci.extend(self.listem)
