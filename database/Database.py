import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect('organizer.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS contacts ("
            "contact_id INTEGER PRIMARY KEY,"
            "vorname text,"
            "nachname text,"
            "telefonnummer integer,)"
        )
        self.connection.commit()
        
    def selectALL(self):

        self.cursor.execute(
            "SELECT * FROM contacts"
        )
        rows = self.cursor.fetchall()
        return rows

    def selectByID(self, contact_id):

        self.cursor.execute(
            "SELECT * FROM contacts WHERE contact_id=?",
            (contact_id,)
        )
        rows = self.cursor.fetchall()
        return rows

    def selectByFirstName(self, vorname):

        self.cursor.execute(
            "SELECT * FROM contacts WHERE vorname LIKE ?",
            ('%'+vorname+'%',)
        )
        rows = self.cursor.fetchall()
        return rows

    def selectByLastName(self, nachname):

        self.cursor.execute(
            "SELECT * FROM contacts WHERE nachname LIKE ?",
            ('%'+nachname+'%',)
        )
        rows = self.cursor.fetchall()
        return rows

    def selectByPhoneNumber(self, telefonnummer):

        self.cursor.execute(
            "SELECT * FROM contacts WHERE telefonnummer LIKE ?",
            ('%'+telefonnummer+'%',)
        )
        rows = self.cursor.fetchall()
        return rows

    def fetch(self, query):

        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def insert(self, vorname, nachname, telefonnummer):

        self.cursor.execute(
            "INSERT INTO contacts"
            "VALUES (NULL, ?, ?, ?)",
            (vorname, nachname, telefonnummer)
        )
        self.connection.commit()

    def remove(self, contact_id):

        self.cursor.execute(
            "DELETE FROM contacts WHERE id=?",
            (contact_id,)
        )
        self.connection.commit()

    def update(self, contact_id, vorname, nachname, telefonnummer):

        self.cursor.execute(
            "UPDATE contacts SET "
            "vorname = ?,"
            "nachname = ?,"
            "telefonnummer = ?"
            "WHERE contact_id = ?",
            (vorname, nachname, telefonnummer, contact_id)
        )
        self.connection.commit()

    def __del__(self):

        self.connection.close()
