# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contact_list = app.contact.get_contact_list
    app.contact.add_contact(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


