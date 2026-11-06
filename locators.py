from selenium.webdriver.common.by import By

REGISTRATION_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле «Имя»
REGISTRATION_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
REGISTRATION_PASSWORD = (By.NAME, "Пароль")  # Поле «Пароль» в форме регистрации
REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
REGISTRATION_PASSWORD_ERROR = (By.CSS_SELECTOR, "p.input__error")  # Ошибка некорректного пароля
MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа на главной странице
LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email на странице входа
LOGIN_PASSWORD = (By.NAME, "Пароль")  # Поле «Пароль» на странице входа
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка подтверждения входа
PERSONAL_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[href='/account']")  # Кнопка «Личный кабинет»
REGISTRATION_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")  # Ссылка «Войти» на странице регистрации

CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")  # Кнопка «Конструктор» в шапке сайта

LOGO_LINK = (By.CSS_SELECTOR, "header a[href='/']")  # Логотип Stellar Burgers для перехода в конструктор

LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из личного кабинета

BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")  # Вкладка «Булки»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")  # Вкладка «Соусы»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")  # Вкладка «Начинки»

ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» на главной странице
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ»