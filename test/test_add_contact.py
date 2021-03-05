# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IvanIvan", title="Ivanushka", company="Ltd Sokol", address="Saint-Petersburg, Nevskyi 21", home="+781266677799", mobile="+76665554433", work="881266677888", fax="881266677766", email="ivanov@mail.ru", email2="ivanov_work@mail.ru", email3="Ivanon_prevate@mail.ru", homepage="ivanov.ya.ru", bday="9", bmonth="April", byear="1972", aday="2", amonth="May", ayear="2002", address2="Saint-Petersburg, Zanevsky 5", phone2="Magnitogorskaya, 25", notes="Natasha`s friend")
    app.contact.add_contact(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


