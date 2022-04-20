from tkinter import Tk, Frame, StringVar, Entry, Label, Button, Text, Radiobutton, IntVar, LEFT

from gui.utils import *


class WindowMain(Tk):
    def __init__(self):
        super(WindowMain, self).__init__()
        # configuration
        self.title('Personal Organizer')
        self.geometry('500x350')
        self.resizable(False, False)
        self.iconbitmap('../icon/purple-monkey.ico')

        # variables
        textbox_var = StringVar()
        buttons_var = StringVar()
        radiobutton_var = IntVar()

        ###########################################################################################
        # Top Area
        # Frames
        frame_top = Frame(self)

        # Labels
        input_radiobutton_label = Label(frame_top, text="Triff eine Auswahl:", justify=LEFT, padx=20)

        # radiobuttons
        choice_radiobutton_add = Radiobutton(
            frame_top,
            text="Hinzufügen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(1),
            value=1,
            justify=LEFT)
        choice_radiobutton_update = Radiobutton(
            frame_top,
            text="Aktualisieren",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(2),
            value=2,
            justify=LEFT)
        choice_radiobutton_search = Radiobutton(
            frame_top,
            text="Suche",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(3),
            value=3,
            justify=LEFT)
        choice_radiobutton_remove = Radiobutton(
            frame_top,
            text="Entfernen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(4),
            value=4,
            justify=LEFT)

        # output field
        text_box = Text(frame_top, height=8, width=35)
        text_box.insert('end', "")
        text_box.config(state='disabled')

        ###########################################################################################
        # Bottom Area
        # Frames
        frame_bottom = Frame(self)

        # buttons
        quit_btn = Button(frame_bottom, text='Löschen', width=12, command=None)

        ###########################################################################################
        # Grid
        # Top
        # implementing the Frames
        frame_top.grid()
        # implementing the labels
        input_radiobutton_label.grid(row=0, column=0, sticky="NW")
        # implementing the textbox
        text_box.grid(row=0, column=1, rowspan=5)
        # implementing the radiobuttons
        choice_radiobutton_add.grid(row=1, column=0, sticky="NW")
        choice_radiobutton_update.grid(row=2, column=0, sticky="NW")
        choice_radiobutton_search.grid(row=3, column=0, sticky="NW")
        choice_radiobutton_remove.grid(row=4, column=0, sticky="NW")
        ###########################################################################################
        # Bottom
        # implementing the Frames
        frame_bottom.grid()
        # implementing the buttons
        quit_btn.grid(row=5, column=5)


