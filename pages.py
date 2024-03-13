import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



    # проверка для подтверждения перехода к странице "Начинки"
class TestStellarburgersPages:
    def test_navigation_stuffings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.STUFFINGS_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Protostomia')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Protostomia')]").is_displayed()

    # проверка для подтверждения перехода к странице "Булки"
    def test_navigation_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.BUNS_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Флюоресцентная')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Флюоресцентная')]").is_displayed()

    # проверка для подтверждения перехода к странице "Соусы"
    def test_navigation_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.SAUCE_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Space Sauce')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Space Sauce')]").is_displayed()



