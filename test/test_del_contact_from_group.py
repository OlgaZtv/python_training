from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, ormdb):
    group = None
    # проверить есть ли контакты
    if len(ormdb.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="TestTest", middlename="Test", lastname="Testing", nickname="testing",
                        title="test", company="Test test", address="Spb", home="000222111",
                        mobile="444555222", work="99966655", fax="11122255", email="test@tesr.ru",
                        email2="test2@test.ru", email3="test3@test.ru", homepage="www.test.ru", bday="15",
                        bmonth="May", byear="1985", aday="14", amonth="June", ayear="1985",
                        address2="Spb", phone2="111111", notes="Friend"))
    # проверить есть ли группы
    if len(ormdb.get_group_list()) == 0:
        app.group.create(
            Group(name="test1", header="test2", footer="test3"))
    # берем случайный контакт из бд
    contact = random.choice(ormdb.get_contact_list())
    # для выбранного контакта проверяем, что есть связь с группой, если нет - добавляем
    list_groups_for_contact = ormdb.get_groups_for_contact(contact)
    if (len(list_groups_for_contact)) == 0:
        group = random.choice(ormdb.get_group_list())
        app.contact.add_contact_to_group(contact, group)
    else:
        # определяем список групп, в которых находится контакт и выбираем одну случайную
        index = random.randrange(len(list_groups_for_contact))
        group = list_groups_for_contact[index]
        app.contact.del_from_group(contact, group)
