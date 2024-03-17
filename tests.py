import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarburgersLocators
from data import TestData
from faker import Faker

fake = Faker()

class TestStellarburgersAccount:

    # переход по клику на «Личный кабинет»
    def test_navigation_to_personal_account(self, driver):
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).click()
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
        driver.find_element(*StellarburgersLocators.ORDER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*StellarburgersLocators.HISTORY_LINK)
        assert driver.find_element(*StellarburgersLocators.HISTORY_LINK).is_displayed(), "Login failed"


    # переход по клику на «Конструктор»

    def test_navigation_to_constructor(self, driver):
        driver.find_element(*StellarburgersLocators.PROTOSTOMIA_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(StellarburgersLocators.ORDER_BUTTON))
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
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*StellarburgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarburgersLocators.ORDER_BUTTON)
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

  # проверка для подтверждения перехода к странице "Начинки"
class TestStellarburgersPages:
    def test_navigation_stuffings(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.STUFFINGS_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*StellarburgersLocators.PROTOSTOMIA_BUTTON))
        assert driver.find_element(*StellarburgersLocators.PROTOSTOMIA_BUTTON).is_displayed()

    # проверка для подтверждения перехода к странице "Булки"
    def test_navigation_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.BUNS_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*StellarburgersLocators.FLUORESCENT_BUN_BUTTON))
        assert driver.find_element(*StellarburgersLocators.FLUORESCENT_BUN_BUTTON).is_displayed()

    # проверка для подтверждения перехода к странице "Соусы"
    def test_navigation_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.SAUCE_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*StellarburgersLocators.SPACE_SAUCE_BUTTON))
        assert driver.find_element(*StellarburgersLocators.SPACE_SAUCE_BUTTON).is_displayed()



class TestStellarburgersLogin:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_main_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert driver.find_element(*StellarburgersLocators.ORDER_BUTTON).is_displayed(), "Login failed"

    # Вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.PASSWORD_INPUT).send_keys(TestData.password)
        driver.find_element(*StellarburgersLocators.SUCCESS_LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
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
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert driver.find_element(*StellarburgersLocators.ORDER_BUTTON).is_displayed(), "Registration form not displayed"

    # Вход через кнопку в форме восстановления пароля
    def test_login_password_recovery_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()
        driver.find_element(*StellarburgersLocators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*StellarburgersLocators.EMAIL_INPUT).send_keys(TestData.email)
        driver.find_element(*StellarburgersLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Сохранить')]")))
        assert driver.find_element(*StellarburgersLocators.SAVE_BUTTON).is_displayed(), "Password recovery form not displayed"
