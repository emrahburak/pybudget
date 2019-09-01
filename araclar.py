
#-*-coding=utf-8-*-

from tkinter import *


class Hesap_mk(object):
    def __init__(self):

        self.depo = ''
        self.yeni()


    def konum(self,gen,yuks,penc):
        self.pgen = gen
        self.pyuks = yuks
        self.penc = penc
       
        

        self.ekrangen = self.penc.winfo_screenwidth()
        self.ekranyuks = self.penc.winfo_screenheight()

        self.x = (self.ekrangen - self.pgen) / 1.3
        self.y = (self.ekranyuks - self.pyuks) / 1.4

        self.penc.geometry('%dx%d+%d+%d' % (self.pgen, self.pyuks,
                                               self.x, self.y))
        
        

    def yeni(self):
        self.pencere2 = Tk()
        self.konum(325,350,self.pencere2)
        self.titlE = self.pencere2.title('CUT HESAP MAKİNASI')
        self.pencere2.tk_setPalette('#9fb6cd')
        self.pencere2.resizable(width=FALSE, height=FALSE)
        self.pencere2.bind('<Escape>',self.cikis)
        self.ekran = Entry(self.pencere2,width=35,bg='white',
                           font='arial 12 ')
        self.ekran.grid(row=0, column=0, columnspan=3, ipady=9)
        self.liste = [\
            "9", "8","7",
            "6", "5","4",
            "3", "2","1",
            "0", "+","-",
            "/", "*","=",
            "C",'çıkış']

        self.sira = 1
        self.sutun = 0
        for i in self.liste:
            self.komut = lambda x=i: self.hesapla(x)
            Button(self.pencere2,
                   text=i,
                   width=8,
                   height=2,
                   font='MonoSpace 12 bold',
##                   bg='#e0eeee',
                   relief=GROOVE,
                   command=self.komut).grid(row=self.sira,
                                            column=self.sutun)
            self.sutun += 1
            if self.sutun > 2:
                self.sutun = 0
                self.sira += 1

    def hesapla(self,tus):
        self.tus = tus
        if self.tus in '0123456789':
            self.ekran.insert(END,self.tus)
            self.depo = self.depo + self.tus

        if self.tus in '+-/*':
            self.depo = self.depo + self.tus
            self.ekran.delete(0,END)

        if self.tus == '=':
            self.ekran.delete(0, END)
        # Normalde tehlikeli bir fonksiyon olan eval() i
        #nasıl kullandığımıza dikkat edin..
            self.hesap = eval(self.depo,{'__builtins__':None},{})
            self.depo = str(self.hesap)
            self.ekran.insert(END, self.depo)

        if self.tus == 'C':
            self.ekran.delete(0, END)
            self.depo = ''

        if self.tus == 'çıkış':
            self.cikis()

    def modul_kapa(self):
        from veriTabani import VeriTabani_7
        self.modul_kapanir = VeriTabani_7(2,'Araçlar')


    def cikis(self,event=None):
        self.modul_kapa()
        return self.pencere2.destroy()

        
        
        


##uyg = Hesap_mk()
##mainloop()

# kod çalışır durumda
