from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    group_list = db.get_group_list()
    rand_group = random.choice(group_list)
    app.group.choose_group_to_view_contact_by_id(rand_group.id)

    if len(app.contact.get_contact_list()) > 0:
        contact_in_group_list = app.contact.get_contact_list()
        rand_contact = random.choice(contact_in_group_list)
        app.contact.remove_contact_from_group_by_id(rand_contact.id)
    else:
        app.open_home_page()
        contact_in_group_list = app.contact.get_contact_list()
        rand_contact = random.choice(contact_in_group_list)
        app.contact.select_contact_by_id(rand_contact.id)
        app.group.choose_group_to_add_contact_by_id(rand_group.id)
        app.contact.remove_contact_from_group_by_id(rand_contact.id)

    contact_list_in_group_db = db.get_contacts_in_group(Group(id=rand_group.id))
    contact_list_in_group_new = app.contact.get_contact_list()
    assert sorted(contact_list_in_group_db, key=Contact.id_or_max) == sorted(contact_list_in_group_new, key=Contact.id_or_max)


"""def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test contact"))
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact_list = app.contact.get_contact_list()
    contact = random.choice(contact_list)
    app.contact.del_contact_from_group_by_id(contact.id)
    contact_list_in_group_db = db.get_contacts_in_group(Group(id='12'))
    contact_list.remove(contact)
    assert sorted(contact_list, key=Contact.id_or_max) == sorted(contact_list_in_group_db, key=Contact.id_or_max)"""