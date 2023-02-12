import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthorization:

    def test_souses_from_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Найти "Соусы" и кликни по ней
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']")))
        time.sleep(1)

    def test_toppings_from_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Найти "Начинки" и кликни по ней
        driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']")))

        time.sleep(1)

    def test_buns_from_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")
        # Найти "Соусы" и кликни по ней
        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']")))
        time.sleep(1)
        # Найти "Булки" и кликни по ней
        driver.find_element(By.XPATH, "//span[text()='Булки']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']")))

        time.sleep(1)
        driver.quit()
