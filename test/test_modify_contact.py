from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test contact"))
    app.contact.modify_first_contact(Contact(firstname="Modified firstname"))


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test contact"))
    app.contact.modify_first_contact(Contact(address="Modified address"))