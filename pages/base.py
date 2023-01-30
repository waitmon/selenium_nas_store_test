from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://newartstore.ru/catalog/vinilovye_plastinki/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_url(self):
        return self.driver.get(self.base_url)

    def scroll_to_top(self):
        return self.driver.execute_script('window.scrollTo(0, 0)')

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)
