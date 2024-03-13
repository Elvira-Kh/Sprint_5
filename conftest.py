import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window_size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