class SearchWindow(Tk):
    def __init__(self):
        super(SearchWindow, self).__init__()
        # configuration
        self.title('Personal Organizer')
        self.geometry('500x350')
        self.resizable(False, False)
        self.iconbitmap('../icon/purple-monkey.ico')

        # variables
        textbox_var = StringVar()
        id_input_entry_var = StringVar()
        firstname_input_entry_var = StringVar()
        lastname_input_entry_var = StringVar()
        phoneNumber_input_entry_var = StringVar()
        buttons_var = StringVar()
        radiobutton_var = IntVar()

        ###########################################################################################
        # Top Area
        # Frames
        frame_top = Frame(self)

        # Labels
        input_radiobutton_label = Label(frame_top, text="Triff eine Auswahl:", justify=LEFT, padx=20)

        # radiobuttons
        choice_radiobutton_add = Radiobutton(
            frame_top,
            text="Hinzufügen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(1),
            value=1,
            justify=LEFT)
        choice_radiobutton_update = Radiobutton(
            frame_top,
            text="Aktualisieren",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(2),
            value=2,
            justify=LEFT)
        choice_radiobutton_search = Radiobutton(
            frame_top,
            text="Suche",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(3),
            value=3,
            justify=LEFT)
        choice_radiobutton_remove = Radiobutton(
            frame_top,
            text="Entfernen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(4),
            value=4,
            justify=LEFT)

        # output field
        text_box = Text(frame_top, height=8, width=35)
        text_box.insert('end', "")
        text_box.config(state='disabled')

        ###########################################################################################
        # Center Area
        # Frames
        frame_center = Frame(self)

        # Labels
        input_id_label = Label(frame_center, text='ID:', font=('bold', 12))
        input_firstName_label = Label(frame_center, text='Vorname:', font=('bold', 12))
        input_lastName_label = Label(frame_center, text='Nachname:', font=('bold', 12))
        input_phoneNumber_label = Label(frame_center, text='Telefon:', font=('bold', 12))

        # input fields
        id_input_entry = Entry(frame_center, textvariable=id_input_entry_var, width=20)
        firstname_input_entry = Entry(frame_center, textvariable=firstname_input_entry_var, width=20)
        lastname_input_entry = Entry(frame_center, textvariable=lastname_input_entry_var, width=20)
        phoneNumber_input_entry = Entry(frame_center, textvariable=phoneNumber_input_entry_var, width=20)

        ###########################################################################################
        # Bottom Area
        # Frames
        frame_bottom = Frame(self)

        # buttons
        search_btn = Button(frame_bottom, text='Suche', width=12, command=search_contact)
        clear_btn = Button(frame_bottom, text='Löschen', width=12, command=clear_fields)
        quit_btn = Button(frame_bottom, text='Löschen', width=12, command=None)

        ###########################################################################################
        # Grid
        # Top
        # implementing the Frames
        frame_top.grid()
        # implementing the labels
        input_radiobutton_label.grid(row=0, column=0, sticky="NW")
        # implementing the textbox
        text_box.grid(row=0, column=1, rowspan=5)
        # implementing the radiobuttons
        choice_radiobutton_add.grid(row=1, column=0, sticky="NW")
        choice_radiobutton_update.grid(row=2, column=0, sticky="NW")
        choice_radiobutton_search.grid(row=3, column=0, sticky="NW")
        choice_radiobutton_remove.grid(row=4, column=0, sticky="NW")
        ###########################################################################################
        # Center
        # implementing the Frames
        frame_center.grid()
        # implementing the labels
        input_id_label.grid(row=1, column=0)
        input_firstName_label.grid(row=1, column=2)
        input_lastName_label.grid(row=2, column=2)
        input_phoneNumber_label.grid(row=2, column=0)
        # implementing the entries
        id_input_entry.grid(row=1, column=1)
        firstname_input_entry.grid(row=1, column=3)
        lastname_input_entry.grid(row=2, column=3)
        phoneNumber_input_entry.grid(row=2, column=1)
        ###########################################################################################
        # Bottom
        # implementing the Frames
        frame_bottom.grid()
        # implementing the buttons
        search_btn.grid(row=5, column=0)
        clear_btn.grid(row=5, column=4)
        quit_btn.grid(row=5, column=5)


class AddWindow(Tk):
    def __init__(self):
        super(AddWindow, self).__init__()
        # configuration
        self.title('Personal Organizer')
        self.geometry('500x350')
        self.resizable(False, False)
        self.iconbitmap('../icon/purple-monkey.ico')

        # variables
        textbox_var = StringVar()
        firstname_input_entry_var = StringVar()
        lastname_input_entry_var = StringVar()
        phoneNumber_input_entry_var = StringVar()
        buttons_var = StringVar()
        radiobutton_var = IntVar()

        ###########################################################################################
        # Top Area
        # Frames
        frame_top = Frame(self)

        # Labels
        input_radiobutton_label = Label(frame_top, text="Triff eine Auswahl:", justify=LEFT, padx=20)

        # radiobuttons
        choice_radiobutton_add = Radiobutton(
            frame_top,
            text="Hinzufügen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(1),
            value=1,
            justify=LEFT)
        choice_radiobutton_update = Radiobutton(
            frame_top,
            text="Aktualisieren",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(2),
            value=2,
            justify=LEFT)
        choice_radiobutton_search = Radiobutton(
            frame_top,
            text="Suche",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(3),
            value=3,
            justify=LEFT)
        choice_radiobutton_remove = Radiobutton(
            frame_top,
            text="Entfernen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(4),
            value=4,
            justify=LEFT)

        # output field
        text_box = Text(frame_top, height=8, width=35)
        text_box.insert('end', "")
        text_box.config(state='disabled')

        ###########################################################################################
        # Center Area
        # Frames
        frame_center = Frame(self)

        # Labels
        input_id_label = Label(frame_center, text='ID:', font=('bold', 12))
        input_firstName_label = Label(frame_center, text='Vorname:', font=('bold', 12))
        input_lastName_label = Label(frame_center, text='Nachname:', font=('bold', 12))
        input_phoneNumber_label = Label(frame_center, text='Telefon:', font=('bold', 12))

        # input fields
        firstname_input_entry = Entry(frame_center, textvariable=firstname_input_entry_var, width=20)
        lastname_input_entry = Entry(frame_center, textvariable=lastname_input_entry_var, width=20)
        phoneNumber_input_entry = Entry(frame_center, textvariable=phoneNumber_input_entry_var, width=20)

        ###########################################################################################
        # Bottom Area
        # Frames
        frame_bottom = Frame(self)

        # buttons
        add_btn = Button(frame_bottom, text='Hinzufügen', width=12, command=add_contact)
        clear_btn = Button(frame_bottom, text='Löschen', width=12, command=clear_fields)
        quit_btn = Button(frame_bottom, text='Löschen', width=12, command=None)

        ###########################################################################################
        # Grid
        # Top
        # implementing the Frames
        frame_top.grid()
        # implementing the labels
        input_radiobutton_label.grid(row=0, column=0, sticky="NW")
        # implementing the textbox
        text_box.grid(row=0, column=1, rowspan=5)
        # implementing the radiobuttons
        choice_radiobutton_add.grid(row=1, column=0, sticky="NW")
        choice_radiobutton_update.grid(row=2, column=0, sticky="NW")
        choice_radiobutton_search.grid(row=3, column=0, sticky="NW")
        choice_radiobutton_remove.grid(row=4, column=0, sticky="NW")
        ###########################################################################################
        # Center
        # implementing the Frames
        frame_center.grid()
        # implementing the labels
        input_id_label.grid(row=1, column=0)
        input_firstName_label.grid(row=1, column=2)
        input_lastName_label.grid(row=2, column=2)
        input_phoneNumber_label.grid(row=2, column=0)
        # implementing the entries
        firstname_input_entry.grid(row=1, column=3)
        lastname_input_entry.grid(row=2, column=3)
        phoneNumber_input_entry.grid(row=2, column=1)
        ###########################################################################################
        # Bottom
        # implementing the Frames
        frame_bottom.grid()
        # implementing the buttons
        add_btn.grid(row=5, column=1)
        clear_btn.grid(row=5, column=4)
        quit_btn.grid(row=5, column=5)


