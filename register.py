from tkinter import *
from PIL import Image,ImageTk
class main(Tk):
    def Images(self):
        self.app_image = ImageTk.PhotoImage(Image.open('src/Register.png'))
        self.close_image = ImageTk.PhotoImage(Image.open('src/Close.png'))
        self.move_image = ImageTk.PhotoImage(Image.open('src/Move.png'))
        self.mini_image = ImageTk.PhotoImage(Image.open('src/Mini.png'))
    def Window_settings(self):
        self.app_body = Label(self,image=self.app_image,bg='#262626')
        self.config(background='#323232')
        self.geometry('500x500+300+100')
        self.app_body.pack()
    def Moveing(self,e):
        self.geometry(f'+{e.x_root-385}+{e.y_root-45}')
    def Key_Release_Uname(self,text):
        if len(text) > 0:
            self.uname_text.configure(text='')
            self.uname_text.place_configure(x=5000)
        else:
            self.uname_text.configure(text='Name')
            self.uname_text.place_configure(x=314)
    def Key_Release_Password(self,text):
        if len(text) > 0:
            self.password_text.configure(text='')
            self.password_text.place_configure(x=5000)
        else:
            self.password_text.configure(text='Password')
            self.password_text.place_configure(x=314)
    def Key_Release_Emil(self,text):
        if len(text) > 0:
            self.emil_text.configure(text='')
            self.emil_text.place_configure(x=5000)
        else:
            self.emil_text.configure(text='Emil')
            self.emil_text.place_configure(x=314)
    def entrys(self):
        self.uname_entry = Entry(self,bg='#262626',font=('tajwal',12),justify='center',border=0,bd=0)
        self.password_entry = Entry(self,bg='#262626',font=('tajwal',12),justify='center',border=0,bd=0)
        self.emil_entry = Entry(self,bg='#262626',font=('tajwal',12),justify='center',border=0,bd=0)
        self.uname_entry.place(x=314,y=234,width=144,height=25)
        self.uname_entry.bind("<KeyRelease>",lambda e: self.Key_Release_Uname(self.uname_entry.get()))
        self.password_entry.place(x=314,y=288,width=144,height=25)
        self.emil_entry.place(x=314,y=360,width=144,height=25)
        self.password_entry.bind("<KeyRelease>",lambda e: self.Key_Release_Password(self.password_entry.get()))
        self.emil_entry.bind("<KeyRelease>",lambda e: self.Key_Release_Emil(self.emil_entry.get()))
    def uname_(self):
        self.uname_text.place_configure(x=5000)
        self.uname_entry.focus()
        '''if self.password_entry.get() == '':
            self.password_text.configure(text='Password')
            self.password_text.place_configure(x=314)
        if self.emil_entry.get() == '':
            self.emil_text.configure(text='Emil')
            self.emil_text.place_configure(x=314)'''

    def password_ (self):
        self.password_text.place_configure(x=5000)
        self.password_entry.focus()
        if self.uname_entry.get() == '':
            self.uname_text.configure(text='Name')
            self.uname_text.place_configure(x=314,y=234)
        if self.emil_entry.get() == '':
            self.emil_text.configure(text='Emil')
            self.emil_text.place_configure(x=314,y=360)
    def emil_(self):
        self.emil_text.place_configure(x=5000)
        self.emil_entry.focus()
        if self.uname_entry.get() == '':
            self.uname_text.configure(text='Name')
            self.uname_text.place_configure(x=314,y=234)
        if self.password_entry.get() == '':
            self.password_text.configure(text='Password')
            self.password_text.place_configure(x=314,y=288)
    def texts(self):
        self.uname_text = Label(self,text='Name',bg='#262626',font=('tajwal',12),justify='center',border=0,bd=0)
        self.password_text = Label(self,text='Emil',bg='#262626',font=('tajwal',12),justify='center',border=0,bd=0)
        self.emil_text = Label(self,text='Password',bg='#262626',font=('tajwal',12),justify='center',border=0,bd=0)
        self.uname_text.place(x=314,y=234,width=144,height=25)
        self.password_text.place(x=314,y=288,width=144,height=25)
        self.emil_text.place(x=314,y=360,width=144,height=25)
        self.uname_text.bind('<Button-1>',lambda e : self.uname_())
        self.emil_text.bind('<Button-1>',lambda e :self.emil_())
        self.password_text.bind('<Button-1>',lambda e :self.password_())

    def buttons(self):
        Button(self,image=self.close_image,border=0,bd=0,bg='#323232',activebackground='#323232',command=lambda : self.destroy()).place(x=451,y=5)
        Button(self,image=self.mini_image,border=0,bd=0,bg='#323232',activebackground='#323232',command=lambda : self.iconify()).place(x=408,y=5)
        self.move = Label(self,image=self.move_image,border=0,bd=0,bg='#323232')
        self.move.place(x=368,y=5)
        self.move.bind('<B1-Motion>',self.Moveing)
        
    def __init__(self):
        super().__init__()
        #self.overrideredirect(1)
        #self.wm_attributes('-transparentcolor','black')
        self.Images()
        self.Window_settings()
        self.buttons()
        self.entrys()
        self.texts()
main().mainloop()