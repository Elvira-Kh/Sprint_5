import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgers:

    @pytest.fixture(scope='session')
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--window_size=1920,1080')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    # проверка для подтверждения перехода к странице "Начинки"
    def test_navigation_stuffings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//a[contains(text(), 'Начинки')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Protostomia')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Protostomia')]").is_displayed()

    # проверка для подтверждения перехода к странице "Булки"
    def test_navigation_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//a[contains(text(), 'Булки')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Флюоресцентная')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Флюоресцентная')]").is_displayed()

    # проверка для подтверждения перехода к странице "Соусы"
    def test_navigation_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//a[contains(text(), 'Соусы')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Space Sauce')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Space Sauce')]").is_displayed()



