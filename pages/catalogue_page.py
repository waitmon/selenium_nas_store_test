from pages.base import Base
from selenium.webdriver.common.by import By


class NASPageLocators:
    locator_search_field = (By.XPATH, "/html/body/div[1]/header/div[3]/div/div/div[1]/form/input")
    locator_search_button = (By.XPATH, "/html/body/div[1]/header/div[3]/div/div/div[1]/form/button")
    locator_item_1_cart_icon = (By.XPATH, "/html/body/div[1]/div[1]/div/section/div/div[1]/div[1]/div[6]/a")
    locator_catalogue_button = (By.XPATH, "/html/body/div[1]/header/div[3]/div/div/ul/li[1]/a")
    locator_cart_icon = (By.XPATH, "//a[@href='/personal/cart/']")


class CataloguePage(Base):
    def search_input(self, textinput):
        search_field = self.find_element(NASPageLocators.locator_search_field)
        search_field.click()
        search_field.send_keys(textinput)
        print('Searching artist by search field input')
        return search_field

    def click_search_button(self):
        return self.find_element(NASPageLocators.locator_search_button).click()

    def click_search_result_item_1(self):
        return self.find_element(NASPageLocators.locator_item_1_cart_icon).click()

    def click_catalogue_button(self):
        return self.find_element(NASPageLocators.locator_catalogue_button).click()

    def click_cart_icon(self):
        return self.find_element(NASPageLocators.locator_cart_icon).click()


