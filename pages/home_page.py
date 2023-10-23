from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locked_account_error = (By.XPATH, '//p[@class="titlea4773"]')
    invalid_login_error = (By.XPATH, '//p[@class="descriptiona5e8a"]')
    username_input = (By.CSS_SELECTOR, '#login_username')
    password_input = (By.CSS_SELECTOR, '#login_password')
    login_button = (By.XPATH, "//*[@value='Sign in']")
    forgot_username_link = (By.XPATH, '//a[@href="/forgot_username"]')
    forgot_password_link = (By.XPATH, '(//a[@href="/forgot_password"])[1]')
    login_button_alternate = (By.XPATH, "//button[@value='Sign in']")
    get_started_button = (By.XPATH, '//button[contains(@class, "createNewAccountButton")]')
    terminated_benefit_message_text_field = (By.CSS_SELECTOR, '.titlea4773')
    account_exits_error = (By.XPATH, "//h2[contains(@class,'title')]")
    welcome_text = (By.TAG_NAME, 'h1')  # abstract locator

    def enter_username(self, username):
        self.enter_text(self.username_input, username)

    def enter_password(self, password):
        self.enter_text(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def click_get_started_button(self):
        self.click(self.get_started_button)

    def get_welcome_text(self):
        return self.get_text(self.welcome_text)
