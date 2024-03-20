import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarburgersLocators
from data import TestData


class TestStellarburgersLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*StellarburgersLocators.ORDER_BUTTON)
        assert driver.find_element(*StellarburgersLocators.ORDER_BUTTON).is_displayed(), "Login failed"

    # Вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(*StellarburgersLocators.ORDER_BUTTON)
        assert driver.find_element(*StellarburgersLocators.ORDER_BUTTON).is_displayed(), "Login failed"

    # Вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.REGISTER_BUTTON).click()
        driver.find_element(*StellarburgersLocators.NAME_INPUT).send_keys(TestData.name)
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(*StellarburgersLocators.ORDER_BUTTON)
        assert driver.find_element(
            *StellarburgersLocators.ORDER_BUTTON).is_displayed(), "Registration form not displayed"

    # Вход через кнопку в форме восстановления пароля
    def test_login_password_recovery_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*StellarburgersLocators.SAVE_BUTTON)
        assert driver.find_element(*StellarburgersLocators.SAVE_BUTTON).is_displayed(), "Password recovery form not displayed"
