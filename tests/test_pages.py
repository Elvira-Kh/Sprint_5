from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import StellarburgersLocators


class TestStellarburgersPages:
    # проверка для подтверждения перехода к странице "Начинки"
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


