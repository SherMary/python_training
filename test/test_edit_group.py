from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    app.session.logout()
