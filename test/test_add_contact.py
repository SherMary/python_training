# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Doctor",
                               middlename="???",
                               lastname="Who",
                               nickname="Clever boy",
                               title="Doctor Who?",
                               company="Masters of time",
                               address="Galifray",
                               telhome="1235632",
                               telmobile="70008549303",
                               telwork="8903994308",
                               fax="48390275902",
                               email="doctorwho86@gal.com",
                               email2="cleverboy@tardis.net",
                               email3="whowho@clever.com",
                               homepage="doctorwho.com",
                               birth="1000",
                               anniversary="1500",
                               address2="Galifray dimension",
                               home2="PlanetGalifray",
                               notes="Somwhere far beyond")
    app.contact.create(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
