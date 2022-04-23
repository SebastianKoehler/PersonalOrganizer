import unittest
from application.contactlist.contact import Contact


class MyContactTest(unittest.TestCase):

    def test_creating_contact_with_full_informations(self):

        contact = Contact(
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

        self.assertTrue(contact.relation == "Privat")
        self.assertTrue(contact.firstName == "Hans")
        self.assertTrue(contact.middleName == "Gregor")
        self.assertTrue(contact.lastName == "Schmidt")
        self.assertTrue(contact.birthday == "19.03.1978")
        self.assertTrue(contact.prefixMobileNumber == "0176")
        self.assertTrue(contact.mobileNumber == "69429175")
        self.assertTrue(contact.prefixPhoneNumber == "0341")
        self.assertTrue(contact.phoneNumber == "2334510")
        self.assertTrue(contact.firstEmail == "HansSchmidt@anbieter.de")
        self.assertTrue(contact.secondEmail == "Hans.Gregor.Schmidt@it.de")

    def test_creating_contact_with_just_the_firstname(self):

        contact = Contact(
            relation="",
            firstName="Peter",
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

        self.assertTrue(contact.relation == "")
        self.assertTrue(contact.firstName == "Peter")
        self.assertTrue(contact.middleName == "")
        self.assertTrue(contact.lastName == "")
        self.assertTrue(contact.birthday == "")
        self.assertTrue(contact.prefixMobileNumber == "")
        self.assertTrue(contact.mobileNumber == "")
        self.assertTrue(contact.prefixPhoneNumber == "")
        self.assertTrue(contact.phoneNumber == "")
        self.assertTrue(contact.firstEmail == "")
        self.assertTrue(contact.secondEmail == "")

    def test_throw_error_when_no_firstname(self):
        with self.assertRaises(Exception, msg="Es muss mindestens ein Vorname angegeben werden!"):
            contact = Contact(
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
            
            self.assertIsNone(contact)
            

if __name__ == '__main__':
    unittest.main()
