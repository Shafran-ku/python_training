# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_for_contact import Application_for_contact

#Инициализация фикстуры
@pytest.fixture #метка - инициализатор фикстуры
def app():
    fixture = Application_for_contact()
    request.addfinalizator(fixture.destroy)
    return fixture

def test_add_contact(app):  #тестовый метод, в качестве параметра принимают фикстуру
    app.open_home_page()
    app.login(wd, username="admin", password="secret")
    app.open_page_new_contact()
    app.create_new_contact(Contact(firstname="First name2", middlename="Middle name2", lastname="Last name2",
                                address="Address2", homephone="777777777", email="mail@mail.ru"))
    app.move_to_home_page()
    app.logout()

def test_add_empty_contact(app):  #тестовый метод, в качестве параметра принимают фикстуру
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_page_new_contact()
    app.create_new_contact(wd, Contact(firstname="", middlename="", lastname="", address="", homephone="",
                               email=""))
    app.move_to_home_page()
    app.logout()
