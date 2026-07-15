from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://saucedemo.com"
        self.wait = WebDriverWait(self.driver, 10)

        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        user_field = self.wait.until(
            EC.visibility_of_element_located(
                self.USERNAME_INPUT))
        user_field.clear()
        user_field.send_keys(username)

        pass_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_INPUT))
        pass_field.clear()
        pass_field.send_keys(password)

        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()
