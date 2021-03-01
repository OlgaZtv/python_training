from model.contact import Contact


def test_edit_contact(app):
    old_contact_list = app.contact.get_contact_list
    contact = Contact(firstname="Vanya", middlename="Sergeevich", lastname="Sergeev", nickname="Vanya", title="Vanyaya", company="Ltd Vanya", address="Saint-Petersburg, Nevskyi 45", home="+78124555555", mobile="+76665554433", work="881266677888", fax="881266677766", email="ivanov@mail.ru", email2="vanya_work@mail.ru", email3="vanya_prevate@mail.ru", homepage="vanya.ya.ru", bday="5", bmonth="May", byear="1983", aday="4", amonth="August", ayear="2005", adress2="Saint-Petersburg, Zanevsky 15", phone2="Magnitogorskaya, 40", notes="Anna`s friend")
    contact.id = old_contact_list[0].id
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit(Contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact)
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
