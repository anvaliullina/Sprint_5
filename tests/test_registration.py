
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_email, generate_password
from locators import (
    REGISTRATION_NAME,
    REGISTRATION_EMAIL,
    REGISTRATION_PASSWORD,
    REGISTRATION_BUTTON,
    REGISTRATION_PASSWORD_ERROR,
)


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 15)

        # Заполняем форму регистрации
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(generate_email())
        driver.find_element(*REGISTRATION_PASSWORD).send_keys(generate_password())
        driver.find_element(*REGISTRATION_BUTTON).click()

        # Проверяем успешную регистрацию
        wait.until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")

    def test_registration_with_invalid_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 15)

        # Вводим некорректный пароль
        wait.until(EC.visibility_of_element_located(REGISTRATION_NAME)).send_keys("Анна")
        driver.find_element(*REGISTRATION_EMAIL).send_keys(generate_email())
        driver.find_element(*REGISTRATION_PASSWORD).send_keys("12345")
        driver.find_element(*REGISTRATION_BUTTON).click()

        # Проверяем сообщение об ошибке
        error = wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_ERROR))
        assert error.text == "Некорректный пароль"
        assert "/register" in driver.current_url
