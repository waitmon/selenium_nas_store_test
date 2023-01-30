from pages.base import Base
from selenium.webdriver.common.by import By


class OrderPageLocators:
    locator_continue_button_item_list = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div/div[1]/div[4]/div["
                                                   "2]/div[3]/div/a")
    locator_continue_button_delivery_region = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div/div[1]/div[5]/div["
                                                         "2]/div[3]/div/a[2]")
    locator_pick_up_point_info = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/form/div/div[1]/div[6]/div[2]/div['
                                            '2]/div[2]/div/div[3]/div')
    locator_continue_button_delivery = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div/div[1]/div[6]/div[2]/div["
                                                  "4]/div/a[2]")
    locator_payment_type = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div/div[1]/div[8]/div[2]/div[2]/div["
                                      "1]/div[2]/div[1]/div")
    locator_continue_button_payment = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div/div[1]/div[8]/div[2]/div["
                                                 "4]/div/a[2]")
    locator_name_field = (By.XPATH, "//input[@name='ORDER_PROP_1']")
    locator_email_field = (By.XPATH, "//input[@name='ORDER_PROP_2']")
    locator_phone_field = (By.XPATH, "//input[@name='ORDER_PROP_3']")


class OrderInfo(Base):

    def click_continue_button_item_list(self):
        return self.find_element(OrderPageLocators.locator_continue_button_item_list).click()

    def click_continue_button_delivery_region(self):
        return self.find_element(OrderPageLocators.locator_continue_button_delivery_region).click()

    def get_pick_up_point_info(self):
        pick_up_point = self.find_element(OrderPageLocators.locator_pick_up_point_info)
        print('Pick up point information:', pick_up_point.text)

    def click_continue_button_delivery(self):
        return self.find_element(OrderPageLocators.locator_continue_button_delivery).click()

    def click_payment_type(self):
        return self.find_element(OrderPageLocators.locator_payment_type).click()

    def click_continue_button_payment(self):
        return self.find_element(OrderPageLocators.locator_continue_button_payment).click()

    def name_input(self, name):
        name_field = self.find_element(OrderPageLocators.locator_name_field)
        name_field.click()
        name_field.send_keys(name)
        print('Name field input')
        return name_field

    def email_input(self, email):
        email_field = self.find_element(OrderPageLocators.locator_email_field)
        email_field.click()
        email_field.send_keys(email)
        print('E-mail field input')
        return email_field

    def phone_input(self, phone):
        phone_field = self.find_element(OrderPageLocators.locator_phone_field)
        phone_field.click()
        phone_field.send_keys(phone)
        print('Phone field input')
        return phone_field
