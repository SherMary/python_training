from model.contact import Contact
import random


def test_modify_contact_firstname_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact", lastname="Modified lastname"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = Contact(firstname="Modified firstname", lastname="Modified lastname")
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = db.get_contact_list()
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Test contact"))
#    app.contact.modify_first_contact(Contact(address="Modified address"))