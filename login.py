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

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_main_page(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]").is_displayed(), "Login failed"

    # Вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]").is_displayed(), "Login failed"

    # Вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):
        name = 'Elvira'
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//input[@name='имя']").send_keys(name)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]").is_displayed(), "Registration form not displayed"

    # Вход через кнопку в форме восстановления пароля
    def test_login_password_recovery_form(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Восстановить')]").click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Сохранить')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").is_displayed(), "Password recovery form not displayed"

