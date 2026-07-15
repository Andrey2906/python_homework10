import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

        self.FIRST_NAME: tuple[str, str] = (By.ID, "first-name")
        self.LAST_NAME: tuple[str, str] = (By.ID, "last-name")
        self.POSTAL_CODE: tuple[str, str] = (By.ID, "postal-code")
        self.CONTINUE_BUTTON: tuple[str, str] = (By.ID, "continue")
        self.TOTAL_LABEL: tuple[str, str] = (
            By.CLASS_NAME, "summary_total_label")

    @allure.step(
        "Заполнить форму оформления заказа ("
        "Имя: '{first_name}', Фамилия: '{last_name}', "
        "Индекс: '{postal_code}')"
    )
    def fill_checkout_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        fn_field: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        fn_field.clear()
        fn_field.send_keys(first_name)

        ln_field: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )
        ln_field.clear()
        ln_field.send_keys(last_name)

        pc_field: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        )
        pc_field.clear()
        pc_field.send_keys(postal_code)

        continue_btn: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_btn.click()

    @allure.step("Получить итоговую стоимость заказа с экрана")
    def get_total_price_text(self) -> str:
        total_element: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return total_element.text
