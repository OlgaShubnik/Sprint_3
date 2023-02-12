from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TestRegistration:
    def test_registration_success(self, user):
        driver = user.driver
        user.generate()
        user.register()
        WebDriverWait(driver, 3).until(expected_conditions.url_contains('/login'))
        driver.quit()

    def test_registration_error(self, user):
        driver = user.driver
        user.generate()
        user.password = "123"
        user.register()

        WebDriverWait(driver, 3).until(expected_conditions.url_contains('/register'))

        # Проверь, что появилась ошибка
        element = driver.find_element(By.XPATH, "//p[contains(@class, 'input__error')]")
        assert 'Некорректный пароль' in element.text

        driver.quit()
