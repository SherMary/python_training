from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test"))
    old_groups = db.get_group_list()
    #index = randrange(len(old_groups))
    group_random = random.choice(old_groups)
    group = Group(name="Modified name")
    #group.id = old_groups[index].id
    app.group.modify_group_by_id(group_random.id, group)
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    #old_groups[index] = group
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    app.group.modify_first_group(Group(header="Modified header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
