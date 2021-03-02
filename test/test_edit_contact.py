from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test",
                     address="testtest", home="1235", mobile="12345", email="test", bday="5", bmonth="March",
                     byear="1980", address2="test", phone2="45657", notes="test"))
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="Vanya", lastname="Sergeev")
    contact.id = old_contact_list[0].id
    app.contact.edit(contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
