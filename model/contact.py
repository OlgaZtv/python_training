from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                 phone2=None, notes=None, id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    # переопределяем представление результатов в консоли - потому что по умолчанию мы видим только адрес памяти, а не значение
    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    # переопределяем функцию равенства - потому что python по умолчанию сравнивает физическое место в памяти (не реальное значение)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    # подготовить обходной путь для 'None' id если id = None присвоить большое значение - оно перемещается в конец списка, когда будет отсортировано
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
