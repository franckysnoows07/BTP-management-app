from tkinter import *
from PIL import Image,ImageTk
from conducteur import conducteurClass
from gasoils import gasoilsClass
from machine import MachineClass
from heure_work import workingHoursClass
from perdieme import perdiemeClass
from depense import depenseClass
import time
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class BTP:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Application de Gestion BTP | Developped by Franck")
        self.root.config(bg="white")
    #=====titre======
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Application de Gestion BTP",image=self.icon_title,compound=LEFT,font=("times new roman",30,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

    #=====btn-deconnecter ===
    #===clock=====
        self.lbl_clock=Label(self.root,text="Bienvenue dans votre espace de gestion BTP\t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
    #===Left-Menu====
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo= self.MenuLogo.resize((200,180), Image.Resampling.LANCZOS)
        self.MenuLogo= ImageTk.PhotoImage(self.MenuLogo)
    
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=104,width=225,height=580)

        lbl_menulogo=Label(LeftMenu, image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)
    
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu, text="Menu", font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        btn_machine=Button(LeftMenu, text="Machine",command=self.machine,image=self.icon_side,compound=LEFT,padx=15,anchor="w", font=("times new roman",18, "bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_conducteur=Button(LeftMenu, text="Conducteurs",command=self.conducteur,image=self.icon_side,compound=LEFT,padx=15,anchor="w", font=("times new roman",18, "bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_gasoil=Button(LeftMenu, text="Gasoil",command=self.gasoil,image=self.icon_side,compound=LEFT,padx=15,anchor="w", font=("times new roman",18, "bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_depenses=Button(LeftMenu, text="Depenses",command=self.depense,image=self.icon_side,compound=LEFT,padx=15,anchor="w", font=("times new roman",18, "bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_working_hours=Button(LeftMenu, text="Heure de\n travail",command=self.travail,image=self.icon_side,compound=LEFT,padx=15,anchor="w", font=("times new roman",18, "bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_perdieme=Button(LeftMenu, text="Perdieme",command=self.perdieme,image=self.icon_side,compound=LEFT,padx=15,anchor="w", font=("times new roman",18, "bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)


    #====content==
        self.lbl_conducteur=Label(self.root,text="Total Conducteur\n[ 0 ]",bd=5, relief=RIDGE, bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_conducteur.place(x=300,y=120, width=300, height=150)
        self.update_conducteur_count()

        self.lbl_machine=Label(self.root,text="Total Machine Prop\n[ 0 ]",bd=5, relief=RIDGE, bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_machine.place(x=650,y=120, width=300, height=150)
        self.update_machine_pp_count()

        self.lbl_machine1=Label(self.root,text="Total Machine Loué\n[ 0 ]",bd=5, relief=RIDGE, bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_machine1.place(x=1000,y=120, width=300, height=150)
        self.update_machine_ll_count()

        self.lbl_gasoil=Label(self.root,text="Total Gasoil Consommée\n[ 0 ]",bd=5, relief=RIDGE, bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_gasoil.place(x=300,y=300, width=300, height=150)
        self.update_gasoil_cp()

        self.lbl_depense=Label(self.root,text="Total Dépense\n[ 0 ]",bd=5, relief=RIDGE, bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_depense.place(x=650,y=300, width=300, height=150)
        self.update_depense()

        self.lbl_perdieme=Label(self.root,text="Total Perdieme\n[ 0 ]",bd=5, relief=RIDGE, bg="#5e4280",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_perdieme.place(x=1000,y=300, width=300, height=150)
        self.update_perdieme()


    #===footer=====
        lbl_footer=Label(self.root,text="\nAG.BTP - Application de gestion BTP | Developped by Franck\n",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_time()
#==============================================================
    def update_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Bienvenue dans votre espace de gestion BTP\t\t Date: {str(date_)}  \t\t Time: {str(time_)}",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.after(200,self.update_time)

    def conducteur(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=conducteurClass(self.new_win)
    def gasoil(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=gasoilsClass(self.new_win)
    def machine(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=MachineClass(self.new_win)
    def travail(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=workingHoursClass(self.new_win)

    def depense(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=depenseClass(self.new_win)

    def perdieme(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=perdiemeClass(self.new_win)

    def update_conducteur_count(self):
            con = sqlite3.connect(database=r'btp.db')  # Replace 'btp.db' with your database name
            cur = con.cursor()
            try:
                cur.execute("SELECT COUNT(*) FROM conducteur")
                total_conducteurs = cur.fetchone()[0]
                self.lbl_conducteur.config(text=f"Total Conducteur\n[ {total_conducteurs} ]")
            except Exception as ex:
                messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
            finally:
                con.close()

    def update_machine_pp_count(self):
            con = sqlite3.connect(database=r'btp.db')  # Replace 'btp.db' with your database name
            cur = con.cursor()
            try:
                cur.execute("SELECT COUNT(*) FROM machine WHERE owner = 'Proprétaire'")
                total_propr = cur.fetchone()[0]
                self.lbl_machine.config(text=f"Total Machine Prop\n[ {total_propr} ]")
            except Exception as ex:
                messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
            finally:
                con.close()

    def update_machine_ll_count(self):
            con = sqlite3.connect(database=r'btp.db')  # Replace 'btp.db' with your database name
            cur = con.cursor()
            try:
                cur.execute("SELECT COUNT(*) FROM machine WHERE owner = 'Loué'")
                total_ll = cur.fetchone()[0]
                self.lbl_machine1.config(text=f"Total Machine loué\n[ {total_ll} ]")
            except Exception as ex:
                messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
            finally:
                con.close()
    def update_gasoil_cp(self):
            con = sqlite3.connect(database=r'btp.db')  # Replace 'btp.db' with your database name
            cur = con.cursor()
            try:
                cur.execute("SELECT SUM(capacitya) FROM gasoil ")
                total_ll = cur.fetchone()[0]
                self.lbl_gasoil.config(text=f"Total Gasoil\n Consommé\n[ {total_ll} L]")
            except Exception as ex:
                messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
            finally:
                con.close()

    def update_depense(self):
            con = sqlite3.connect(database=r'btp.db')  # Replace 'btp.db' with your database name
            cur = con.cursor()
            try:
                cur.execute("SELECT SUM(montant) FROM depense ")
                total_ll = cur.fetchone()[0]
                self.lbl_depense.config(text=f"Total Depense\n[ {total_ll} CFA]")
            except Exception as ex:
                messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
            finally:
                con.close()

    def update_perdieme(self):
            con = sqlite3.connect(database=r'btp.db')  # Replace 'btp.db' with your database name
            cur = con.cursor()
            try:
                cur.execute("SELECT SUM(montant) FROM perdieme ")
                total_ll = cur.fetchone()[0]
                self.lbl_perdieme.config(text=f"Total Perdieme\n[ {total_ll} CFA]")
            except Exception as ex:
                messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
            finally:
                con.close()

if __name__=="__main__":
    root=Tk()
    obj=BTP(root)
    root.mainloop()