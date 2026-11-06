
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import (
    REGISTRATION_NAME,
    REGISTRATION_EMAIL,
    REGISTRATION_PASSWORD,
    REGISTRATION_BUTTON,
    LOGIN_EMAIL,
    LOGIN_PASSWORD,
    LOGIN_BUTTON,
    PERSONAL_ACCOUNT_BUTTON,
    CONSTRUCTOR_BUTTON,
    LOGO_LINK,
    LOGOUT_BUTTON,
    LOGO_LINK,
    LOGOUT_BUTTON,
    ORDER_BUTTON,
)

class TestPersonalAccount:
    
    def test_open_personal_account(self, driver):         
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Регистрируем пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Входим в аккаунт
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = ORDER_BUTTON
        wait.until(EC.visibility_of_element_located(order_button))

        # Открываем личный кабинет
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()

        # Проверяем переход в профиль
        wait.until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url



    def test_go_to_constructor_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Регистрируем пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Входим в аккаунт
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = ORDER_BUTTON
        wait.until(EC.visibility_of_element_located(order_button))

        # Открываем личный кабинет
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account/profile"))

        # Возвращаемся в конструктор
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_BUTTON)).click()

        # Проверяем переход на главную страницу
        wait.until(EC.visibility_of_element_located(order_button))
        assert driver.current_url.rstrip("/") == "https://stellarburgers.education-services.ru"


    def test_go_to_constructor_by_logo(self, driver):
        wait = WebDriverWait(driver, 15)
        email = generate_email()
        password = generate_password()

        # Регистрируем пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(email)
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()
        wait.until(EC.url_contains("/login"))

        # Входим в аккаунт
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = ORDER_BUTTON
        wait.until(EC.visibility_of_element_located(order_button))

        # Переходим в личный кабинет
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account/profile"))

        # Нажимаем на логотип Stellar Burgers
        wait.until(EC.element_to_be_clickable(LOGO_LINK)).click()

        # Проверяем переход в конструктор
        wait.until(EC.visibility_of_element_located(order_button))
        assert driver.current_url.rstrip("/") == "https://stellarburgers.education-services.ru"



    def test_logout_from_personal_account(self, driver):
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

        # Входим в аккаунт
        driver.find_element(*LOGIN_EMAIL).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        order_button = ORDER_BUTTON
        wait.until(EC.visibility_of_element_located(order_button))

        # Открываем личный кабинет
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_contains("/account/profile"))

        # Нажимаем кнопку «Выход»
        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

        # Проверяем, что открылась страница входа
        wait.until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")
