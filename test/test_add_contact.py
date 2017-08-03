# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from fixture.application import Apllication


@pytest.fixture
def app(request):
    fixture = Apllication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Doctor",
                               middlename="???",
                               lastname="Who",
                               nickname="Clever boy",
                               title="Doctor Who?",
                               company="Masters of time",
                               address="Galifray",
                               telhome="123-56-32",
                               telmobile="+7000854930403",
                               telwork="+89 039 9430288",
                               fax="48390275902",
                               email="doctorwho86@gal.com",
                               email2="cleverboy@tardis.net",
                               email3="whowho@clever.com",
                               homepage="doctorwho.com",
                               birth="1000",
                               anniversary="1500",
                               address2="Galifray dimension",
                               home2="Planet Galifray",
                               notes="Somwhere far beyond"))
    app.logout()

