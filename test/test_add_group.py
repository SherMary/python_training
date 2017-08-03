# -*- coding: utf-8 -*-
import pytest

from fixture.application import Apllication
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Apllication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="New group", header="Group's header", footer="Group's footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

