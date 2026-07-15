import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Калькулятор")
@allure.feature("Арифметические операции")
@allure.story("Сложение чисел с задержкой ответа")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест медленного сложения чисел 7 и 8")
@allure.description(
    "Тест проверяет корректность работы калькулятора при сложении двух чисел "
    "в условиях установленной искусственной задержки выполнения операции."
)
def test_slow_calculator(driver) -> None:
    page = CalculatorPage(driver)
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result()
    with allure.step("Проверить, что итоговый результат равен '15'"):
        assert result == "15", (
            f"Ошибка! Ожидался результат '15', но получено: '{result}'"
        )
