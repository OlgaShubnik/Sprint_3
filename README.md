1. registration.py #тесты с регистрацией
2. authorization.py #тесты с авторизацией
3. personal_area.py #тесты переход в ЛКб выход из ЛК переход в конструкторы и клик на логотип
4. menu.py #переход между вкладками Соусы, булки, начинки
5. conftest.py #собственно фикстура

Локаторы 

(By.XPATH, "//button[text()='Войти в аккаунт']") Вход в аккаунт 
(By.LINK_TEXT, "Зарегистрироваться")  Кнопка зарегистрироваться
(By.XPATH, "//label[text()='Имя']/parent::div//input") Поле Name
(By.XPATH, "//label[text()='Email']/parent::div//input") Поле Email
(By.XPATH, "//label[text()='Пароль']/parent::div//input") Поле пароль
(By.XPATH, "//button[text()='Зарегистрироваться']") Кнопка зарегистрироваться 
(By.XPATH, "//button[text()='Войти']") Кнопка Войти 
(By.XPATH, "//p[text()='Личный Кабинет']") Кнопка личный кабинет
(By.LINK_TEXT, "Восстановить пароль") Кнопка Восстановить пароль 
(By.XPATH, "//p[contains(@class, 'input__error')]") Сообщение об ошибке
(By.XPATH, "//a[contains(@class, 'AppHeader_header__link_active__1IkJo')]") Кнопка Конструктор 
(By.XPATH, "//button[text()='Выход']" Кнопка Выход 
((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Соусы']"))) раздел Соусы 
((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Начинки']"))) раздел Начинки
((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='Булки']"))) раздел Булки # Sprint_3
