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
        username_field = self.find_element(self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find_element(self.password_input)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.find_element(self.login_button).click()

    def get_welcome_text(self):
        return self.find_element(self.welcome_text).text
