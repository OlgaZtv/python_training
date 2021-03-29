# -*- coding: utf-8 -*-
import random


def test_add_contact_to_group(app, ormdb):
    exception_group_list = []
    # берем случайный контакт из бд
    contact = random.choice(ormdb.get_contact_list())
    # для выбранного контакта определяем группу в которую он не входит:
    # берем список групп в которые входит контакт
    list_groups_for_contact = ormdb.get_groups_for_contact(contact)
    # берем список всех групп
    list_all_groups = ormdb.get_group_list()
    # составляем список групп в которые контакт не входит
    # (идем по списку всех групп и если встречаем отсутсвующую в list_groups_for_contact заносим в новый list)
    for gr in list_all_groups:
        if gr not in list_groups_for_contact:
            exception_group_list.append(gr)
    # дополнительно проверяем, что контакт, не находится во всех существующих группах
    if len(exception_group_list) == 0:
        # если это так, удаляем его из одной случайной группы
        group = list_groups_for_contact[random.randrange(len(list_groups_for_contact))]
        app.contact.remove_from_group(contact, group)
    else:
        # из списка групп в которые контакт не входит, выбираем случайную
        index = random.randrange(len(exception_group_list))
        group = list_all_groups[index]
    # добавляем контакт в группу
    app.contact.add_contact_to_group(contact, group)



