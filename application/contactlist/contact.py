class Contact:

    # constructor
    def __init__(self, firstName, **kwargs):
        # private attributes
        self.__relation = kwargs.get('relation')
        self.__firstName = firstName
        self.__middleName = kwargs.get('middleName')
        self.__lastName = kwargs.get('lastName')
        self.__birthday = kwargs.get('birthday')
        self.__prefixMobileNumber = kwargs.get('prefixMobileNumber')
        self.__mobileNumber = kwargs.get('mobileNumber')
        self.__prefixPhoneNumber = kwargs.get('prefixPhoneNumber')
        self.__phoneNumber = kwargs.get('phoneNumber')
        self.__firstEmail = kwargs.get('firstEmail')
        self.__secondEmail = kwargs.get('secondEmail')

        if firstName == "":
            raise Exception("Es muss mindestens ein Vorname angegeben werden!")

    # getter
    def get_relation(self):
        return self.__relation

    def get_firstName(self):
        return self.__firstName

    def get_middleName(self):
        return self.__middleName

    def get_lastName(self):
        return self.__lastName

    def get_birthday(self):
        return self.__birthday

    def get_prefixMobileNumber(self):
        return self.__prefixMobileNumber

    def get_mobileNumber(self):
        return self.__mobileNumber

    def get_prefixPhoneNumber(self):
        return self.__prefixPhoneNumber

    def get_phoneNumber(self):
        return self.__phoneNumber

    def get_firstEmail(self):
        return self.__firstEmail

    def get_secondEmail(self):
        return self.__secondEmail

    def get_contact(self):
        relation = self.__relation
        firstName = self.__firstName
        middleName = self.__middleName
        lastName = self.__lastName
        birthday = self.__birthday
        prefixMobileNumber = self.__prefixMobileNumber
        mobileNumber = self.__mobileNumber
        prefixPhoneNumber = self.__prefixPhoneNumber
        phoneNumber = self.__phoneNumber
        firstEmail = self.__firstEmail
        secondEmail = self.__secondEmail

        if relation == "": relation = "keine Angabe"
        if firstName == "": firstName = "keine Angabe"
        if middleName == "": middleName = "keine Angabe"
        if lastName == "": lastName = "keine Angabe"
        if birthday == "": birthday = "keine Angabe"
        if prefixMobileNumber == "": prefixMobileNumber = "keine Angabe"
        if mobileNumber == "": mobileNumber = "keine Angabe"
        if prefixPhoneNumber == "": prefixPhoneNumber = "keine Angabe"
        if phoneNumber == "": phoneNumber = "keine Angabe"
        if firstEmail == "": firstEmail = "keine Angabe"
        if secondEmail == "": secondEmail = "keine Angabe"

        if prefixMobileNumber == "keine Angabe" or mobileNumber == "keine Angabe":
            mobil = "keine Angabe"
        else:
            mobil = prefixMobileNumber + "\\" + mobileNumber

        if prefixPhoneNumber == "keine Angabe" or phoneNumber == "keine Angabe":
            house = "keine Angabe"
        else:
            house = prefixPhoneNumber + "\\ " + phoneNumber

        print(f"Beziehung:\t\t{relation}\n"
              f"Vorname:\t\t{firstName}\n"
              f"2. Vorname:\t\t{middleName}\n"
              f"Nachname:\t\t{lastName}\n"
              f"Geburtstag:\t\t{birthday}\n"
              f"Mobil:\t\t\t{mobil}\n"
              f"Festnetz:\t\t{house}\n"
              f"1. Email:\t\t{firstEmail}\n"
              f"2. Email:\t\t{secondEmail}\n")

    # setter
    def set_relation(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__relation = ""
        else:
            self.__relation = value

    def set_firstName(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__firstName = ""
        else:
            self.__firstName = value

    def set_middleName(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__middleName = ""
        else:
            self.__middleName = value

    def set_lastName(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__lastName = ""
        else:
            self.__lastName = value

    def set_birthday(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__birthday = ""
        else:
            self.__birthday = value

    def set_prefixMobileNumber(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__prefixMobileNumber = ""
        else:
            self.__prefixMobileNumber = value

    def set_mobileNumber(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__mobileNumber = ""
        else:
            self.__mobileNumber = value

    def set_prefixPhoneNumber(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__prefixPhoneNumber = ""
        else:
            self.__prefixPhoneNumber = value

    def set_phoneNumber(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__phoneNumber = ""
        else:
            self.__phoneNumber = value

    def set_firstEmail(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__firstEmail = ""
        else:
            self.__firstEmail = value

    def set_secondEmail(self, value):
        _ = str(value).strip()
        if _ == "":
            self.__secondEmail = ""
        else:
            self.__secondEmail = value

    def del_relation(self):
        del self.__relation
        self.__relation = ""

    def del_firstName(self):
        del self.__firstName
        self.__firstName = ""

    def del_middleName(self):
        del self.__middleName
        self.__middleName = ""

    def del_lastName(self):
        del self.__lastName
        self.__lastName = ""

    def del_birthday(self):
        del self.__birthday
        self.__birthday = ""

    def del_prefixMobileNumber(self):
        del self.__prefixMobileNumber
        self.__prefixMobileNumber = ""

    def del_mobileNumber(self):
        del self.__mobileNumber
        self.__mobileNumber = ""

    def del_prefixPhoneNumber(self):
        del self.__prefixPhoneNumber
        self.__prefixPhoneNumber = ""

    def del_phoneNumber(self):
        del self.__phoneNumber
        self.__phoneNumber = ""

    def del_firstEmail(self):
        del self.__firstEmail
        self.__firstEmail = ""

    def del_secondEmail(self):
        del self.__secondEmail
        self.__secondEmail = ""

    # properties
    relation = property(get_relation, set_relation, del_relation)
    firstName = property(get_firstName, set_firstName, del_firstName)
    middleName = property(get_middleName, set_middleName, del_middleName)
    lastName = property(get_lastName, set_lastName, del_lastName)
    birthday = property(get_birthday, set_birthday, del_birthday)
    prefixMobileNumber = property(get_prefixMobileNumber, set_prefixMobileNumber, del_prefixMobileNumber)
    mobileNumber = property(get_mobileNumber, set_mobileNumber, del_mobileNumber)
    prefixPhoneNumber = property(get_prefixPhoneNumber, set_prefixPhoneNumber, del_prefixPhoneNumber)
    phoneNumber = property(get_phoneNumber, set_phoneNumber, del_phoneNumber)
    firstEmail = property(get_firstEmail, set_firstEmail, del_firstEmail)
    secondEmail = property(get_secondEmail, set_secondEmail, del_secondEmail)
