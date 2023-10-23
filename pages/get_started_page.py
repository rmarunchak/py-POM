from selenium.webdriver.common.by import By
from .base_page import BasePage


class GetStartedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Elements
    first_name_input = (By.XPATH, "//input[@id = 'first_name']")
    last_name_input = (By.XPATH, "//input[@id = 'last_name']")
    dob_month_input = (By.XPATH, "//input[@id = 'month']")
    dob_day_input = (By.XPATH, "//input[@id = 'day']")
    dob_year_input = (By.XPATH, "//input[@id = 'year']")
    zip_code_input = (By.XPATH, "//input[@id = 'postal']")
    email_input = (By.XPATH, "//input[@id = 'email_address']")
    promo_code_checkbox = (By.XPATH, "//input[@id = 'has_promo_code']")
    promo_code_input = (By.XPATH, "//input[@id = 'promo_code']")
    continue_button = (By.XPATH, "//button[@id = 'continue-registration-button']//*[.='Next']")
    registration_error = (By.XPATH, "//span[contains(@class,'form--error-message--text')]")
    email_address_error = (By.CSS_SELECTOR, '#error-emailAddress')
    zip_code_error = (By.CSS_SELECTOR, '#error-zipCode')

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name_input, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name_input, last_name)

    def enter_dob_month(self, month):
        self.enter_text(self.dob_month_input, month)

    def enter_dob_day(self, day):
        self.enter_text(self.dob_day_input, day)

    def enter_dob_year(self, year):
        self.enter_text(self.dob_year_input, year)

    def enter_zip_code(self, zip_code):
        self.enter_text(self.zip_code_input, zip_code)

    def enter_email(self, email):
        self.enter_text(self.email_input, email)

    def click_continue(self):
        self.click(self.continue_button)

    def click_promo_code_checkbox(self):
        self.click(self.promo_code_checkbox)

    def enter_promo_code(self, promo_code):
        self.enter_text(self.promo_code_input, promo_code)

    def get_registration_error_message(self):
        return self.get_text(self.registration_error)

    def verify_registration_error(self):
        error_message = "This code isn't valid. Try a new code or clear the checkbox to continue."
        assert self.get_registration_error_message() == error_message, (f"Expected '{error_message}' but"
                                                                        f" got '{self.get_registration_error_message()}'")

    def get_email_address_error(self):
        return self.get_text(self.email_address_error)

    def verify_email_address_error(self):
        error_message = 'Please enter a valid email'
        assert error_message in self.get_email_address_error(), (f"Expected error message to contain '{error_message}' "
                                                                 f"but got '{self.get_email_address_error()}'")

    def get_zip_code_error(self):
        return self.get_text(self.zip_code_error)

    def verify_zip_code_error(self):
        error_message = 'Please enter a valid Zip code in one of the formats: ##### or #####-####'
        assert error_message in self.get_zip_code_error(), (f"Expected error message to contain '{error_message}' but "
                                                            f"got '{self.get_zip_code_error()}'")

