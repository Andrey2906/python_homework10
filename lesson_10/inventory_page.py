import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

        self.CART_BUTTON: tuple[str, str] = (
            By.CLASS_NAME,
            "shopping_cart_link",
        )

    @allure.step(
            "Добавить товар в корзину по ID кнопки: '{product_button_id}'")
    def add_product_to_cart_by_id(self, product_button_id: str) -> None:
        button_locator: tuple[str, str] = (By.ID, product_button_id)
        button: WebElement = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    @allure.step("Перейти в корзину кликом по иконке корзины")
    def go_to_cart(self) -> None:
        cart_btn: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )
        cart_btn.click()
