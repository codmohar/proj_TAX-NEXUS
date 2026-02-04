from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
import tkinter.messagebox as tmsg
#from s2pg import *


def pg():
    root=Tk()
    root.title('First Page')
    root.geometry('1200x800')
    root.minsize(1000,800)
    root.maxsize(1250,2000)


    Label(text='Welcome To Tax Collecting System',font=('algerian 33 bold'),fg='gray20',bg='gray43').pack(pady=2)


    f1=Frame(root,bg='gray39',relief=SUNKEN,borderwidth=5,
             padx=5,pady=5)
    f1.pack(side=TOP,padx=200,pady=90,anchor='nw')

    Label(f1,text="USERNAME:",bg='gray52',font=('Baskerville_Old_Face 10 bold')).pack(side='left',padx=9)

    f2=Frame(root,bg='gray39',relief=SUNKEN,borderwidth=5,padx=5,pady=5)
    f2.pack(side="left",anchor='nw',padx=200)
    Label(f2,text="PASSWORD:",bg='gray52',font=('Baskerville_Old_Face 10 bold')).pack(side='left',padx=9)


    # for input value from user
    uv=StringVar()
    pv=StringVar()

    ue=Entry(f1,textvariable=uv,borderwidth=2,name='userid')
    pe=Entry(f2,textvariable=pv,borderwidth=2,name='passwd')

    ue.pack(padx=9)
    pe.pack(padx=7)

    def gg():

        root=Tk()
        root.title(f"{ue.get()}'s Status".capitalize())
        root.geometry('500x500')
        main = Menu(root)
        m1 = Menu(main)
        def h():
            print('happy')
            a=tmsg.showinfo('HELP',
                            "government is not for helping people")

        m1.add_command(label='proj', command=h)
        m1.add_separator()
        m1.add_command(label='save', command=h)
        m1.add_command(label='help', command=h)
        main.add_cascade(label='file', menu=m1)

        root.config(menu=main)

        root.mainloop()

    def submit():
        try:
            print('username=',ue.get(),'\npassword=',pe.get())
            # giving info s to database
            i = c.connect(host='localhost', username='root', passwd='mohar466',database='info')
            if i.is_connected():
                print('succesful')
                cur = i.cursor()
                h ="insert into information values('{}','{}')".format(str(ue.get()), str(pe.get()))
                print(h)
                cur.execute(h)
                i.commit()
            gg()
        except:
            print('Try other password!')
            a = tmsg.showinfo('WARNING!',
                              "Try Another password")

    b=Button(root,text='Enter',borderwidth=4,relief=SUNKEN,bg='LightCyan2',font='arial_black 10 bold',command=submit)
    b.pack(side='top',pady=100,anchor='sw')
    #for giiving name to the gui

    cg= Image.open('2.jpg')
    jj = ImageTk.PhotoImage(cg)
    Label(root, image= jj,bg='gray9').place(relwidth=1, relheight=1)

    root.mainloop()




def spg(self,master):

    self.geometry('1200x800')
    self.minsize(1000,800)
    self.maxsize(1250,20000)
    self.bg=Image.open('4.jpg')
    self.im=ImageTk.PhotoImage(self.bg)
    tk.Label(master,image=self.im,bg='gray9').place(relwidth=1,relheight=1)

    rosegold = "#b76e79"
    tk.Label(text="Are You A New User",fg='grey92',
          bg='gray9',font=('Bodoni_MT 20 bold')).pack(pady=130,fill=X)


    tk.Button(master,text='YES',font=("Arial", 16, "bold"),  # Font styling
        bg="grey9",  # Background color
        fg=rosegold,  # Text color (rosegold)
        activebackground="#1c1c1c",  # Background color when clicked (darker black)
        activeforeground=rosegold,  # Text color when clicked
        highlightbackground=rosegold,  # Border color (rosegold)
        highlightthickness=2,  # Thickness of the border
        width=4,
        height=1,command=por).pack(side=LEFT,padx=270,pady=20)

    tk.Button(master,text='NO',font=("Arial", 16, "bold"),  # Font styling
        bg="grey9",  # Background color
        fg=rosegold,  # Text color (rosegold)
        activebackground="#1c1c1c",  # Background color when clicked (darker black)
        activeforeground=rosegold,  # Text color when clicked
        highlightbackground=rosegold,  # Border color (rosegold)
        highlightthickness=2,  # Thickness of the border
        width=10,padx=1,
        height=1,command=pg).pack(side='right',padx=270,pady=20)




    self.title('WEBSITE')

    self.mainloop()