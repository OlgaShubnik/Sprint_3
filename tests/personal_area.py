from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorization:

    def test_login_to_personal_area(self, user):
        driver = user.driver
        user.login_to_personal_area()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/account/profile"))
        driver.quit()

    def test_redirect_to_constructor_from_personal_area(self, user):
        driver = user.driver
        user.login_to_personal_area()

        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()

        WebDriverWait(driver, 5).until(expected_conditions.url_matches("https://stellarburgers.nomoreparties.site/"))
        element = driver.find_element(By.XPATH, "//a[contains(@class, 'AppHeader_header__link_active__1IkJo')]")
        assert 'Конструктор' in element.text
        driver.quit()

    def test_redirect_to_logo_from_personal_area(self, user):
        driver = user.driver
        user.login_to_personal_area()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/account/profile"))

        # Найди логотип и кликни по нему
        driver.find_element(By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2").click()

        WebDriverWait(driver, 5).until(expected_conditions.url_matches("https://stellarburgers.nomoreparties.site/"))
        element = driver.find_element(By.XPATH, "//a[contains(@class, 'AppHeader_header__link_active__1IkJo')]")
        assert 'Конструктор' in element.text
        driver.quit()

    def test_exit_from_personal_area(self, user):
        driver = user.driver
        user.login_to_personal_area()
        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/account/profile"))

        driver.find_element(By.XPATH, "//button[text()='Выход']").click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("https://stellarburgers.nomoreparties.site/login"))
        driver.quit()
