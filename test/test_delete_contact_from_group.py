from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact_list = app.contact.get_contact_list()
    contact = random.choice(contact_list)
    app.contact.del_contact_from_group_by_id(contact.id)
    contact_list_in_group_db = db.get_contacts_in_group(Group(id='12'))
    contact_list.remove(contact)
    assert sorted(contact_list, key=Contact.id_or_max) == sorted(contact_list_in_group_db, key=Contact.id_or_max)