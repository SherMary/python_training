# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Apllication


@pytest.fixture
def app(request):
    fixture = Apllication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="New group", header="Group's header", footer="Group's footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

