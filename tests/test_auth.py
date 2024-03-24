from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import StellarburgersLocators
from faker import Faker
from Sprint_5.data import TestData

fake = Faker()

class TestStellarburgersAuthentication:

    # Регистрация нового пользователя
    def test_new_user_registration(self, driver):
        email = fake.email()
        password = "fakepassword1234"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.REGISTER_BUTTON).click()
        driver.find_element(*StellarburgersLocators.NAME_INPUT).send_keys(TestData.name)
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*StellarburgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarburgersLocators.SUCCESS_LOGIN_BUTTON))
        assert driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).is_displayed(), "Registration failed"

     # Авторизация с корректным паролем
    def test_authentication_correct(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarburgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarburgersLocators.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    # Авторизация с некорректным паролем
    def test_authentication_incorrect(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarburgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarburgersLocators.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"