
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import (    
    REGISTRATION_NAME,
    REGISTRATION_EMAIL,
    REGISTRATION_PASSWORD,
    REGISTRATION_BUTTON,
    MAIN_LOGIN_BUTTON,
    LOGIN_EMAIL,
    LOGIN_PASSWORD,
    LOGIN_BUTTON,
    PERSONAL_ACCOUNT_BUTTON,    REGISTRATION_LOGIN_LINK,
    REGISTRATION_LOGIN_LINK,
    ORDER_BUTTON,
)


class TestLogin:

    def test_login_from_main_page(self, driver):
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Подготавливаем зарегистрированного пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Входим через кнопку на главной странице
        driver.get("https://stellarburgers.education-services.ru/")
        wait.until(EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)).click()
        wait.until(EC.url_contains("/login"))

        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем успешную авторизацию
        order_button = ORDER_BUTTON
        assert wait.until(EC.visibility_of_element_located(order_button)).is_displayed()


    def test_login_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Регистрируем нового пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Переходим к входу через личный кабинет
        driver.get("https://stellarburgers.education-services.ru/")
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/login"))

        # Авторизуемся
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем успешный вход
        order_button = ORDER_BUTTON
        assert wait.until(EC.visibility_of_element_located(order_button)).is_displayed()


    def test_login_from_registration_page(self, driver):
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Создаём пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Переходим на регистрацию и нажимаем ссылку «Войти»
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.element_to_be_clickable(REGISTRATION_LOGIN_LINK)).click()
        wait.until(EC.url_contains("/login"))

        # Авторизуемся
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем успешный вход
        order_button = ORDER_BUTTON
        assert wait.until(EC.visibility_of_element_located(order_button)).is_displayed()



    def test_login_from_password_recovery_page(self, driver):
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Регистрируем нового пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Открываем восстановление пароля и нажимаем «Войти»
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        wait.until(EC.element_to_be_clickable(REGISTRATION_LOGIN_LINK)).click()
        wait.until(EC.url_contains("/login"))

        # Вводим данные пользователя
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        # Проверяем успешный вход
        order_button = ORDER_BUTTON
        assert wait.until(EC.visibility_of_element_located(order_button)).is_displayed()
