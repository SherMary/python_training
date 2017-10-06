from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    app.contact.filter_not_in_group_contact()
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
        app.contact.filter_not_in_group_contact()
    contact_not_in_group = app.contact.get_contact_list()
    rand_contact = random.choice(contact_not_in_group)
    app.contact.select_contact_by_id(rand_contact.id)
    group_list = db.get_group_list()
    rand_group = random.choice(group_list)
    app.group.choose_group_to_add_contact_by_id(rand_group.id)
    contact_list_in_group_db = db.get_contacts_in_group(Group(id=rand_group.id))
    contact_list_in_group = app.contact.get_contact_list()
    assert sorted(contact_list_in_group, key=Contact.id_or_max) == sorted(contact_list_in_group_db, key=Contact.id_or_max)