class UpdateWindow(Tk):
    def __init__(self):
        super(UpdateWindow, self).__init__()
        # configuration
        self.title('Personal Organizer')
        self.geometry('500x350')
        self.resizable(False, False)
        self.iconbitmap('../icon/purple-monkey.ico')

        # variables
        textbox_var = StringVar()
        id_input_entry_var = StringVar()
        firstname_input_entry_var = StringVar()
        lastname_input_entry_var = StringVar()
        phoneNumber_input_entry_var = StringVar()
        buttons_var = StringVar()
        radiobutton_var = IntVar()

        ###########################################################################################
        # Top Area
        # Frames
        frame_top = Frame(self)

        # Labels
        input_radiobutton_label = Label(frame_top, text="Triff eine Auswahl:", justify=LEFT, padx=20)

        # radiobuttons
        choice_radiobutton_add = Radiobutton(
            frame_top,
            text="Hinzufügen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(1),
            value=1,
            justify=LEFT)
        choice_radiobutton_update = Radiobutton(
            frame_top,
            text="Aktualisieren",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(2),
            value=2,
            justify=LEFT)
        choice_radiobutton_search = Radiobutton(
            frame_top,
            text="Suche",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(3),
            value=3,
            justify=LEFT)
        choice_radiobutton_remove = Radiobutton(
            frame_top,
            text="Entfernen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(4),
            value=4,
            justify=LEFT)

        # output field
        text_box = Text(frame_top, height=8, width=35)
        text_box.insert('end', "")
        text_box.config(state='disabled')

        ###########################################################################################
        # Center Area
        # Frames
        frame_center = Frame(self)

        # Labels
        input_id_label = Label(frame_center, text='ID:', font=('bold', 12))
        input_firstName_label = Label(frame_center, text='Vorname:', font=('bold', 12))
        input_lastName_label = Label(frame_center, text='Nachname:', font=('bold', 12))
        input_phoneNumber_label = Label(frame_center, text='Telefon:', font=('bold', 12))

        # input fields
        id_input_entry = Entry(frame_center, textvariable=id_input_entry_var, width=20)
        firstname_input_entry = Entry(frame_center, textvariable=firstname_input_entry_var, width=20)
        lastname_input_entry = Entry(frame_center, textvariable=lastname_input_entry_var, width=20)
        phoneNumber_input_entry = Entry(frame_center, textvariable=phoneNumber_input_entry_var, width=20)

        ###########################################################################################
        # Bottom Area
        # Frames
        frame_bottom = Frame(self)

        # buttons
        update_btn = Button(frame_bottom, text='Aktualisieren', width=12, command=update_contact)
        clear_btn = Button(frame_bottom, text='Löschen', width=12, command=clear_fields)
        quit_btn = Button(frame_bottom, text='Löschen', width=12, command=None)

        ###########################################################################################
        # Grid
        # Top
        # implementing the Frames
        frame_top.grid()
        # implementing the labels
        input_radiobutton_label.grid(row=0, column=0, sticky="NW")
        # implementing the textbox
        text_box.grid(row=0, column=1, rowspan=5)
        # implementing the radiobuttons
        choice_radiobutton_add.grid(row=1, column=0, sticky="NW")
        choice_radiobutton_update.grid(row=2, column=0, sticky="NW")
        choice_radiobutton_search.grid(row=3, column=0, sticky="NW")
        choice_radiobutton_remove.grid(row=4, column=0, sticky="NW")
        ###########################################################################################
        # Center
        # implementing the Frames
        frame_center.grid()
        # implementing the labels
        input_id_label.grid(row=1, column=0)
        input_firstName_label.grid(row=1, column=2)
        input_lastName_label.grid(row=2, column=2)
        input_phoneNumber_label.grid(row=2, column=0)
        # implementing the entries
        id_input_entry.grid(row=1, column=1)
        firstname_input_entry.grid(row=1, column=3)
        lastname_input_entry.grid(row=2, column=3)
        phoneNumber_input_entry.grid(row=2, column=1)
        ###########################################################################################
        # Bottom
        # implementing the Frames
        frame_bottom.grid()
        # implementing the buttons
        update_btn.grid(row=5, column=2)
        clear_btn.grid(row=5, column=4)
        quit_btn.grid(row=5, column=5)


