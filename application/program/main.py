from application.contactlist.contact import Contact
# from application.contactlist.contactlist import Contactlist


"""
    contact1 = Contact(
        relation="",
        firstName="",
        middleName="",
        lastName="",
        birthday="",
        prefixMobileNumber="",
        mobileNumber="",
        prefixPhoneNumber="",
        phoneNumber="",
        firstEmail="",
        secondEmail=""
    )
"""


def main():

    contact1 = Contact(
        relation="Privat",
        firstName="Hans",
        middleName="Gregor",
        lastName="Schmidt",
        birthday="19.03.1978",
        prefixMobileNumber="0176",
        mobileNumber="69429175",
        prefixPhoneNumber="0341",
        phoneNumber="2334510",
        firstEmail="HansSchmidt@anbieter.de",
        secondEmail="Hans.Gregor.Schmidt@it.de"
    )

    contact2 = Contact(
        relation="",
        firstName="",
        middleName="",
        lastName="",
        birthday="",
        prefixMobileNumber="",
        mobileNumber="",
        prefixPhoneNumber="",
        phoneNumber="",
        firstEmail="",
        secondEmail=""
    )

    contact1.get_contact()
    contact2.get_contact()


if __name__ == '__main__':
    main()
