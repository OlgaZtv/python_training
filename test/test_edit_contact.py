from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="Vanya", middlename="Sergeevich", lastname="Sergeev", nickname="Vanya", title="Vanyaya", company="Ltd Vanya", address="Saint-Petersburg, Nevskyi 45", home="+78124555555", mobile="+76665554433", work="881266677888", fax="881266677766", email="ivanov@mail.ru", email2="vanya_work@mail.ru", email3="vanya_prevate@mail.ru", homepage="vanya.ya.ru", bday="5", bmonth="May", byear="1983", aday="4", amonth="August", ayear="2005", adress2="Saint-Petersburg, Zanevsky 15", phone2="Magnitogorskaya, 40", notes="Anna`s friend"))