class RemoveWindow(Tk):
    def __init__(self):
        super(RemoveWindow, self).__init__()
        # configuration
        self.title('Personal Organizer')
        self.geometry('500x350')
        self.resizable(False, False)
        self.iconbitmap('../icon/purple-monkey.ico')

        # variables
        textbox_var = StringVar()
        id_input_entry_var = StringVar()
        buttons_var = StringVar()
        radiobutton_var = IntVar()

        ###########################################################################################
        # Top Area
        # Frames
        frame_top = Frame(self)

        # Labels
        input_radiobutton_label = Label(frame_top, text="Triff eine Auswahl:", justify=LEFT, padx=20)

        # radiobuttons
        choice_radiobutton_add = Radiobutton(
            frame_top,
            text="Hinzufügen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(1),
            value=1,
            justify=LEFT)
        choice_radiobutton_update = Radiobutton(
            frame_top,
            text="Aktualisieren",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(2),
            value=2,
            justify=LEFT)
        choice_radiobutton_search = Radiobutton(
            frame_top,
            text="Suche",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(3),
            value=3,
            justify=LEFT)
        choice_radiobutton_remove = Radiobutton(
            frame_top,
            text="Entfernen",
            padx=20,
            variable=radiobutton_var,
            command=open_choice(4),
            value=4,
            justify=LEFT)

        # output field
        text_box = Text(frame_top, height=8, width=35)
        text_box.insert('end', "")
        text_box.config(state='disabled')

        ###########################################################################################
        # Center Area
        # Frames
        frame_center = Frame(self)

        # Labels
        input_id_label = Label(frame_center, text='ID:', font=('bold', 12))

        # input fields
        id_input_entry = Entry(frame_center, textvariable=id_input_entry_var, width=20)

        ###########################################################################################
        # Bottom Area
        # Frames
        frame_bottom = Frame(self)

        # buttons
        remove_btn = Button(frame_bottom, text='Entfernen', width=12, command=remove_contact)
        clear_btn = Button(frame_bottom, text='Löschen', width=12, command=clear_fields)
        quit_btn = Button(frame_bottom, text='Löschen', width=12, command=None)

        ###########################################################################################
        # Grid
        # Top
        # implementing the Frames
        frame_top.grid()
        # implementing the labels
        input_radiobutton_label.grid(row=0, column=0, sticky="NW")
        # implementing the textbox
        text_box.grid(row=0, column=1, rowspan=5)
        # implementing the radiobuttons
        choice_radiobutton_add.grid(row=1, column=0, sticky="NW")
        choice_radiobutton_update.grid(row=2, column=0, sticky="NW")
        choice_radiobutton_search.grid(row=3, column=0, sticky="NW")
        choice_radiobutton_remove.grid(row=4, column=0, sticky="NW")
        ###########################################################################################
        # Center
        # implementing the Frames
        frame_center.grid()

        # implementing the labels
        input_id_label.grid(row=1, column=0)

        # implementing the entries
        id_input_entry.grid(row=1, column=1)
        ###########################################################################################
        # Bottom
        # implementing the Frames
        frame_bottom.grid()
        # implementing the buttons
        remove_btn.grid(row=5, column=3)
        clear_btn.grid(row=5, column=4)
        quit_btn.grid(row=5, column=5)
