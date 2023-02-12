import pytest
import uuid

from random import randint
from selenium.webdriver.common.by import By
from selenium import webdriver


class User:
    def __init__(self, driver):
        self.email = "olga_shubnik_6_001@ya.ru"
        self.password = "123456"
        self.name = "Ольга"
        self.driver = driver

    def generate(self):
        self.email = "olga_shubnik_6_" + str(uuid.uuid4()) + "@ya.ru"
        self.password = str(randint(100000, 999999))
        self.name = "Ольга"

    def register(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")

        # Найди кнопку "Войти в аккаунт" и кликни по ней
        self.driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()

        # Найди кнопку "Зарегистрироваться" и кликни по ней
        self.driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        # Найди поле "Name" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Имя']/parent::div//input").send_keys(self.name)

        # Найди поле "Email" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Email']/parent::div//input").send_keys(self.email)

        # Найди поле "Пароль" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Пароль']/parent::div//input").send_keys(self.password)

        # Найди кнопку "Зарегистрироваться" и кликни по ней
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        return self

    def login(self):
        # Найди поле "Email" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Email']/parent::div//input").send_keys(self.email)
        # Найди поле "Пароль" и заполни его
        self.driver.find_element(By.XPATH, "//label[text()='Пароль']/parent::div//input").send_keys(self.password)

        # Найди кнопку "Войти" и кликни по ней
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        return self

    def default_login(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Найди кнопку "Войти в аккаунт" и кликни по ней
        self.driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        self.login()

    def login_to_personal_area(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        # Найди кнопку "Личный Кабинет" и кликни по ней
        self.driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        self.login()
        self.driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()


@pytest.fixture
def driver():
    return webdriver.Chrome()


@pytest.fixture
def user(driver):
    return User(driver)

