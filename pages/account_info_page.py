from selenium.webdriver.common.by import By
from .base_page import BasePage
from random import choice


class AccountInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Address Details
    first_address_input = (By.XPATH, "//input[@id = 'resident_address_line1']")
    second_address_input = (By.XPATH, "//input[@id = 'resident_address_line2']")
    city_input = (By.XPATH, "//input[@id = 'resident_city']")
    zipcode_input = (By.XPATH, "//input[@id = 'resident_zipcode']")
    preferred_phone_input = (By.XPATH, "//input[@name = 'primaryPhoneNumber.number']")
    state_dropdown = (By.XPATH, "//select[@id = 'resident_state']")
    first_available_state = (By.XPATH, "//select[@id = 'resident_state']/option[2]")

    # User Details
    username_input = (By.XPATH, "//input[@id = 'username']")
    password_input = (By.XPATH, "//input[@id = 'password']")
    password_confirmation_input = (By.XPATH, "//input[@id = 'password_confirmation']")

    # Security Questions
    sec_question_dropdowns = [
        (By.XPATH, f"//select[@id = 'security_question_id_{i}']") for i in range(1, 7)
    ]
    sec_question_buttons = [
        (By.XPATH, f"//select[@id = 'security_question_id_{i}']/option") for i in range(1, 7)
    ]
    sec_answer_inputs = [
        (By.XPATH, f"//input[@id = 'security_question_response_{i}']") for i in range(1, 7)
    ]

    # Card Details
    card_type_dropdown = (By.XPATH, "//select[@id = 'billing_card_type']")
    first_available_card = (By.XPATH, "//select[@id='billing_card_type']/option[2]")
    card_number_input = (By.XPATH, "//input[@id = 'billing_card_number']")
    card_exp_month_dropdown = (By.XPATH, "//select[@id = 'billing_expiration_month']")
    card_exp_year_dropdown = (By.XPATH, "//select[@id = 'billing_expiration_year']")

    # Other UI elements
    same_as_home_address_checkbox = (By.XPATH, "//input[@id='billing_same_as_physical']")
    learn_about_teladoc_dropdown = (By.CSS_SELECTOR, '#hear-about-us-question')
    learn_about_us_input = (By.XPATH, "//input[@id = 'hear-about-us-question']")
    preferred_language_dropdown = (By.CSS_SELECTOR, '#language')
    language_input = (By.XPATH, "//input[@id='other_language']")
    notice_of_privacy_practices_checkbox = (By.XPATH, "//input[@name = 'agreement']")
    create_account_button = (By.XPATH, "//button[@id = 'submit']")
    complete_registration_button = (By.XPATH, "//button[@id = 'submit']")

    # Authorized Consenters section
    authorized_consenter_first_name_input = (By.XPATH, "//input[@id = 'authorized_consenter_first_name']")
    authorized_consenter_last_name_input = (By.XPATH, "//input[@id = 'authorized_consenter_last_name']")
    authorized_consenter_phone_number_input = (By.XPATH, "//input[@id = 'authorizedconsenter-spnf-spnf-phone-number']")
    email_input = (By.XPATH, "//input[@id = 'email_address']")
    gender_dropdown = (By.XPATH, "//select[@id = 'gender']")
    go_to_my_homepage_button = (By.XPATH, "//button//h3[text()='go to my homepage']")
    terms_of_service_link = (By.XPATH, "//span[@class='custom-checkbox-label']/a[contains(text(), 'terms of service')]")
    non_discrimination_link = (
        By.XPATH, "//span[@class='custom-checkbox-label']/a[contains(text(), 'notice of nondiscrimination')]")
    privacy_practices_link = (
        By.XPATH, "//span[@class='custom-checkbox-label']/a[contains(text(), 'notice of privacy practices')]")

    def enter_address_details(self, address1, address2, city, zipcode):
        self.enter_text(self.first_address_input, address1)
        self.enter_text(self.second_address_input, address2)
        self.enter_text(self.city_input, city)
        self.enter_text(self.zipcode_input, zipcode)

    def put_preferred_phone(self, phone):
        self.enter_text(self.preferred_phone_input, phone)

    def select_state(self, state):
        self.select_dropdown_by_text(self.state_dropdown, state)

    def enter_user_details(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.enter_text(self.password_confirmation_input, password)

    def select_random_security_question(self, index):
        self.click(self.sec_question_dropdowns[index])
        options = self.find_elements(self.sec_question_buttons[index])[1:]
        choice(options).click()

    def enter_security_answer(self, index, answer):
        self.enter_text(self.sec_answer_inputs[index], answer)

    def enter_card_details(self, card_type, card_number, exp_month, exp_year):
        self.select_dropdown_by_text(self.card_type_dropdown, card_type)
        self.enter_text(self.card_number_input, card_number)
        self.select_dropdown_by_text(self.card_exp_month_dropdown, exp_month)
        self.select_dropdown_by_text(self.card_exp_year_dropdown, exp_year)

    def tap_same_as_home_address_checkbox(self):
        self.click(self.same_as_home_address_checkbox)

    def tap_notice_of_privacy_practices_checkbox(self):
        self.click(self.notice_of_privacy_practices_checkbox)

    def tap_terms_of_service_link(self):
        self.click(self.terms_of_service_link)

    def tap_non_discrimination_link(self):
        self.click(self.non_discrimination_link)

    def tap_privacy_practices_link(self):
        self.click(self.privacy_practices_link)

    def click_create_account(self):
        self.click(self.create_account_button)

    def click_complete_registration(self):
        self.click(self.complete_registration_button)

    def complete_registration(self, member):
        """Completes the registration process with the provided member details."""

        fields = {
            self.username_input: member['username'],
            self.password_input: member['password'],
            self.password_confirmation_input: member['password']
        }

        for locator, value in fields.items():
            if not self.get_text(locator):
                self.enter_text(locator, value)

        # Click on the complete registration button
        self.click(self.complete_registration_button)


