from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from tkcalendar import DateEntry
import tkinter as tk
import datetime
from tkinter import ttk


class essenseClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Application de Gestion BTP | Developped by Franck")
        self.root.config(bg="white")
        self.root.focus_force()
#===================
#All Variables =================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_gas_id=StringVar()
        self.var_capacity_bgn=DoubleVar()
        self.var_capacity_add=DoubleVar()
        self.var_capacity_end=DoubleVar()
        self.var_capacity_rst=DoubleVar()
        self.var_capacity_csm=DoubleVar()
        self.var_cond_surname=StringVar()
        self.var_date=StringVar()
        self.var_hours=StringVar()
        self.var_machine_name=StringVar()
        self.var_mois=StringVar()






    #========searchFrame=========
    #     SearchFrame=LabelFrame(self.root,text="Recherche Conducteur", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
    #     SearchFrame.place(x=250, y=20, width=600,height=70)
    
    # #===options===
    #     cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=(" ","Email","Nom","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
    #     cmb_search.place(x=10,y=10, width=180)
    #     cmb_search.current(0)

    #     txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
    #     btn_search=Button(SearchFrame,text="Recherche",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

    #=====title======
        title=Label(self.root,text="Infos Essence",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP, fill=X)


    #=====content=====
    #=====ligne premier====
        essense_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        essense_frame.place(x=10, y=40, width=290, height=450)

    #======name selector =====  
        lbl_cond_name = Label(essense_frame, text="Conducteur", font=("goudy old style", 15), bg="white").place(x=0, y=5)
        self.cmb_cond_name = ttk.Combobox(essense_frame, textvariable=self.var_cond_surname, font=("goudy old style", 12), state='readonly')
        self.cmb_cond_name.place(x=130, y=5, width=150)
        # Populate the combobox with conducteur names from the database
        self.populate_conducteur_names()

    #======machine selector=========
        lbl_machine = Label(essense_frame, text="Machine", font=("goudy old style", 15), bg="white").place(x=0, y=40)
        self.cmb_machine = ttk.Combobox(essense_frame, textvariable=self.var_machine_name, font=("goudy old style", 10), state='readonly')
        self.cmb_machine.place(x=130, y=40, width=150)
        # Populate the combobox with conducteur names from the database
        self.populate_machine_names()

        lbl_mois = Label(essense_frame, text="Mois", font=("goudy old style", 15), bg="white").place(x=0, y=80)
        self.cmb_mois = ttk.Combobox(essense_frame, font=("goudy old style", 12), textvariable=self.var_mois, state='readonly')
        self.cmb_mois['values'] = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet','Aout','Septembre', 'Octobre', 'Novembre', 'Decembre']
        self.cmb_mois.place(x=130, y=80, width=150)  

        lbl_date = Label(essense_frame, text="Date", font=("goudy old style", 15), bg="white").place(x=0, y=120)
        date_entry = DateEntry(essense_frame, textvariable=self.var_date, date_pattern='dd/mm/yyyy', width=18, background='darkblue', foreground='white', borderwidth=2, locale='fr_FR')
        date_entry.place(x=130, y=120, width=150, height=30)

    #=======capacity=====
        lbl_capacity_bgn=Label(essense_frame,text="Essence initial",font=("goudy old style", 15), bg="white").place(x=0, y=160)
        txt_capacity_bgn=Entry(essense_frame, textvariable=self.var_capacity_bgn, font=("goudy old style",15), bg="lightyellow").place(x=130, y=160, width=150)

        lbl_capacity_add=Label(essense_frame,text="Essence ajouté",font=("goudy old style", 15), bg="white").place(x=0, y=200)
        txt_capacity_add=Entry(essense_frame, textvariable=self.var_capacity_add, font=("goudy old style",15), bg="lightyellow").place(x=130, y=200, width=150)

        # lbl_capacity_rst=Label(essense_frame,text="Essence restant",font=("goudy old style", 15), bg="white").place(x=0, y=240)
        # txt_capacity_rst=Entry(essense_frame, textvariable=self.var_capacity_rst, font=("goudy old style",15), bg="lightyellow").place(x=130, y=240, width=150)


        # lbl_id=Label(essense_frame,text="ID ",font=("goudy old style", 15), bg="white").place(x=0, y=280)
        # txt_id=Entry(essense_frame, textvariable=self.var_gas_id, font=("goudy old style",15), bg="lightyellow")
        # txt_id.place(x=70, y=280, width=50)
        # txt_id.insert(0, "1")


    #========buttons===========
        btn_save=Button(essense_frame,text="Sauvegarder",command=self.add,font=("goudy old style",12),bg="#2196f3",fg="white",cursor="hand2").place(x=70,y=310,width=100,height=30)
        btn_clear=Button(essense_frame,text="Effacer",command=self.clear,font=("goudy old style",12),bg="#607d8b",fg="white",cursor="hand2").place(x=190,y=310,width=90,height=30)
        btn_update=Button(essense_frame,text="Maj",command=self.update,font=("goudy old style",12),bg="#4caf50",fg="white",cursor="hand2").place(x=70,y=345,width=100,height=30)
        btn_suppr=Button(essense_frame,text="Supprimer",command=self.delete,font=("goudy old style",12),bg="#f44336",fg="white",cursor="hand2").place(x=190,y=345,width=90,height=30)

    #=======Search frame=======           
        SearchFrame = LabelFrame(self.root,text="Recherche",bd=2, relief=RIDGE, bg="lightblue")
        SearchFrame.place(x=870, y=35, width=220, height=160)

        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Mois","Date","machine_name","nom"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10, width=200)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=10,y=60)
        btn_search=Button(SearchFrame,text="Recherche",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=10,y=100,width=150,height=30)


    #========Essence Details Frame
        details_frame = Frame(self.root, bd=2, relief=RIDGE)
        details_frame.place(x=310, y=40, width=550, height=270) 

        scrolly=Scrollbar(details_frame, orient=VERTICAL)
        scrollx=Scrollbar(details_frame, orient=HORIZONTAL)

        #self.GasTable=ttk.Treeview(details_frame, columns=("id","mois","date", "nom","machine_name","capacityd","capacitya","capacityr"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.GasTable=ttk.Treeview(details_frame, columns=("mois","date", "nom","machine_name","capacityd","capacitya","capacityr"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.GasTable.xview)
        scrolly.config(command=self.GasTable.yview)


        #self.GasTable.heading("id",text="ID")
        self.GasTable.heading("mois",text="Mois")
        self.GasTable.heading("date",text="Date")
        self.GasTable.heading("nom",text="Conducteur")
        self.GasTable.heading("machine_name",text="Machine")
        self.GasTable.heading("capacityd",text="Essence Début")
        self.GasTable.heading("capacitya",text="Essence Ajouté")
        self.GasTable.heading("capacityr",text="Essence Restant")
        self.GasTable["show"]="headings"

        #self.GasTable.column("id",width=30)   
        self.GasTable.column("mois",width=70)     
        self.GasTable.column("date",width=70)
        self.GasTable.column("nom",width=100)
        self.GasTable.column("machine_name",width=100)
        self.GasTable.column("capacityd",width=90)
        self.GasTable.column("capacitya",width=90)
        self.GasTable.column("capacityr",width=90)
        self.GasTable.pack(fill=BOTH, expand=1)
        self.GasTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        consumption_frame = Frame(self.root, bd=2, relief=RIDGE)
        consumption_frame.place(x=310, y=320, width=250, height=170)
        scrolly_consumption = Scrollbar(consumption_frame, orient=VERTICAL)
        scrollx_consumption = Scrollbar(consumption_frame, orient=HORIZONTAL)
        self.ConsumptionTable = ttk.Treeview(consumption_frame, columns=( "date", "consumption"), yscrollcommand=scrolly_consumption.set, xscrollcommand=scrollx_consumption.set)

        self.ConsumptionTable.heading("date", text="Date")
        self.ConsumptionTable.heading("consumption", text="Essence ajouté")
        self.ConsumptionTable["show"] = "headings"

        self.ConsumptionTable.column("date", width=70)
        self.ConsumptionTable.column("consumption", width=150)
        self.show2()
        scrollx_consumption.pack(side=BOTTOM, fill=X)
        scrolly_consumption.pack(side=RIGHT, fill=Y)
        scrollx_consumption.config(command=self.ConsumptionTable.xview)
        scrolly_consumption.config(command=self.ConsumptionTable.yview)

        self.ConsumptionTable.pack(fill=BOTH, expand=1)


        machine_frame = Frame(self.root, bd=2, relief=RIDGE)
        machine_frame.place(x=580, y=320, width=250, height=170)
        scrolly_consumption = Scrollbar(machine_frame, orient=VERTICAL)
        scrollx_consumption = Scrollbar(machine_frame, orient=HORIZONTAL)
        self.MachTable = ttk.Treeview(machine_frame, columns=( "machine_name", "consumption"), yscrollcommand=scrolly_consumption.set, xscrollcommand=scrollx_consumption.set)

        self.MachTable.heading("machine_name", text="Machine")
        self.MachTable.heading("consumption", text="Essence ajouté")
        self.MachTable["show"] = "headings"

        self.MachTable.column("machine_name", width=100)
        self.MachTable.column("consumption", width=150)
        self.show3()
        scrollx_consumption.pack(side=BOTTOM, fill=X)
        scrolly_consumption.pack(side=RIGHT, fill=Y)
        scrollx_consumption.config(command=self.MachTable.xview)
        scrolly_consumption.config(command=self.MachTable.yview)

        self.MachTable.pack(fill=BOTH, expand=1)

        mois_frame = Frame(self.root, bd=2, relief=RIDGE)
        mois_frame.place(x=850, y=320, width=200, height=170)
        scrolly_consumption = Scrollbar(mois_frame, orient=VERTICAL)
        scrollx_consumption = Scrollbar(mois_frame, orient=HORIZONTAL)
        self.MoisTable = ttk.Treeview(mois_frame, columns=( "mois", "consumption"), yscrollcommand=scrolly_consumption.set, xscrollcommand=scrollx_consumption.set)

        self.MoisTable.heading("mois", text="Mois")
        self.MoisTable.heading("consumption", text="Essence ajouté")
        self.MoisTable["show"] = "headings"

        self.MoisTable.column("mois", width=50)
        self.MoisTable.column("consumption", width=100)
        self.show4()
        scrollx_consumption.pack(side=BOTTOM, fill=X)
        scrolly_consumption.pack(side=RIGHT, fill=Y)
        scrollx_consumption.config(command=self.MoisTable.xview)
        scrolly_consumption.config(command=self.MoisTable.yview)

        self.MoisTable.pack(fill=BOTH, expand=1)



    def populate_consumption_table(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT  date, SUM(capacitya) as consumption FROM essense GROUP BY date")
            rows = cur.fetchall()
            self.ConsumptionTable.delete(*self.ConsumptionTable.get_children())
            for row in rows:
                self.ConsumptionTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
        finally:
            con.close()

    def populate_mach_table(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT  machine_name, SUM(capacitya) as consumption FROM essense GROUP BY machine_name")
            rows = cur.fetchall()
            self.MachTable.delete(*self.MachTable.get_children())
            for row in rows:
                self.MachTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
        finally:
            con.close()

    def populate_mois_table(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT  mois, SUM(capacitya) as consumption FROM essense GROUP BY mois")
            rows = cur.fetchall()
            self.MoisTable.delete(*self.MoisTable.get_children())
            for row in rows:
                self.MoisTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}")
        finally:
            con.close()


        #============================================================================
    def add(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT capacityr FROM essense ORDER BY id DESC LIMIT 1")
            last_capacity_rst = cur.fetchone()

            if last_capacity_rst is None:
                self.var_capacity_rst = float(self.var_capacity_bgn.get()) - float(self.var_capacity_add.get())
            else:
                self.var_capacity_rst = float(last_capacity_rst[0]) + float(self.var_capacity_bgn.get()) - float(self.var_capacity_add.get())
            cur.execute("Insert into essense (mois,date,nom,machine_name,capacityd,capacitya,capacityr) values(?,?,?,?,?,?,?)",(
                                        #self.var_gas_id.get(),
                                        self.var_mois.get(),
                                        self.var_date.get(),
                                        self.var_cond_surname.get(),
                                        self.var_machine_name.get(),
                                        self.var_capacity_bgn.get(),
                                        self.var_capacity_add.get(),
                                        self.var_capacity_rst,
                    ))
            con.commit()
            messagebox.showinfo("Success", "Info  Ajouté avec success", parent=self.root)
            self.var_gas_id.set(cur.lastrowid)
            self.show()
            self.populate_consumption_table()
            self.populate_mach_table()
            self.populate_mois_table()
            self.clear1()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT mois,date,nom,machine_name,capacityd,capacitya,capacityr FROM essense ORDER BY id")
            rows=cur.fetchall()
            self.GasTable.delete(*self.GasTable.get_children())
            for row in rows:
                self.GasTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def show2(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT date, SUM(capacitya) as consumption FROM essense GROUP BY date ORDER BY date ASC")
            rows = cur.fetchall()
            self.ConsumptionTable.delete(*self.ConsumptionTable.get_children())
            for row in rows:
                self.ConsumptionTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}")

    def show3(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT machine_name, SUM(capacitya) as consumption FROM essense GROUP BY machine_name")
            rows = cur.fetchall()
            self.MachTable.delete(*self.MachTable.get_children())
            for row in rows:
                self.MachTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}")

    def show4(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT mois, SUM(capacitya) as consumption FROM essense GROUP BY mois")
            rows = cur.fetchall()
            self.MoisTable.delete(*self.MoisTable.get_children())
            for row in rows:
                self.MoisTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}")

    def get_data(self,ev):
        f=self.GasTable.focus()
        content=(self.GasTable.item(f))
        row=content['values']
        #print(row)
        #self.var_gas_id.set(row[])
        self.var_mois.set(row[0])
        self.var_date.set(row[1])
        self.var_cond_surname.set(row[2])
        self.var_machine_name.set(row[3])
        self.var_capacity_bgn.set(row[4])
        self.var_capacity_add.set(row[5])
        self.var_capacity_rst.set(row[6])
        #self.var_capacity_csm.set(row[7])


    def get_data2(self,ev):
        g=self.capacity_table.focus()
        content=(self.capacity_table.item(g))
        row=content['values']
        #print(row)
        self.var_date.set(row[0])
        self.var_machine_name.set(row[2])
        self.var_capacity_add.set(row[3])

    def clear(self):
        self.var_gas_id.set("")
        self.var_mois.set("")
        self.var_date.set("")
        self.var_cond_surname.set("")
        self.var_machine_name.set("")
        self.var_capacity_bgn.set("0.0")
        self.var_capacity_add.set("0.0")
        self.var_capacity_rst.set("")
        self.show()
    
    def clear1(self):
        self.var_capacity_bgn.set("0.0")
        self.var_capacity_add.set("0.0")
 



    def search(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get() == " ":
                messagebox.showerror("Error", "Choisisser l'un des option disponibles", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Entrez une valeur", parent=self.root)
            else:
                # Validate the column name against a whitelist
                valid_columns = ['Mois','Date', 'machine_name', 'nom']  # Example whitelist
                if self.var_searchby.get() in valid_columns:
                    # Using parameterized queries for the value part
                    query = f"SELECT * FROM essense WHERE {self.var_searchby.get()} LIKE ?"
                    cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.GasTable.delete(*self.GasTable.get_children())
                        for row in rows:
                            self.GasTable.insert('', END, values=row)
                    else:
                        messagebox.showerror("Error", "Pas de record!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "Invalid search column", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)


    def update(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            # cur.execute("Select * from gasoil where id=?",(self.var_gas_id.get(),))
            # row=cur.fetchone()
            # if row == None:
            #         messagebox.showerror("Error","Invalid date",parent=self.root)
            # else:
            #     self.var_capacity_csm = float(self.var_capacity_bgn.get()) + float(self.var_capacity_add.get()) - float(self.var_capacity_rst.get())
                cur.execute("Update  essense set  mois=?, date=?, nom=?, machine_name=?, capacityd=?, capacitya=?, capacityr=?  where nom=? and capacityr=? ",(
                                            self.var_mois.get(),
                                            self.var_date.get(),
                                            self.var_cond_surname.get(),
                                            self.var_machine_name.get(),
                                            self.var_capacity_bgn.get(),
                                            self.var_capacity_add.get(),
                                            self.var_capacity_rst.get(),
                                            self.var_cond_surname.get(),
                                            self.var_capacity_rst.get(),
                                            #self.var_gas_id.get(),
                        ))
                con.commit()
                messagebox.showinfo("Success", "Info mise a jour avec success", parent=self.root)
                self.var_gas_id.set(cur.lastrowid)
                self.show()
                self.populate_consumption_table()
                self.populate_mach_table()
                self.populate_mois_table()
                con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    # Add this method to your essenseClass
    def populate_conducteur_names(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT nom, prénom FROM conducteur")
            rows = cur.fetchall()
            conducteur_names = [f"{row[0]} {row[1]}" for row in rows]
            self.cmb_cond_name['values'] = conducteur_names
            if conducteur_names:  # Set the first name as the default value if the list is not empty
                self.cmb_cond_name.current(0)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)
        finally:
            con.close()

    # Add this method to your essenseClass
    def populate_machine_names(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT machine_name FROM machine")
            rows = cur.fetchall()
            machine_names = [row[0] for row in rows]
            self.cmb_machine['values'] = machine_names
            if machine_names:  # Set the first name as the default value if the list is not empty
                self.cmb_machine.current(0)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            # if self.var_gas_id.get()=="":
            #     messagebox.showerror("Error","Le ID  est requis", parent=self.root)
            # else:
            #     cur.execute("Select * from gasoil where id=?",(self.var_gas_id.get(),))
            #     row=cur.fetchone()
            #     if row == None:
            #         messagebox.showerror("Error","Invalid  ID",parent=self.root)
            #     else:
                    op=messagebox.askyesno("confirm","Etes vous sure de vouloir supprimer ?",parent=self.root)
                    if op ==True:
                        cur.execute("delete from essense where nom=? and capacityr=?  ",(self.var_cond_surname.get(),self.var_capacity_rst.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Info supprimer avec succes",parent=self.root)
                        self.clear()
                        self.populate_consumption_table()
                        self.populate_mach_table()
                        self.populate_mois_table()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=essenseClass(root)
    root.mainloop()