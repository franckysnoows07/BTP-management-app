from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
import sqlite3
from tktimepicker import AnalogPicker, AnalogThemes
import math

class workingHoursClass:
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

        self.var_date=StringVar()
        self.var_name=StringVar()
        self.var_hours_bgn=StringVar()
        self.var_hours_pse=StringVar()
        self.var_hours_rep=StringVar()
        self.var_hours_fn=StringVar()
        self.var_hours_csm=StringVar()
        self.var_hours_tt=StringVar()
        self.var_hours_tt_arr=StringVar()
        self.var_montant=StringVar()
        


 #=====title======
        title=Label(self.root,text="Infos Heures",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

    #========searchFrame=========
        SearchFrame=LabelFrame(self.root,text="Recherche", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=350, y=30, width=700,height=70)

    #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=(" ","Date","Conducteur","Montant"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=30,y=8, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=250,y=8, height=30)
        btn_search=Button(SearchFrame,text="Recherche",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=490,y=8,width=150,height=30)


    #=====content=====
    #=====info frame=====
        infoFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        infoFrame.place(x=0, y=40, width=310, height=450)

    #=====ligne premier====
        lbl_name=Label(infoFrame,text="Conducteur",font=("goudy old style",15),bg="white").place(x=0,y=10)
        self.cmb_cond_name = ttk.Combobox(infoFrame, font=("goudy old style", 12),textvariable=self.var_name, state='readonly')
        self.cmb_cond_name.place(x=130, y=10, width=150)
        # Populate the combobox with conducteur names from the database
        self.populate_conducteur_names()

        lbl_date = Label(infoFrame, text="Date", font=("goudy old style", 15), bg="white").place(x=0, y=50)
        date_entry = DateEntry(infoFrame, date_pattern='dd/mm/yyyy',textvariable=self.var_date, width=18, background='darkblue', foreground='white', borderwidth=2, locale='fr_FR')
        date_entry.place(x=130, y=50, width=150, height=30)


        lbl_heure_db=Label(infoFrame,text="Heure début",font=("goudy old style",15),bg="white").place(x=0,y=90)
        self.txt_heure_db_h = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_db_h.place(x=175, y=90, width=25)
        lbl_deux_point=Label(infoFrame,text=":",font=("goudy old style",30),bg="white").place(x=202,y=75)
        self.txt_heure_db_m = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_db_m.place(x=220, y=90, width=25)
        
        
        lbl_heure_p=Label(infoFrame,text="Heure de pause",font=("goudy old style",15),bg="white").place(x=0,y=130)
        self.txt_heure_p_h = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_p_h.place(x=175, y=130, width=25)
        lbl_deux_point=Label(infoFrame,text=":",font=("goudy old style",30),bg="white").place(x=202,y=115)
        self.txt_heure_p_m = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_p_m.place(x=220, y=130, width=25)
        

        lbl_heure_rp=Label(infoFrame,text="Heure de reprise",font=("goudy old style",15),bg="white").place(x=0,y=170)
        self.txt_heure_rp_h = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_rp_h.place(x=175, y=170, width=25)
        lbl_deux_point=Label(infoFrame,text=":",font=("goudy old style",30),bg="white").place(x=202,y=155)
        self.txt_heure_rp_m = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_rp_m.place(x=220, y=170, width=25)


        lbl_heure_fn=Label(infoFrame,text="Heure de fin",font=("goudy old style",15),bg="white").place(x=0,y=210)
        self.txt_heure_fn_h = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_fn_h.place(x=175, y=210, width=25)
        lbl_deux_point=Label(infoFrame,text=":",font=("goudy old style",30),bg="white").place(x=202,y=195)
        self.txt_heure_fn_m = Entry(infoFrame, font=("goudy old style", 15))
        self.txt_heure_fn_m.place(x=220, y=210, width=25)

        lbl_montant=Label(infoFrame,text="Montant",font=("goudy old style",15),bg="white").place(x=0,y=250)
        txt_montant=Entry(infoFrame,textvariable=self.var_montant,font=("goudy old style",15),bg="lightyellow").place(x=130,y=250, width=150)



        #=====buttons =====
        btn_save=Button(infoFrame,text="Sauvegarder", command=self.add,font=("goudy old style",12),bg="#2196f3",fg="white",cursor="hand2").place(x=0,y=290,width=100,height=30)
        btn_clear=Button(infoFrame,text="Effacer",command=self.clear,font=("goudy old style",12),bg="#607d8b",fg="white",cursor="hand2").place(x=90,y=290,width=90,height=30)
        btn_suppr=Button(infoFrame,text="Supprimer",command=self.delete,font=("goudy old style",12),bg="#f44336",fg="white",cursor="hand2").place(x=180,y=290,width=100,height=30)


    #========searchFrame=========
        hour_Frame=LabelFrame(self.root, font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        hour_Frame.place(x=320, y=120, width=770,height=370)

        scrolly=Scrollbar(hour_Frame, orient=VERTICAL)
        scrollx=Scrollbar(hour_Frame, orient=HORIZONTAL)

        self.HourTable=ttk.Treeview(hour_Frame,columns=("date","conducteur","heured","heurep","heurer","heuref","heuret","heureta","montant"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.HourTable.xview)
        scrolly.config(command=self.HourTable.yview)
        
        self.HourTable.heading("date",text="Date")
        self.HourTable.heading("conducteur",text="Conducteur")
        self.HourTable.heading("heured",text="Heure début")
        self.HourTable.heading("heurep",text="Heure Pause")
        self.HourTable.heading("heurer",text="Heure reprise")
        self.HourTable.heading("heuref",text="Heure  fin")
        self.HourTable.heading("heuret",text="Durée")
        self.HourTable.heading("heureta",text="Durée arrondi")
        self.HourTable.heading("montant",text="Montant (CFA)")

        self.HourTable["show"]="headings"

        self.HourTable.column("date",width=90)
        self.HourTable.column("conducteur",width=100)
        self.HourTable.column("heured",width=100)
        self.HourTable.column("heurep",width=100)
        self.HourTable.column("heurer",width=100)
        self.HourTable.column("heuref",width=100)
        self.HourTable.column("heuret",width=100)
        self.HourTable.column("heureta",width=100)
        self.HourTable.column("montant",width=100)
        self.HourTable.pack(fill=BOTH,expand=1)
        self.HourTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()



    # Add this method to your gasoilClass
 
    def add(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            self.var_hours_bgn= str(self.txt_heure_db_h.get()) +" : "+ str(self.txt_heure_db_m.get())
            self.var_hours_pse= str(self.txt_heure_p_h.get()) +" : "+  str(self.txt_heure_p_m.get())
            self.var_hours_rep= str(self.txt_heure_rp_h.get()) +" : "+  str(self.txt_heure_rp_m.get())
            self.var_hours_fn= str(self.txt_heure_fn_h.get()) +" : "+  str(self.txt_heure_fn_m.get())
            self.var_hours_tt = int(int(int(self.txt_heure_p_h.get()) * 60 + int(self.txt_heure_p_m.get()) - int(self.txt_heure_db_h.get()) * 60 - int(self.txt_heure_db_m.get())) + int(int(self.txt_heure_fn_h.get()) * 60 + int(self.txt_heure_fn_m.get()) - int(self.txt_heure_rp_h.get()) * 60 - int(self.txt_heure_rp_m.get()))) / 60
            self.var_hours_tt_arr = math.ceil(self.var_hours_tt)
            cur.execute("Insert into workinghours (date,conducteur,heured,heurep,heurer,heuref,heuret,heureta,montant) values(?,?,?,?,?,?,?,?,?)",(
                                        self.var_date.get(),
                                        self.var_name.get(),
                                        self.var_hours_bgn,
                                        self.var_hours_pse,
                                        self.var_hours_rep,
                                        self.var_hours_fn,
                                        self.var_hours_tt,
                                        self.var_hours_tt_arr,
                                        self.var_montant.get(),
                    ))
            con.commit()
            messagebox.showinfo("Success", "Info  Ajouté avec success", parent=self.root)
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")


 
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


    def show(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM workinghours")
            rows=cur.fetchall()
            self.HourTable.delete(*self.HourTable.get_children())
            for row in rows:
                self.HourTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def get_data(self,ev):
        f=self.HourTable.focus()
        content=(self.HourTable.item(f))
        row=content['values']
        #print(row)
        self.var_date.set(row[0])
        self.var_name.set(row[1])
        # self.var_hours_bgn.set(row[2])
        # self.var_hours_pse.set(row[3])
        # self.var_hours_rep.set(row[4])
        # self.var_hours_fn.set(row[5])

    def delete(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
                    op=messagebox.askyesno("confirm","Etes vous sure de vouloir suprimer les données?",parent=self.root)
                    if op ==True:
                        cur.execute("delete from workinghours where date=? and conducteur=?",(self.var_date.get(),self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Donnée supprimer avec succes",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}",parent=self.root)

    def clear(self):
        self.var_date.set("")
        self.var_name.set("")
        self.var_hours_bgn.set("")
        self.var_hours_pse.set("")
        self.var_hours_rep.set("")
        self.var_hours_fn.set("")
        self.var_hours_tt.set("")
        self.var_montant.set("")
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
                valid_columns = ['Date', 'Conducteur', 'montant']  # Example whitelist
                if self.var_searchby.get() in valid_columns:
                    # Using parameterized queries for the value part
                    query = f"SELECT * FROM workinghours WHERE {self.var_searchby.get()} LIKE ?"
                    cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.HourTable.delete(*self.HourTable.get_children())
                        for row in rows:
                            self.HourTable.insert('', END, values=row)
                    else:
                        messagebox.showerror("Error", "Pas de record!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "Invalid search column", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=workingHoursClass(root)
    root.mainloop()