# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="1111112222", header="3wedwdsdsdsd", footer="ddddfff"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))



