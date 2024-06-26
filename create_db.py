import sqlite3
def create_db():
    con=sqlite3.connect(database='btp.db')
    cur=con.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS conducteur(condID INTEGER PRIMARY KEY AUTOINCREMENT, nom text,prénom text,genre text,ifu text,salaire text,email text,adresse text,contact text)")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "conducteur" (
	"condID"	INTEGER,
	"nom"	TEXT,
	"prénom"	TEXT,
	"genre"	TEXT,
	"ifu"	TEXT,
	"salaire"	TEXT,
	"email"	TEXT,
	"adresse"	TEXT,
	"contact"	TEXT,
	PRIMARY KEY("condID","nom")
)
    """)

    #cur.execute("CREATE TABLE IF NOT EXISTS machine (machine_id INTEGER PRIMARY KEY AUTOINCREMENT,machine_name text,owner text,return_time text,status text,price real,capacity real)")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "machine" (
	"machine_id"	INTEGER,
	"machine_name"	TEXT,
	"owner"	TEXT,
	"return_time"	TEXT,
	"status"	TEXT,
	"price"	INTEGER,
	"capacity"	REAL,
	PRIMARY KEY("machine_id" AUTOINCREMENT)
)
    """)
   
   
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS workinghours (
    #     date text PRIMARY KEY, 
    #     conducteur text, 
    #     heured REAL, 
    #     heurep REAL, 
    #     heurer REAL, 
    #     heuref REAL,
    #     heuret integer, 
    #     FOREIGN KEY (conducteur) REFERENCES conducteur(nom)
    # )
    # """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "workinghours" (
	"date"	TEXT,
	"conducteur"	TEXT,
	"heured"	NUMERIC,
	"heurep"	NUMERIC,
	"heurer"	NUMERIC,
	"heuref"	NUMERIC,
	"heuret"	INTEGER,
	"heureta"	INTEGER,
	"montant"	INTEGER,
	FOREIGN KEY("conducteur") REFERENCES "conducteur"("nom")
)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "gasoil" (
        "id"	INTEGER,
        "mois"	TEXT,
        "date"	TEXT,
        "nom"	TEXT,
        "machine_name"	TEXT,
        "capacityd"	REAL,
        "capacitya"	REAL,
        "capacityr"	REAL,
        PRIMARY KEY("id" AUTOINCREMENT),
        FOREIGN KEY("nom") REFERENCES "conducteur"("nom"),
        FOREIGN KEY("machine_name") REFERENCES "machine"("machine_name")
    )    
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS "essense" (
        "id"	INTEGER,
        "mois"	TEXT,
        "date"	TEXT,
        "nom"	TEXT,
        "machine_name"	TEXT,
        "capacityd"	REAL,
        "capacitya"	REAL,
        "capacityr"	REAL,
        PRIMARY KEY("id" AUTOINCREMENT),
        FOREIGN KEY("nom") REFERENCES "conducteur"("nom"),
        FOREIGN KEY("machine_name") REFERENCES "machine"("machine_name")
    )    
    """)


    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS perdieme (
    #     date text PRIMARY KEY, 
    #     conducteur text, 
    #     heured REAL, 
    #     heurep REAL, 
    #     heurer REAL, 
    #     heuref REAL,
    #     heuret integer, 
    #     FOREIGN KEY (conducteur) REFERENCES conducteur(nom)
    # )
    # """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "perdieme" (
	"date"	TEXT,
	"conducteur"	TEXT,
	"heured"	TEXT,
	"heurep"	TEXT,
	"heurer"	TEXT,
	"heuref"	TEXT,
	"heuret"	INTEGER,
	"heureta"	INTEGER,
	"montant"	INTEGER,
	FOREIGN KEY("conducteur") REFERENCES "conducteur"("nom")
)
    """)

    #cur.execute("CREATE TABLE IF NOT EXISTS depense( depID INTEGER PRIMARY KEY AUTOINCREMENT,date text, categorie text, type text, description text,montant text)")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS "depense" (
	"depID"	INTEGER UNIQUE,
	"date"	TEXT,
	"categorie"	TEXT,
	"type"	TEXT,
	"description"	TEXT,
	"montant"	INTEGER,
	PRIMARY KEY("depID")
)
    """)

    con.commit()



create_db()