import re
from model.contact import Contact
from random import randrange

def test_contacts(app, ormdb):
    random_index = randrange(app.contact.count())
    # взять все контакты с главной страницы
    contact_from_home_page = app.contact.get_contact_list()
    # взять все записи конатктов из бд
    contact_from_db = ormdb.get_contact_list()
    # сравниваем списки, сортируя
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)


def test_contact_info_on_main_page(app):
    if app.contact.amount() == 0:
        app.contact.create(
            Contact(firstname="TestTest", middlename="Test", lastname="Testing", nickname="testing",
                    title="test", company="Test test", address="Spb", home="000222111",
                    mobile="444555222", work="99966655", fax="11122255", email="test@tesr.ru",
                    email2="test2@test.ru", email3="test3@test.ru", homepage="www.test.ru", bday="15",
                    bmonth="May", byear="1985", aday="14", amonth="June", ayear="1985",
                    address2="Spb", phone2="111111", notes="Friend"))
    random_index = randrange(app.contact.amount())
    contact_from_home_page = app.contact.get_contact_list()[random_index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
