import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarburgersLocators
from data import TestData

class TestStellarburgersAccount:

    # переход по клику на «Личный кабинет»
    def test_navigation_to_personal_account(self, driver):
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).click()
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
        driver.find_element(*StellarburgersLocators.ORDER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'История заказов')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'История заказов')]").is_displayed(), "Login failed"


    # переход по клику на «Конструктор»
    def test_navigation_to_constructor(self, driver):
        driver.find_element(*StellarburgersLocators.PROTOSTOMIA_BUTTON).click()
        order_button = driver.find_element(*StellarburgersLocators.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"


    # переход по клику на «Stellar Burgers»
    def test_navigation_to_logo(self, driver):
        driver.find_element(*StellarburgersLocators.STELLARBURGERS_LOGO).click()
        order_button = driver.find_element(*StellarburgersLocators.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"


    # выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_personal_account(self, driver):
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.LOGOUT_BUTTON).click()
        login_button = driver.find_element(*StellarburgersLocators.LOGIN_BUTTON)
        assert login_button.text == "Войти", "Элемент 'Войти' не найден"

