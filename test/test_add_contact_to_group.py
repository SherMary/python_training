from model.contact import Contact
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    contact_list = app.contact.get_contact_list()
    contact = random.choice(contact_list)
    app.contact.add_contact_to_group_by_id(contact.id)
    #contact_list_in_group = app.contact.get_contact_list_from_group()
    #contact_list_in_group_db = db.get_contact_list_from_group()
    #assert sorted(contact_list_in_group) == sorted(contact_list_in_group_db)