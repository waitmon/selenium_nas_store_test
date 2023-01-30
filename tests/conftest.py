import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.page_load_strategy = 'eager'
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    yield driver
    driver.quit()