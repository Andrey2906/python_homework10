import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

        self.CHECKOUT_BUTTON: tuple[str, str] = (By.ID, "checkout")
        self.CART_ITEMS: tuple[str, str] = (
            By.CLASS_NAME, "inventory_item_name")

    @allure.step("Получить список названий товаров в корзине")
    def get_item_names(self) -> list[str]:
        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_ITEMS))
        elements: list[WebElement] = self.driver.find_elements(
            *self.CART_ITEMS)
        return [element.text for element in elements]

    @allure.step("Нажать на кнопку перехода к оформлению заказа (Checkout)")
    def click_checkout(self) -> None:
        checkout_btn: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()
