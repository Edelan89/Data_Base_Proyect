from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()

#----------------------- Data Base ------------------

def conexionBaseDatos():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        USER_NAME VARCHAR(50),
                        PASSWORD VARCHAR(50),
                        LAST_NAME VARCHAR(30),
                        ADRESS VARCHAR(50),
                        COMMENTS CARCHAR(200)
            )
            ''')
        
        messagebox.showinfo('Data Base', 'The data base has been created')

    except:
        messagebox.showwarning('Warning!','The data base already exists')

# --------------------- Pop Ups ---------------------


# def infoConexion():
#     messagebox.showinfo('Conexion', 'You have connected to the database')


def exitApp():
    valor = messagebox.askokcancel('Exit', 'Do you want close the program?')
    if valor == True:
        root.destroy()


def infoLicence():
    messagebox.showinfo('Licence', 'Edelan 2023')


def infoAbout():
    messagebox.showinfo('App', 'Practice Aplication')


def cleanFields():
    myId.set('')
    myName.set('')
    myLastName.set('')
    myPassword.set('')
    myAdress.set('')
    comments_entry.delete(1.0,END)

def create():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    '''miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ 
                     myName.get() +
                      "','" + myLastName.get() + 
                       "','" + myPassword.get() +
                        "','" + myAdress.get() + 
                         "','" + comments_entry.get("1.0", END) + "')")'''
    datos = myName.get(), myLastName.get(), myPassword.get(), myAdress.get(), comments_entry.get("1.0", END)

    miCursor.execute('INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)', (datos))

    miConexion.commit()

    messagebox.showinfo('Info','The information has been save successful :D')


def createAndClean():
    create()
    cleanFields()

def read():
    myConexion = sqlite3.connect('Usuarios')
    myCursor = myConexion.cursor()

    myCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + myId.get())

    usuario_read = myCursor.fetchall()

    for usuario in usuario_read:
        myId.set(usuario[0])
        myName.set(usuario[1])
        myLastName.set(usuario[2])
        myPassword.set(usuario[3])
        myAdress.set(usuario[4])
        comments_entry.insert(1.0, usuario[5])

    myConexion.commit()

def update():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    '''miCursor.execute("UPDATE DATOSUSUARIOS SET USER_NAME= '" + myName.get() +
                     "', LAST_NAME='" + myLastName.get() +
                     "', PASSWORD='" + myPassword.get() +
                     "', ADRESS='" + myAdress.get() +
                     "', COMMENTS='" + comments_entry.get('1.0', END) +
                     "' WHERE ID=" + myId.get())'''
    
    datos = myName.get(), myLastName.get(), myPassword.get(), myAdress.get(), comments_entry.get("1.0", END)

    miCursor.execute("UPDATE DATOSUSUARIOS SET USER_NAME=?, LAST_NAME=?, PASSWORD=?, ADRESS=?, COMMENTS=?" + "WHERE ID=" + myId.get(), (datos))
    
    miConexion.commit()

    messagebox.showinfo('Info','The information has been updated :D')

def delete():
    miConexion = sqlite3.connect('Usuarios')
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + myId.get())
    miConexion.commit()

    messagebox.showinfo('Info','The record has been deleted')

# ------------------ cascades -----------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, height=300, width=300)

#-------------------- StringVars --------------------

myId = StringVar()
myName = StringVar()
myLastName = StringVar()
myPassword = StringVar()
myAdress = StringVar()

# ------------------ cascade BBDD -----------------------

BBDDMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='BBDD', menu=BBDDMenu)
BBDDMenu.add_command(label='Connect', command=conexionBaseDatos)
BBDDMenu.add_command(label='Exit', command=exitApp)
# ------------------------ cascade delete --------------------------
deleteMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Delete', menu=deleteMenu)
deleteMenu.add_command(label='Delete fields', command=cleanFields)

# ------------------------ cascade delete --------------------------
CRUDMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='CRUD', menu=CRUDMenu)
CRUDMenu.add_command(label='Create', command=createAndClean)
CRUDMenu.add_command(label='Read', command=read)
CRUDMenu.add_command(label='Update', command=update)
CRUDMenu.add_command(label='Delete', command=delete)

# ------------------------ cascade Help --------------------------
helpMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='Licence', command=infoLicence)
helpMenu.add_command(label='About of...', command=infoAbout)

# ------------------ Frame Boxes -----------------------

frame_boxes = Frame(root)
frame_boxes.pack()

# -------------------- ID -----------------------------

idLabel = Label(frame_boxes, text='ID: ')
idLabel.grid(row=0, column=0, padx=10, pady=10, sticky='e')

id_entry = Entry(frame_boxes, textvariable = myId)
id_entry.grid(row=0, column=1)
id_entry.config(justify='center')

# -------------------- Name -----------------------------

nameLabel = Label(frame_boxes, text='Name: ')
nameLabel.grid(row=1, column=0, padx=10, pady=10, sticky='e')

name_entry = Entry(frame_boxes, textvariable = myName)
name_entry.grid(row=1, column=1)
name_entry.config(justify='center')

# -------------------- Last Name -----------------------------

lastNameLabel = Label(frame_boxes, text='Last Name: ')
lastNameLabel.grid(row=2, column=0, padx=10, pady=10, sticky='e')

lastName_entry = Entry(frame_boxes, textvariable = myLastName)
lastName_entry.grid(row=2, column=1)
lastName_entry.config(justify='center')

# -------------------- Password -----------------------------

passwordLabel = Label(frame_boxes, text='Password: ')
passwordLabel.grid(row=3, column=0, padx=10, pady=10, sticky='e')

password_entry = Entry(frame_boxes, textvariable = myPassword )
password_entry.grid(row=3, column=1)
password_entry.config(show='*', justify='center')

# -------------------- Address -----------------------------

addressLabel = Label(frame_boxes, text='Address: ')
addressLabel.grid(row=4, column=0, padx=10, pady=10, sticky='e')

address_entry = Entry(frame_boxes, textvariable = myAdress)
address_entry.grid(row=4, column=1)
address_entry.config(justify='center')

# -------------------- Comment -----------------------------

commentsLabel = Label(frame_boxes, text='Comments: ')
commentsLabel.grid(row=5, column=0, padx=10, pady=10, sticky='e')

comments_entry = Text(frame_boxes, width=16, height=8)
comments_entry.grid(row=5, column=1)

ScrollVert = Scrollbar(frame_boxes, command=comments_entry.yview)
ScrollVert.grid(row=5, column=2, sticky='nsew')

comments_entry.config(yscrollcommand=ScrollVert.set)

# ------------------ Frame Buttom -----------------------

frame_button = Frame(root)
frame_button.pack()

createButton = Button(frame_button, text='Create', width=5, command=createAndClean)
createButton.grid(row=0, column=0, padx=10, pady=10, sticky='e')

readButton = Button(frame_button, text='Read', width=5, command=read)
readButton.grid(row=0, column=1, padx=10, pady=10, sticky='e')

updateButton = Button(frame_button, text='Update', width=5, command=update)
updateButton.grid(row=0, column=2, padx=10, pady=10, sticky='e')

deleteButton = Button(frame_button, text='Delete', width=5, command=delete)
deleteButton.grid(row=0, column=3, padx=10, pady=10, sticky='e')
# ------------------- end ---------------------------------
root.mainloop()
