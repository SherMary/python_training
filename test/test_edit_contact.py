from model.contact import Contact

def test_edit_contact(app):
    app.contact.edit_contact(Contact(firstname="Master",
                               middlename="Missi",
                               lastname="Cruel Person",
                               nickname="Selfish lady",
                               title="MASTER",
                               company="Lords of time",
                               address="Galifray?",
                               telhome="123-56-2",
                               telmobile="+7000854930",
                               telwork="+89 090 9430288",
                               fax="409238275902",
                               email="master86@gal.com",
                               email2="missiforever@tardis.net",
                               email3="wheredoctoris@clever.com",
                               homepage="mastermissi.com",
                               birth="1000",
                               anniversary="1500",
                               address2="Galifray dimension",
                               home2="Where doctor is",
                               notes="Somewhere far beyond!"))
