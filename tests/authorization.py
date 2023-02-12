from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorization:

    def test_login_after_registration(self, user):
        driver = user.driver
        user.generate()
        user.register()
        user.login()

        WebDriverWait(driver, 3).until(expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/'))
        driver.quit()

    def test_login_from_account_enter_button(self, user):
        driver = user.driver
        driver.get("https://stellarburgers.nomoreparties.site")
        # Найди кнопку "Войти в аккаунт" и кликни по ней
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        user.login()

        WebDriverWait(driver, 3).until(expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/'))
        driver.quit()

    def test_login_from_person_area_button(self, user):
        driver = user.driver
        driver.get("https://stellarburgers.nomoreparties.site")
        # Найди кнопку "Личный Кабинет" и кликни по ней
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        user.login()

        WebDriverWait(driver, 3).until(expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/'))
        driver.quit()

    def test_login_from_recovery_button(self, user):
        driver = user.driver
        driver.get("https://stellarburgers.nomoreparties.site")
        # Найди кнопку "Войти в аккаунт" и кликни по ней
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        # Найди ссылку "Восстановить пароль" и кликни по ней
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        # Найди ссылку "Войти" и кликни по ней
        driver.find_element(By.LINK_TEXT, "Войти").click()

        user.login()

        WebDriverWait(driver, 3).until(expected_conditions.url_contains('https://stellarburgers.nomoreparties.site/'))
        driver.quit()
