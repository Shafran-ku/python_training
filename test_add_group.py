# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture                                   # метка, превращает функцию в инициализатор фикстуры
def app(request):                                 # функция создает фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)         # для разрушения фикстуры
    return fixture

def test_add_group(app):                            # тестовый метод, принимающий в качестве параметра фикстуру
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test5", header="xxx", footer="xxx"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

