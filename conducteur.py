from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class conducteurClass:
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

        self.var_cond_id=StringVar()
        self.var_name=StringVar()
        self.var_surname=StringVar()
        self.var_ifu=StringVar()
        self.var_contact=StringVar()
        self.var_salaryph=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar() 





    #========searchFrame=========
        SearchFrame=LabelFrame(self.root,text="Recherche Conducteur", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250, y=20, width=600,height=70)
    
    #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=(" ","Adresse","Nom","Prénom"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Recherche",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

    #=====title======
        title=Label(self.root,text="Infos Conducteur",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


    #=====content=====
    #=====ligne premier====
        #lbl_condid=Label(self.root,text="Cond ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Genre",font=("goudy old style",15),bg="white").place(x=370,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)


        #txt_condid=Entry(self.root,textvariable=self.var_cond_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150, width=180)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender, values=(" ","Masculin","Féminin"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
    
    #=====2nd line =====
        lbl_surname=Label(self.root,text="Nom",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_name=Label(self.root,text="Prénom(s)",font=("goudy old style",15),bg="white").place(x=370,y=190)
        lbl_ifu=Label(self.root,text="IFU",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_surname=Entry(self.root,textvariable=self.var_surname,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_ifu=Entry(self.root,textvariable=self.var_ifu,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

    #===3rd line=======
        lbl_address=Label(self.root,text="Adresse",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=370,y=230)
        lbl_salaryph=Label(self.root,text="Salaire",font=("goudy old style",15),bg="white").place(x=750,y=230)

        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=230,width=200,height=70)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
        txt_salaryph=Entry(self.root,textvariable=self.var_salaryph,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)   

    #========buttons===========
        btn_save=Button(self.root,text="Sauvegarder",command=self.add,font=("goudy old style",12),bg="#2196f3",fg="white",cursor="hand2").place(x=370,y=270,width=100,height=30)
        btn_maj=Button(self.root,text="Mettre a jour",command=self.update,font=("goudy old style",12),bg="#4caf50",fg="white",cursor="hand2").place(x=520,y=270,width=150,height=30)
        btn_suppr=Button(self.root,text="Supprimer",command=self.delete,font=("goudy old style",12),bg="#f44336",fg="white",cursor="hand2").place(x=720,y=270,width=100,height=30)
        btn_clear=Button(self.root,text="Effacer",command=self.clear,font=("goudy old style",12),bg="#607d8b",fg="white",cursor="hand2").place(x=870,y=270,width=100,height=30)
    
    
    #====Conducteur Details =====

        cond_frame = Frame(self.root,bd=3,relief=RIDGE)
        cond_frame.place(x=0,y=330,relwidth=1,height=155)

        scrolly=Scrollbar(cond_frame, orient=VERTICAL)
        scrollx=Scrollbar(cond_frame, orient=HORIZONTAL)

        #self.CondTable=ttk.Treeview(cond_frame,columns=("condID", "nom","prénom","genre","ifu","salaire","email","adresse","contact"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        self.CondTable=ttk.Treeview(cond_frame,columns=("nom","prénom","genre","ifu","salaire","email","adresse","contact"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CondTable.xview)
        scrolly.config(command=self.CondTable.yview)
        
        #self.CondTable.heading("condID",text="Cond ID")
        self.CondTable.heading("nom",text="Nom")
        self.CondTable.heading("prénom",text="Prénom (s)")
        self.CondTable.heading("genre",text="Genre")
        self.CondTable.heading("ifu",text="IFU")
        self.CondTable.heading("salaire",text="Salaire")
        self.CondTable.heading("email",text="Email")
        self.CondTable.heading("adresse",text="Adresse")
        self.CondTable.heading("contact",text="Contact")

        self.CondTable["show"]="headings"

        #self.CondTable.column("condID",width=90)
        self.CondTable.column("nom",width=100)
        self.CondTable.column("prénom",width=100)
        self.CondTable.column("genre",width=100)
        self.CondTable.column("ifu",width=100)
        self.CondTable.column("salaire",width=100)
        self.CondTable.column("email",width=100)
        self.CondTable.column("adresse",width=100)
        self.CondTable.column("contact",width=100)
        self.CondTable.pack(fill=BOTH,expand=1)
        self.CondTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#============================================================================
    def add(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            # if self.var_cond_id.get()=="":
            #     messagebox.showerror("Error","Le ID du conducteur est requis", parent=self.root)
            # else:
            #     cur.execute("Select * from conducteur where condID=?",(self.var_cond_id.get(),))
            #     row=cur.fetchone()
            #     if row != None:
            #         messagebox.showerror("Error","Ce ID existe deja, utilse un autre",parent=self.root)
            #     else:
                    cur.execute("Insert into conducteur ( nom,prénom,genre,ifu,salaire,email,adresse,contact) values(?,?,?,?,?,?,?,?)",(
                                        # self.var_cond_id.get(),
                                        self.var_surname.get(),
                                        self.var_name.get(),
                                        self.var_gender.get(),
                                        self.var_ifu.get(),
                                        self.var_salaryph.get(),
                                        self.var_email.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_contact.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Conducteur Ajouter avec success", parent=self.root)
                    #self.var_cond_id.set(cur.lastrowid)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT nom,prénom,genre,ifu,salaire,email,adresse,contact FROM conducteur")
            rows=cur.fetchall()
            self.CondTable.delete(*self.CondTable.get_children())
            for row in rows:
                self.CondTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def get_data(self,ev):
        f=self.CondTable.focus()
        content=(self.CondTable.item(f))
        row=content['values']
        #print(row)
        #self.var_cond_id.set(row[0])
        self.var_surname.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_ifu.set(row[3])
        self.var_salaryph.set(row[4])
        self.var_email.set(row[5])
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[6]),
        self.var_contact.set(row[7])

    def update(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_cond_id.get()=="":
                messagebox.showerror("Error","Le ID du conducteur est requis", parent=self.root)
            else:
                cur.execute("Select * from conducteur where condID=?",(self.var_cond_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Conducteur ID",parent=self.root)
                else:
                    cur.execute("Update conducteur set prénom=?,genre=?,ifu=?,salaire=?,email=?,adresse=?,contact=? where nom=? ",(                                        self.var_surname.get(),
                                        self.var_name.get(),
                                        self.var_gender.get(),
                                        self.var_ifu.get(),
                                        self.var_salaryph.get(),
                                        self.var_email.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_contact.get(),
                                        self.var_name.get(),
                                        #self.var_cond_id.get(),
                                       
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Conducteur mise a jour avec success", parent=self.root)
                    #self.var_cond_id.set(cur.lastrowid)
                    self.show()
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def delete(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_surname.get()=="":
                messagebox.showerror("Error","Le nom du conducteur est requis", parent=self.root)
            else:
                cur.execute("Select * from conducteur where nom=?",(self.var_surname.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Conducteur nom",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Etes vous sure de vouloir suprimer le conducteur?",parent=self.root)
                    if op ==True:
                        cur.execute("delete from conducteur where nom=?",(self.var_surname.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Conducteur supprimer avec succes",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}",parent=self.root)

    def clear(self):
        #self.var_cond_id.set("")
        self.var_surname.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_ifu.set("")
        self.var_salaryph.set("")
        self.var_email.set("")
        self.txt_address.delete('1.0',END)
        self.var_contact.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set(" ")
        self.show()

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
                valid_columns = ['Adresse', 'Nom', 'Prénom']  # Example whitelist
                if self.var_searchby.get() in valid_columns:
                    # Using parameterized queries for the value part
                    query = f"SELECT * FROM conducteur WHERE {self.var_searchby.get()} LIKE ?"
                    cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.CondTable.delete(*self.CondTable.get_children())
                        for row in rows:
                            self.CondTable.insert('', END, values=row)
                    else:
                        messagebox.showerror("Error", "Pas de record!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "Invalid search column", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=conducteurClass(root)
    root.mainloop()