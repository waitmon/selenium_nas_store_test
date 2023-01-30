from pages.base import Base
from selenium.webdriver.common.by import By


class CartPageLocators:
    locator_cart_title_artist = (By.CSS_SELECTOR, 'div.author')
    locator_cart_title_record = (By.CSS_SELECTOR, 'td.info.item > div.name > a')
    locator_cart_final_price = (By.CSS_SELECTOR, '#allSum_FORMATED')
    locator_checkout_button = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/section/form/div/div/div/div[2]/div[1]/a[3]')


class CartPage(Base):

    def title_artist_assertion(self):
        artist_title = self.find_element(CartPageLocators.locator_cart_title_artist)
        assert artist_title.text == 'BORIS'
        print('Artist title is:', artist_title.text)

    def title_record_assertion(self):
        record_title = self.find_element(CartPageLocators.locator_cart_title_record)
        assert record_title.text == 'Heavy Rocks'
        print('Record title is:', record_title.text)

    def cart_final_price_assertion(self):
        cart_final_price = self.find_element(CartPageLocators.locator_cart_final_price)
        assert cart_final_price.text == '1 700 руб.'
        print('Final price is:', cart_final_price.text)

    def click_checkout_button(self):
        return self.find_element(CartPageLocators.locator_checkout_button).click()