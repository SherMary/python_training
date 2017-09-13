

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.telhome == contact_from_edit_page.telhome
    assert contact_from_home_page.telwork == contact_from_edit_page.telwork
    assert contact_from_home_page.telmobile == contact_from_edit_page.telmobile
    assert contact_from_home_page.home2 == contact_from_edit_page.home2
