from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_address_input = (By.XPATH, "//input[@id = 'resident_address_line1']")
    second_address_input = (By.XPATH, "//input[@id = 'resident_address_line2']")
    city_input = (By.XPATH, "//input[@id = 'resident_city']")
    zipcode_input = (By.XPATH, "//input[@id = 'resident_zipcode']")
    preferred_phone_input = (By.XPATH, "//input[@name = 'primaryphonenumber.number']")
    state_dropdown = (By.XPATH, "//select[@id = 'resident_state']")
    first_available_state = (By.XPATH, "//select[@id = 'resident_state']/option[2]")
    username_input = (By.XPATH, "//input[@id = 'username']")
    password_input = (By.XPATH, "//input[@id = 'password']")
    password_confirmation_input = (By.XPATH, "//input[@id = 'password_confirmation']")
    first_sec_question_dropdown = (By.XPATH, "//select[@id = 'security_question_id_1']")
    first_sec_question_buttons = (By.XPATH, "//select[@id = 'security_question_id_1']/option")
    second_sec_question_dropdown = (By.XPATH, "//select[@id = 'security_question_id_2']")
    second_sec_question_buttons = (By.XPATH, "//select[@id = 'security_question_id_2']/option")
    third_sec_question_dropdown = (By.XPATH, "//select[@id = 'security_question_id_3']")
    third_sec_question_buttons = (By.XPATH, "//select[@id = 'security_question_id_3']/option")
    fourth_sec_question_dropdown = (By.XPATH, "//select[@id = 'security_question_id_4']")
    fifth_sec_question_dropdown = (By.XPATH, "//select[@id = 'security_question_id_5']")
    sixth_sec_question_dropdown = (By.XPATH, "//select[@id = 'security_question_id_6']")
    first_sec_answer_input = (By.XPATH, "//input[@id = 'security_question_response_1']")
    second_sec_answer_input = (By.XPATH, "//input[@id = 'security_question_response_2']")
    third_sec_answer_input = (By.XPATH, "//input[@id = 'security_question_response_3']")
    fourth_sec_answer_input = (By.XPATH, "//input[@id = 'security_question_response_4']")
    fifth_sec_answer_input = (By.XPATH, "//input[@id = 'security_question_response_5']")
    sixth_sec_answer_input = (By.XPATH, "//input[@id = 'security_question_response_6']")
    card_type_dropdown = (By.XPATH, "//select[@id = 'billing_card_type']")
    first_available_card = (By.XPATH, "//select[@id='billing_card_type']/option[2]")
    card_number_input = (By.XPATH, "//input[@id = 'billing_card_number']")
    card_exp_month_dropdown = (By.XPATH, "//select[@id = 'billing_expiration_month']")
    card_exp_year_dropdown = (By.XPATH, "//select[@id = 'billing_expiration_year']")
    same_as_home_address_checkbox = (By.XPATH, "//input[@id='billing_same_as_physical']")
    learn_about_teladoc_dropdown = (By.CSS_SELECTOR, '#hear-about-us-question')
    learn_about_us_input = (By.XPATH, "//input[@id = 'hear-about-us-question']")
    preferred_language_dropdown = (By.CSS_SELECTOR, '#language')
    language_input = (By.XPATH, "//input[@id='other_language']")
    notice_of_privacy_practices_checkbox = (By.XPATH, "//input[@name = 'agreement']")
    create_account_button = (By.XPATH, "//button[@id = 'submit']")
    complete_registration_button = (By.XPATH, "//button[@id = 'submit']")
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

    def put_first_address(self, address):
        self.enter_text(self.first_address_input, address)

    def put_second_address(self, address):
        self.enter_text(self.second_address_input, address)

    def put_city(self, city):
        self.enter_text(self.city_input, city)

    def put_zipcode(self, zipcode):
        self.enter_text(self.zipcode_input, zipcode)

    def put_preferred_phone(self, phone):
        self.enter_text(self.preferred_phone_input, phone)

    def select_state(self, state):
        self.select_dropdown_by_text(self.state_dropdown, state)

    def put_username(self, username):
        self.enter_text(self.username_input, username)

    def put_password(self, password):
        self.enter_text(self.password_input, password)
        self.enter_text(self.password_confirmation_input, password)

    def select_first_security_question(self, question):
        self.select_dropdown_by_text(self.first_sec_question_dropdown, question)

    def put_first_security_answer(self, answer):
        self.enter_text(self.first_sec_answer_input, answer)

    def click_create_account(self):
        self.click(self.create_account_button)

    def click_complete_registration(self):
        self.click(self.complete_registration_button)
