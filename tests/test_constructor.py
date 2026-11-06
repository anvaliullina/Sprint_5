
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB


class TestConstructor:

    def test_switch_to_buns(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)

        # Сначала выбираем соусы
        wait.until(EC.element_to_be_clickable(SAUCES_TAB)).click()
        wait.until(
            lambda d: "tab_tab_type_current"
            in d.find_element(*SAUCES_TAB).get_attribute("class")
        )

        # Переключаемся обратно на булки
        wait.until(EC.element_to_be_clickable(BUNS_TAB)).click()

        # Проверяем активную вкладку
        assert wait.until(
            lambda d: "tab_tab_type_current"
            in d.find_element(*BUNS_TAB).get_attribute("class")
        )

    def test_switch_to_sauces(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)

        # Выбираем соусы
        wait.until(EC.element_to_be_clickable(SAUCES_TAB)).click()

        assert wait.until(
            lambda d: "tab_tab_type_current"
            in d.find_element(*SAUCES_TAB).get_attribute("class")
        )

    def test_switch_to_fillings(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)

        # Выбираем начинки
        wait.until(EC.element_to_be_clickable(FILLINGS_TAB)).click()

        assert wait.until(
            lambda d: "tab_tab_type_current"
            in d.find_element(*FILLINGS_TAB).get_attribute("class")
        )
