import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:
    # делаем конструктор
    def __init__(self, host, name, user, password):
        # передаем полученные значения в поля созданного объекта
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # делаем коннект к бд (autocommit=True сбрасываем кеш после каждого запроса)
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    # метод для получения списка групп из бд (вместо считывания данных вебдрайвером с ui: fixture/group.py -
    # get_group_list)
    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                # создаем объект group и в него заносим необходимые данные из БД и заносим все полученные объекты в
                # список
                (id, name, header, footer) = row
                # id конвертим в string т.к. в тесте сравнения данных (test_db_matches_ui.py) c UI приходит ID как
                # string
                Group(id=id, name=name, header=header, footer=footer)
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    # метод для зачистки (закрываем соединение к бд). Открыто все время пока существует фикстура
    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                # создаем объект contacts и в него заносим необходимые данные из БД и заносим все полученные объекты в
                # список
                (id, firstname, lastname) = row
                # id конвертим в string т.к. c UI приходит ID как string
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

