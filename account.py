
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarburgers:

    @pytest.fixture(scope='session')
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--window_size=1920,1080')
        driver = webdriver.Chrome(options=options)
        yield driver
        driver.quit()

    # переход по клику на «Личный кабинет»
    def test_navigation_to_personal_account(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'История заказов')]")))
        assert driver.find_element(By.XPATH, "//button[contains(text(), 'История заказов')]").is_displayed(), "Login failed"

    # переход по клику на «Конструктор»
    def test_navigation_to_constructor(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Конструктор')]").click()
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    # переход по клику на «Stellar Burgers»
    def test_navigation_to_logo(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//img[@alt='Stellar Burgers']").click()
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"

    # выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_personal_account(self, driver):
        email = "elvira.filatova2017@yandex.ru"
        password = "toshinyadai"
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()
        order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
        assert order_button.text == "Оформить заказ", "Элемент 'Оформить заказ' не найден"
        driver.find_element(By.XPATH, "//button[contains(text(), 'Личный кабинет')]").click()
        driver.find_element(By.XPATH, "//button[contains(text(), 'Выход')]").click()
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
        assert login_button.text == "Войти", "Элемент 'Войти' не найден"