from selenium.webdriver.common.by import By

class StellarburgersLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    NAME_INPUT = (By.XPATH, "//input[@name='имя']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    SUCCESS_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    STUFFINGS_LINK = (By.XPATH, "//a[contains(text(), 'Начинки')]")
    PROTOSTOMIA_BUTTON = (By.XPATH, "//button[contains(text(), 'Protostomia')]")
    BUNS_LINK = (By.XPATH, "//a[contains(text(), 'Булки')]")
    FLUORESCENT_BUN_BUTTON = (By.XPATH, "//button[contains(text(), 'Флюоресцентная')]")
    SAUCE_LINK = (By.XPATH, "//a[contains(text(), 'Соусы')]")
    SPACE_SAUCE_BUTTON = (By.XPATH, "//button[contains(text(), 'Space Sauce')]")
    HISTORY_LINK = (By.XPATH, "//button[contains(text(), 'История заказов')]")
<<<<<<<<< Temporary merge branch 1
=========
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
>>>>>>>>> Temporary merge branch 2
