from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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

    def modify_contact_by_index(self, index, new_contacts_form):
        wd = self.app.wd
        self.open_home_page()
        # init contact edition
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact(new_contacts_form)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit(self):
        self.modify_contact_by_index(0)

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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=contact_id, home=all_phones[0], mobile=all_phones[1], work=all_phones[2], phone2=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work, mobile=mobile, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile,
                       phone2=phone2)