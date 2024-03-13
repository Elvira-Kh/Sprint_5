import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgers:

    @pytest.fixture(scope='session')
    def driver(self):
        driver = webdriver.Chrome(options=options)
        options.add_argument('--window_size=1920,1080')
        yield driver
        driver.quit()

    # Регистрация нового пользователя
    def test_new_user_registration(self, driver):
        name = 'Elvira'
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//input[@name='имя']").send_keys(name)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Вход')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Вход')]").is_displayed(), "Registration failed"

    # Авторизация с корректным паролем
    def test_authentication_correct(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    # Авторизация с некорректным паролем
    def test_authentication_incorrect(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyada1"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
