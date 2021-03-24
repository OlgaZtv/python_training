from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test",
                    address="testtest", home="1235", mobile="12345", email="test", bday="5", bmonth="March",
                    byear="1980", address2="test", phone2="45657", notes="test"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contact_list = db.get_contact_list()
    assert old_contact_list == new_contact_list
    if check_ui:
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
