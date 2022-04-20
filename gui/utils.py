from tkinter import messagebox, END




def clear_fields(vorname_entry, nachname_entry, telefonnummer_entry):
    vorname_entry.delete(0, END)
    nachname_entry.delete(0, END)
    telefonnummer_entry.delete(0, END)


def add_contact(db, vorname_entry, nachname_entry, telefonnummer_entry):
    if vorname_entry.get() == '' or nachname_entry.get() == '' or telefonnummer_entry.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(
        vorname_entry.get(),
        nachname_entry.get(),
        telefonnummer_entry.get())
    clear_fields()


def remove_contact(db, cid):
    db.remove(cid)
    clear_fields()


def update_contact(db, vorname_entry, nachname_entry, telefonnummer_entry):
    db.update(
        vorname_entry.get(),
        nachname_entry.get(),
        telefonnummer_entry.get())


def search_contact():

    user_input = ""
    if user_input == "cid":
        search_id()
    if user_input == "vorname_entry":
        search_vorname()
    if user_input == "nachname_entry":
        search_nachname()
    if user_input == "telefonnummer_entry":
        search_telefonnummer()
    else:
        print("Wrong Input!")


def search_id(cid):
    contact_id = cid.get()


def search_vorname(vorname_entry):
    vorname = vorname_entry.get()


def search_nachname(nachname_entry):
    nachname = nachname_entry.get()


def search_telefonnummer(telefonnummer_entry):
    telefonnummer = telefonnummer_entry.get()


def open_choice(value):

    if value == 1:
        from gui.gui import AddWindow
        window = AddWindow
        return window
    elif value == 2:
        from gui.gui import UpdateWindow
        window = UpdateWindow
        return window
    elif value == 3:
        from gui.gui import SearchWindow
        window = SearchWindow
        return window
    elif value == 4:
        from gui.gui import RemoveWindow
        window = RemoveWindow
        return window
