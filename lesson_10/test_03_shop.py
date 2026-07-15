import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Оформление заказа")
@allure.feature("Покупка товаров")
@allure.story("Сквозной сценарий покупки нескольких товаров")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Успешное оформление покупки трех товаров в Saucedemo")
@allure.description(
    "Тест проверяет полный цикл: "
    "авторизацию, добавление трех товаров в корзину, "
    "заполнение формы доставки и финальную проверку итоговой стоимости заказа."
    )
def test_saucedemo_purchase(driver) -> None:
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    product_buttons = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for button_id in product_buttons:
        inventory_page.add_product_to_cart_by_id(button_id)

    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_form(
        first_name="Тест",
        last_name="Тестов",
        postal_code="12345"
    )

    actual_total = checkout_page.get_total_price_text()

    expected_total = "Total: $58.29"
    with allure.step("Проверить, что итоговая сумма равна '{expected_total}'"):
        assert actual_total == expected_total, (
            f"Ошибка! Ожидали точное совпадение с '{expected_total}', "
            f"но получили '{actual_total}'"
        )
