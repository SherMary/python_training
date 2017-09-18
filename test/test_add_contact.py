# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 20),
                               middlename=random_string("middlename", 20),
                               lastname=random_string("lastname", 20),
                               nickname=random_string("nickname", 20),
                               title=random_string("title", 20),
                               company=random_string("company", 20),
                               address=random_string("address", 20),
                               telhome=random_string("telhome", 20),
                               telmobile=random_string("telmobile", 20),
                               telwork=random_string("telwork", 20),
                               fax=random_string("fax", 20),
                               email=random_string("email", 20),
                               email2=random_string("email2", 20),
                               email3=random_string("email3", 20),
                               homepage=random_string("homepage", 20),
                               birth=random_string("birth", 20),
                               anniversary=random_string("anniversary", 20),
                               address2=random_string("address2", 20),
                               home2=random_string("home2", 20),
                               notes=random_string("notes", 20))
            for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
