
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BUNS_TAB, SAUCES_TAB, FILLINGS_TAB


def test_switch_to_buns(driver):
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

    # Проверяем, что вкладка «Булки» активна
    assert wait.until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*BUNS_TAB).get_attribute("class")
    )


def test_switch_to_sauces(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 15)

    # Нажимаем вкладку «Соусы»
    wait.until(EC.element_to_be_clickable(SAUCES_TAB)).click()

    # Проверяем, что вкладка «Соусы» активна
    assert wait.until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*SAUCES_TAB).get_attribute("class")
    )


def test_switch_to_fillings(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    wait = WebDriverWait(driver, 15)

    # Нажимаем вкладку «Начинки»
    wait.until(EC.element_to_be_clickable(FILLINGS_TAB)).click()

    # Проверяем, что вкладка «Начинки» активна
    assert wait.until(
        lambda d: "tab_tab_type_current"
        in d.find_element(*FILLINGS_TAB).get_attribute("class")
    )
