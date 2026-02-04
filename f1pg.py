from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as c
import tkinter.messagebox as tmsg
from tkinter import Toplevel
from s2pg import por
from nf2pg1 import nf2pg
from sql_th import sqlcon
n='0321'

try:
    class sch(Tk):
        def __init__(self):
            super().__init__()
            self.geometry('1200x800')
            self.minsize(1000, 800)
            self.maxsize(1250, 20000)
            self.bg = Image.open('4.jpg')
            self.im = ImageTk.PhotoImage(self.bg)
            Label(self, image=self.im, bg='gray9').place(relwidth=1, relheight=1)

            rosegold = "#b76e79"
            Label(self,text="Are You A New User", fg='grey92',
                  bg='gray9', font=('Bodoni_MT 20 bold')).pack(pady=130, fill=X)

            Button(self, text='YES', font=("Arial", 16, "bold"),  # Font styling
                   bg="grey9",  # Background color
                   fg=rosegold,  # Text color (rosegold)
                   activebackground="#1c1c1c",  # Background color when clicked (darker black)
                   activeforeground=rosegold,  # Text color when clicked
                   highlightbackground=rosegold,  # Border color (rosegold)
                   highlightthickness=2,  # Thickness of the border
                   width=4,
                   height=1, command=por).pack(side=LEFT, padx=270, pady=20)

            def pg():

                root = Toplevel()
                root.title('ENTRY')
                root.geometry('1200x800')
                root.minsize(1000, 800)
                root.maxsize(1250, 2000)

                self.bg = Image.open('2.jpg')
                self.k = ImageTk.PhotoImage(self.bg)
                Label(root, image=self.k).place(relwidth=1, relheight=1)
                Label(root,text='Welcome To Tax Collecting System', font=('algerian 33 bold'), fg='gray20', bg='gray43').pack(
                    pady=2,fill=X)

                f1 = Frame(root, bg='gray39', relief=SUNKEN, borderwidth=5,
                           padx=5, pady=5)
                f1.pack(side=TOP, padx=200, pady=130, anchor='nw')

                Label(f1, text="USERNAME:", bg='gray52', font=('Baskerville_Old_Face 10 bold')).pack(side='left', padx=9)

                f2 = Frame(root, bg='gray39', relief=SUNKEN, borderwidth=5, padx=5, pady=5)
                f2.pack(side="left", anchor='nw', padx=200)
                Label(f2, text="PASSWORD:", bg='gray52', font=('Baskerville_Old_Face 10 bold')).pack(side='left', padx=9)

                # for input value from user
                uv = StringVar()
                pv = StringVar()

                ue = Entry(f1, textvariable=uv, borderwidth=2, name='userid')
                pe = Entry(f2, textvariable=pv, borderwidth=2, name='passwd')

                ue.pack(padx=9)
                pe.pack(padx=7)

                def submit():
                    try:
                        print('username=', ue.get(), '\npassword=', pe.get())
                        # giving info s to database
                        i = c.connect(host='localhost', username='root', passwd=n, database='info')
                        if i.is_connected():
                            print('successful')
                            cur = i.cursor()
                            h = "SELECT * FROM account"
                            cur.execute(h)
                            data = cur.fetchall()

                            registered = False  # Flag to check if user is registered

                            for record in data:
                                if record[0] == pe.get() or record[1] == ue.get():
                                    registered = True  # Set the flag to True if a match is found
                                    for j in record:
                                        print(j)
                                    nf2pg(pe.get())  # Call your function if registered

                            if not registered:  # Check the flag after the loop
                                a = tmsg.showinfo("Warning", "You are not registered\n Please register yourself")

                            i.commit()  # Commit the transaction if needed
                    except:
                        print()

                b = Button(root, text='Enter', borderwidth=4, relief=SUNKEN, bg='LightCyan2', font='arial_black 15 bold',
                           command=submit,width=8)
                b.pack(side='top', pady=100, anchor='sw')
                # for giiving name to the gui



                root.mainloop()

            Button(self, text='NO', font=("Arial", 16, "bold"),  # Font styling
                   bg="grey9",  # Background color
                   fg=rosegold,  # Text color (rosegold)
                   activebackground="#1c1c1c",  # Background color when clicked (darker black)
                   activeforeground=rosegold,  # Text color when clicked
                   highlightbackground=rosegold,  # Border color (rosegold)
                   highlightthickness=2,  # Thickness of the border
                   width=10, padx=1,
                   height=1, command=pg).pack(side='right', padx=270, pady=20)

            self.title('WEBSITE')





    if __name__ == '__main__':
        q=sch()
        #q.sqlcon()
        q.mainloop()
        sqlcon()
except:
    print()