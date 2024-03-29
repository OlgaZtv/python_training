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

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_home_page()
        # init contact edition
        self.select_contact_by_id(id)
        # click to edit
        wd.find_element_by_xpath("//img[@title='Edit']//parent::a[contains(@href,'id="+id+"')]").click()
        # fill contact form
        self.fill_contact(contact)
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # init contact deletion
        self.select_contact_by_id(id)
        # delete contact by id
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # alert acceptation
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


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
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(id=contact_id, lastname=lastname, firstname=firstname, address=address, all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
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
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, home=home, work=work, mobile=mobile, phone2=phone2,
                        email=email, email2=email2, email3=email3)

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

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("to_group").click()
        for we_group in wd.find_elements_by_xpath("//select[@name='to_group']//option"):
            if we_group.get_attribute("value") == group.id:
                we_group.click()
        wd.find_element_by_name("add").click()
        # return
        self.open_home_page()
        self.contact_cache = None

    def del_from_group(self, contact, group):
        wd = self.app.wd
        # выбрать группу из выпадающего списка
        for we_in_group in wd.find_elements_by_xpath("//select[@name='group']//option"):
            if we_in_group.get_attribute("value") == group.id:
                wd.find_element_by_name("group").click()
                we_in_group.click()
                break
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("remove").click()
        # return
        self.open_home_page()
        self.contact_cache = None


