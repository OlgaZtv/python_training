from model.contact import Contact

import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    app.contact.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact)
    old_contact_list.remove(contact)
    assert old_contact_list == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max()) == sorted(app.contact.get_contact_list(),
                                                                      key=Contact.id_or_max())
