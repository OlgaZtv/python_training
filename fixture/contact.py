from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def edit_contact_by_index(self, index, new_contacts_form):
        wd = self.app.wd
        self.open_home_page()
        # init contact edition
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact(new_contacts_form)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit(self):
        self.edit_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # init contact deletion
        wd.find_elements_by_name("selected[]")[index].click()
        # delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # alert acceptation
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def fill_contact(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_fileld_value("firstname", contact.firstname)
        self.change_fileld_value("middlename", contact.middlename)
        self.change_fileld_value("lastname", contact.lastname)
        self.change_fileld_value("nickname", contact.nickname)
        self.change_fileld_value("title", contact.title)
        self.change_fileld_value("company", contact.company)
        self.change_fileld_value("address", contact.address)
        self.change_fileld_value("home", contact.home)
        self.change_fileld_value("mobile", contact.mobile)
        self.change_fileld_value("work", contact.work)
        self.change_fileld_value("fax", contact.fax)
        self.change_fileld_value("email", contact.email)
        self.change_fileld_value("email2", contact.email2)
        self.change_fileld_value("email3", contact.email3)
        self.change_fileld_value("homepage", contact.homepage)
        self.change_fileld_value2("bday", contact.bday)
        self.change_fileld_value2("bmonth", contact.bmonth)
        self.change_fileld_value("byear", contact.byear)
        self.change_fileld_value2("aday", contact.aday)
        self.change_fileld_value2("amonth", contact.amonth)
        self.change_fileld_value("ayear", contact.ayear)
        self.change_fileld_value("address2", contact.address2)
        self.change_fileld_value("phone2", contact.phone2)
        self.change_fileld_value("notes", contact.notes)


    def change_fileld_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_fileld_value2(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).send_keys(text)


    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                firstname = element.find_element_by_xpath("./td[3]").text
                lastname = element.find_element_by_xpath("./td[2]").text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=contact_id))
        return list(self.contact_cache)
