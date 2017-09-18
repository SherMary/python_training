import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
           contact_from_edit_page)


def test_emails_on_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert email_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
        email_from_edit_page)


def test_name_and_address_on_home_page(app):
    name_and_address_from_home_page = app.contact.get_contact_list()[0]
    name_and_address_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert name_and_address_from_home_page.firstname == name_and_address_from_edit_page.firstname
    assert name_and_address_from_home_page.lastname == name_and_address_from_edit_page.lastname
    assert name_and_address_from_home_page.address == name_and_address_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.telhome, contact.telmobile, contact.telwork, contact.home2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))