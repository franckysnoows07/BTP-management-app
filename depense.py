# achat des pieces
# maintenance
# perdieme
# diver
# gasoil

from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import sqlite3

class depenseClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Application de Gestion BTP | Developped by Franck")
        self.root.config(bg="white")
        self.root.focus_force()

    #====variable=======

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_date=StringVar()
        self.var_cat1=StringVar()
        self.var_cat2=StringVar()
        self.var_type=StringVar()
        self.var_montant=StringVar()
        self.var_id=StringVar()

#====titre==========
        title=Label(self.root,text="Infos Dépense",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
       

#=====frame========
    #=====dépenses======


        depenseFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        depenseFrame.place(x=0, y=30, width=310, height=460)

        #=====depense label and entry point =================================
        lbl_date=Label(depenseFrame,text="Date",font=("goudy old style",15),bg="white").place(x=0,y=50)
        date_entry = DateEntry(depenseFrame, date_pattern='dd/mm/yyyy',textvariable=self.var_date, width=18, background='darkblue', foreground='white', borderwidth=2, locale='fr_FR')
        date_entry.place(x=130, y=50, width=150, height=30)

        lbl_id=Label(depenseFrame,text="ID",font=("goudy old style",15),bg="white").place(x=0,y=10)
        txt_id = Entry(depenseFrame, textvariable=self.var_id, font=("goudy old style", 15), bg="lightyellow").place(x=130, y=10, width=50)



        lbl_cat2 = Label(depenseFrame, text="Machine", font=("goudy old style", 15), bg="white").place(x=0, y=90)
        self.cmb_cat2 = ttk.Combobox(depenseFrame, font=("goudy old style", 12), textvariable=self.var_cat2, state='readonly')
        self.cmb_cat2.place(x=130, y=90, width=150)
        self.populate_machine_names()

        lbl_type = Label(depenseFrame, text="Type", font=("goudy old style", 15), bg="white").place(x=0, y=130)
        self.cmb_type = ttk.Combobox(depenseFrame, font=("goudy old style", 12), textvariable=self.var_type, state='readonly')
        self.cmb_type['values'] = ['achat_des_pieces', 'maintenance', 'Divers']
        self.cmb_type.place(x=130, y=130, width=150)       


        lbl_desc=Label(depenseFrame,text="Description",font=("goudy old style",15),bg="white").place(x=0,y=170)
        self.txt_desc=Text(depenseFrame,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=130,y=170,width=150,height=100)

        lbl_montant=Label(depenseFrame,text="Montant",font=("goudy old style",15),bg="white").place(x=0,y=280)
        txt_montant = Entry(depenseFrame, textvariable=self.var_montant, font=("goudy old style", 15), bg="lightyellow").place(x=130, y=280, width=150)

        btn_save=Button(self.root,text="Sauvegarder",command=self.add,font=("goudy old style",12),bg="#2196f3",fg="white",cursor="hand2").place(x=170,y=350,width=100,height=30)
        btn_delete=Button(self.root,text="Supprimer",command=self.delete,font=("goudy old style",12),bg="#f44336",fg="white",cursor="hand2").place(x=170,y=390,width=100,height=30)

    #========searchFrame=========
        SearchFrame=LabelFrame(self.root,text="Recherche", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480, y=30, width=600,height=70)

    #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=(" ","Date","Categorie","Type"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Recherche",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

    #===== MAIN =================================
        mainFrame=LabelFrame(self.root, font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        mainFrame.place(x=320, y=120, width=770,height=370)
        scrolly=Scrollbar(mainFrame, orient=VERTICAL)
        scrollx=Scrollbar(mainFrame, orient=HORIZONTAL)

        self.DepTable=ttk.Treeview(mainFrame,columns=("depID","date","categorie","type","description","montant"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.DepTable.xview)
        scrolly.config(command=self.DepTable.yview)

        self.DepTable.heading("depID",text="Depense ID")
        self.DepTable.heading("date",text="Date")
        self.DepTable.heading("categorie",text="Categorie")
        self.DepTable.heading("type",text="Type")
        self.DepTable.heading("description",text="Description")
        self.DepTable.heading("montant",text="Montant")

        self.DepTable["show"] = "headings"

        self.DepTable.column("depID",width=50)
        self.DepTable.column("date",width=90)
        self.DepTable.column("categorie",width=100)
        self.DepTable.column("type",width=90)
        self.DepTable.column("description",width=120)
        self.DepTable.column("montant",width=100)
        self.DepTable.pack(fill=BOTH,expand=1)
        self.DepTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#============================================================================
    def add(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","Le ID du conducteur est requis", parent=self.root)
            else:
                cur.execute("Select * from depense where depID=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Ce ID existe deja, utilse un autre",parent=self.root)
                else:
                    cur.execute("Insert into depense (depID,date,categorie,type,description,montant) values(?,?,?,?,?,?)",(
                                        self.var_id.get(),
                                        self.var_date.get(),
                                        self.var_cat2.get(),
                                        self.var_type.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_montant.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Conducteur Ajouter avec success", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM depense")
            rows=cur.fetchall()
            self.DepTable.delete(*self.DepTable.get_children())
            for row in rows:
                self.DepTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def get_data(self,ev):
        f=self.DepTable.focus()
        content=(self.DepTable.item(f))
        row=content['values']
        #print(row)
        self.var_id.set(row[0])
        self.var_date.set(row[1])
        self.var_cat2.set(row[2])
        self.var_type.set(row[3])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[4])
        self.var_montant.set(row[5])

    def clear(self):
        f=self.DepTable.focus()
        content=(self.DepTable.item(f))
        row=content['values']
        #print(row)
        self.var_id.set("")
        self.var_date.set("")
        self.var_cat2.set("")
        self.var_type.set("")
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert("")
        self.var_montant.set("")

    def populate_conducteur_names(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT nom, prénom FROM conducteur")
            rows = cur.fetchall()
            self.cmb_cat1['values'] = [f"{row[0]} {row[1]}" for row in rows]
            # if self.cmb_cat1['values']:  # Set the first name as the default value if the list is not empty
            #     self.cmb_cat1.current(0)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)
        finally:
            con.close()

    def populate_machine_names(self):
        con = sqlite3.connect(database=r'btp.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT machine_name FROM machine")
            rows = cur.fetchall()
            machine_names = [row[0] for row in rows]
            self.cmb_cat2['values'] = machine_names
            # if machine_names:  # Set the first name as the default value if the list is not empty
            #     self.cmb_cat2.current(0)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)
        finally:
            con.close()

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
                valid_columns = ['Date', 'Categorie', 'Type']  # Example whitelist
                if self.var_searchby.get() in valid_columns:
                    # Using parameterized queries for the value part
                    query = f"SELECT * FROM depense WHERE {self.var_searchby.get()} LIKE ?"
                    cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.DepTable.delete(*self.DepTable.get_children())
                        for row in rows:
                            self.DepTable.insert('', END, values=row)
                    else:
                        messagebox.showerror("Error", "Pas de record!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "Invalid search column", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","Le ID est requis", parent=self.root)
            else:
                cur.execute("Select * from depense where depID=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid  ID",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Etes vous sure de vouloir supprimer ?",parent=self.root)
                    if op ==True:
                        cur.execute("delete from depense where depID=?",(self.var_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Info supprimer avec succes",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=depenseClass(root)
    root.mainloop()