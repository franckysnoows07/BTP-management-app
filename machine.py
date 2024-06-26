import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

class MachineClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Machine Management System")
        self.root.config(bg="white")

        # Variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_machine_id = StringVar()
        self.var_machine_name = StringVar()
        self.var_owner = StringVar()
        self.var_return_time = StringVar()
        self.var_status = StringVar()
        self.var_machine_price = StringVar()
        self.var_machine_capacity = StringVar()

        # Machine Frame
        machine_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        machine_frame.place(x=10, y=10, width=450, height=480)

        # Title
        title = Label(machine_frame, text="Machine Management", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        # Labels and Entries
        lbl_machine_id = Label(machine_frame, text="Machine ID", font=("goudy old style", 15), bg="white").place(x=30, y=60)
        txt_machine_id = Entry(machine_frame, textvariable=self.var_machine_id, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=60, width=200)

        lbl_machine_name = Label(machine_frame, text="Nom", font=("goudy old style", 15), bg="white").place(x=30, y=100)
        txt_machine_name = Entry(machine_frame, textvariable=self.var_machine_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=100, width=200)

        lbl_owner = Label(machine_frame, text="Propriété", font=("goudy old style", 15), bg="white").place(x=30, y=140)
        cmb_owner = ttk.Combobox(machine_frame, textvariable=self.var_owner, values=("Proprétaire", "Loué"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_owner.place(x=180, y=140, width=200)
        cmb_owner.current(0)

        lbl_return_time = Label(machine_frame, text="Date de Retour", font=("goudy old style", 15), bg="white").place(x=30, y=180)
        txt_return_time = Entry(machine_frame, textvariable=self.var_return_time, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=180, width=200)

        lbl_status = Label(machine_frame, text="Status", font=("goudy old style", 15), bg="white").place(x=30, y=220)
        cmb_status = ttk.Combobox(machine_frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=180, y=220, width=200)
        cmb_status.current(0)

        lbl_price = Label(machine_frame, text="Prix", font=("goudy old style", 15), bg="white").place(x=30, y=260)
        txt_price = Entry(machine_frame, textvariable=self.var_machine_price, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=260, width=200)

        lbl_capacity = Label(machine_frame, text="Capacité", font=("goudy old style", 15), bg="white").place(x=30, y=300)
        txt_capacity = Entry(machine_frame, textvariable=self.var_machine_capacity, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=300, width=200)

        # Buttons
        btn_add = Button(machine_frame, text="Ajouter", command=self.add_machine, font=("goudy old style", 15), bg="#4caf50", fg="white").place(x=30, y=340, width=150, height=30)
        btn_update = Button(machine_frame, text="Mettre a jour", command=self.update_machine, font=("goudy old style", 15), bg="#2196f3", fg="white").place(x=190, y=340, width=150, height=30)
        btn_delete = Button(machine_frame, text="Supprimer", command=self.delete_machine, font=("goudy old style", 15), bg="#f44336", fg="white").place(x=30, y=380, width=150, height=30)
        btn_clear = Button(machine_frame, text="Effacer", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white").place(x=190, y=380, width=150, height=30)

    #========searchFrame=========
        SearchFrame=LabelFrame(self.root,text="Recherche Machine", font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480, y=10, width=600,height=80)
    
    #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=(" ","owner","machine_name","capacity"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Recherche",command=self.search_machine,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

        # Machine Details Frame
        details_frame = Frame(self.root, bd=3, relief=RIDGE)
        details_frame.place(x=480, y=100, width=600, height=400)

        scrolly = Scrollbar(details_frame, orient=VERTICAL)
        scrollx = Scrollbar(details_frame, orient=HORIZONTAL)

        self.MachineTable = ttk.Treeview(details_frame, columns=("machine_id", "machine_name", "owner", "return_time", "status", "price","capacity"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.MachineTable.xview)
        scrolly.config(command=self.MachineTable.yview)

        self.MachineTable.heading("machine_id", text="Machine ID")
        self.MachineTable.heading("machine_name", text="Nom")
        self.MachineTable.heading("owner", text="Propriété")
        self.MachineTable.heading("return_time", text="Date de retour")
        self.MachineTable.heading("status", text="Status")
        self.MachineTable.heading("price", text="Prix (CFA)")
        self.MachineTable.heading("capacity", text="Capacité (L)")

        self.MachineTable["show"] = "headings"  # Hide the default column

        self.MachineTable.column("machine_id", width=90, anchor=CENTER)
        self.MachineTable.column("machine_name", width=200, anchor="sw")
        self.MachineTable.column("owner", width=100, anchor=CENTER)
        self.MachineTable.column("return_time", width=200, anchor=CENTER)
        self.MachineTable.column("status", width=100, anchor=CENTER)
        self.MachineTable.column("price", width=100, anchor=CENTER)
        self.MachineTable.column("capacity", width=100, anchor=CENTER)

        self.MachineTable.pack(fill=BOTH, expand=1)
        self.MachineTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()  # To display the machines in the table

#============================================================================
    def add_machine(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_machine_id.get()=="":
                messagebox.showerror("Error","Le ID du conducteur est requis", parent=self.root)
            else:
                cur.execute("Select * from machine where machine_id=?",(self.var_machine_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Ce ID existe deja, utilse un autre",parent=self.root)
                else:
                    cur.execute("Insert into machine (machine_id,machine_name,owner,return_time,status,price,capacity) values(?,?,?,?,?,?,?)",(
                                        self.var_machine_id.get(),
                                        self.var_machine_name.get(),
                                        self.var_owner.get(),
                                        self.var_return_time.get(),
                                        self.var_status.get(),
                                        self.var_machine_price.get(),
                                        self.var_machine_capacity.get(),
                                       
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Machine Ajoutée avec success", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM machine")
            rows=cur.fetchall()
            self.MachineTable.delete(*self.MachineTable.get_children())
            for row in rows:
                self.MachineTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def get_data(self,ev):
        f=self.MachineTable.focus()
        content=(self.MachineTable.item(f))
        row=content['values']
        #print(row)
        self.var_machine_id.set(row[0])
        self.var_machine_name.set(row[1])
        self.var_owner.set(row[2])
        self.var_return_time.set(row[3])
        self.var_status.set(row[4])
        self.var_machine_price.set(row[5])
        self.var_machine_capacity.set(row[6])

    def update_machine(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_machine_id.get()=="":
                messagebox.showerror("Error","Le ID de la machine est requis", parent=self.root)
            else:
                cur.execute("Select * from machine where machine_id=?",(self.var_machine_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Machine ID",parent=self.root)
                else:
                    cur.execute("Update machine set machine_name=?,owner=?,return_time=?,status=?,price=?,capacity=? where machine_id=? ",(
                                        self.var_machine_name.get(),
                                        self.var_owner.get(),
                                        self.var_return_time.get(),
                                        self.var_status.get(),
                                        self.var_machine_price.get(),
                                        self.var_machine_capacity.get(),
                                        self.var_machine_id.get(),
                                       
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Machine mise a jour avec success", parent=self.root)
                    self.show()
                   # con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}")

    def delete_machine(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_machine_id.get()=="":
                messagebox.showerror("Error","Le ID de la machine est requis", parent=self.root)
            else:
                cur.execute("Select * from machine where machine_id=?",(self.var_machine_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid machine ID",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Etes vous sure de vouloir suprimer la machine ?",parent=self.root)
                    if op ==True:
                        cur.execute("delete from machine where machine_id=?",(self.var_machine_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Machine supprimée avec succes",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Erreur due a :{str(ex)}",parent=self.root)

    def clear(self):
        self.var_machine_id.set("")
        self.var_machine_name.set("")
        self.var_owner.set("")
        self.var_return_time.set("")
        self.var_status.set("")
        self.var_machine_price.set("")
        self.var_machine_capacity.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set(" ")
        self.show()

    def search_machine(self):
        con=sqlite3.connect(database=r'btp.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get() == " ":
                messagebox.showerror("Error", "Choisisser l'un des option disponibles", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Entrez une valeur", parent=self.root)
            else:
                # Validate the column name against a whitelist
                valid_columns = ['owner', 'machine_name', 'capacity']  # Example whitelist
                if self.var_searchby.get() in valid_columns:
                    # Using parameterized queries for the value part
                    query = f"SELECT * FROM machine WHERE {self.var_searchby.get()} LIKE ?"
                    cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        self.MachineTable.delete(*self.MachineTable.get_children())
                        for row in rows:
                            self.MachineTable.insert('', END, values=row)
                    else:
                        messagebox.showerror("Error", "Pas de record!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "Invalid search column", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Erreur due a :{str(ex)}", parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=MachineClass(root)
    root.mainloop()