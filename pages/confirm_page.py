from selenium.webdriver.common.by import By
from .base_page import BasePage
from utils.base_assert import BaseAssert
import re
import pdb


class ConfirmPage(BasePage, BaseAssert):
    go_to_my_homepage_button = (By.XPATH, "//button/*[text()='Go to my homepage']")
    welcome_message_text_field = (By.XPATH, "//h1[@data-testid='text-welcomeMessage']")

    def verify_first_name(self, member, expected):
        self.verify_object_equals(member['first_nm'], expected, 'First name')

    def verify_last_name(self, member, expected):
        self.verify_object_equals(member['last_nm'], expected, 'Last name')

    def verify_gender(self, member, expected):
        self.verify_object_equals(member['gender_cd'], expected.upper(), 'Gender')

    def verify_username(self, member, expected):
        self.verify_object_equals(member['user_nm'], expected, 'Username')

    def verify_first_name_by_member_object(self, actual, expected):
        self.verify_object_equals(actual['first_nm'], expected['first_name'], 'First name')

    def verify_last_name_by_member_object(self, actual, expected):
        self.verify_object_equals(actual['last_nm'], expected['last_name'], 'Last name')

    def verify_registration_mrn_by_member(self, mrns, member, reg_mrn_name, winner_flag):
        member_id = member['individual_id']
        exact_reg_mrn = [id for id in mrns['instances'] if
                         id['individualId'] == member_id and id['mrnSourceClassificationCd'] == reg_mrn_name.upper()]
        self.verify_object_equals(exact_reg_mrn[0]['mrnSourceClassificationCd'], reg_mrn_name.upper(),
                                  'member_master_mrn_source_classification_cd')
        self.verify_object_equals(exact_reg_mrn[0]['winnerEligibilityFlg'], winner_flag.upper(),
                                  'member_master_mrn_source_classification_cd')

    def tap_go_to_my_homepage(self):
        self.find_element(self.go_to_my_homepage_button).click()

    def verify_welcome_message_text(self, member):
        first_name = member if isinstance(member, str) else member['first_name']
        welcome_message_pattern = r"Good (Morning|Evening|Afternoon), {}".format(first_name)
        actual_message = self.retrieve_welcome_disclaimer_text()

        BaseAssert.verify_object_contains(welcome_message_pattern, actual_message, 'Welcome message')

    def retrieve_welcome_disclaimer_text(self):
        return self.find_element(self.welcome_message_text_field).text
