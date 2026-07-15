import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 60)

        self.delay_input: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self.result_field: tuple[str, str] = (By.CSS_SELECTOR, "#result")

    @allure.step("Установить задержку калькулятора: {seconds} сек.")
    def set_delay(self, seconds: int) -> None:
        element = self.wait.until(
            EC.visibility_of_element_located(self.delay_input))
        element.clear()
        element.send_keys(str(seconds))

    @allure.step("Нажать на кнопку калькулятора с текстом: '{label}'")
    def click_button(self, label: str) -> None:
        locator: tuple[str, str] = (
            By.XPATH,
            f"//button[normalize-space()='{label}']",
        )
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(locator))
        button.click()

    @allure.step("Получить текущий результат на табло")
    def get_result(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.result_field))
        return element.text
