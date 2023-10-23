from selenium.webdriver.common.by import By
from .base_page import BasePage
import random


class HealthEquityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Elements
    next_button = (By.CSS_SELECTOR, '#continue-registration-button')
    male_gender_radio = (By.CSS_SELECTOR, '#gender-male-sex-radio')
    female_gender_radio = (By.CSS_SELECTOR, '#gender-female-sex-radio')
    other_gender_radio = (By.CSS_SELECTOR, '#gender-other-sex-radio')
    hispanic_ethnicity_radio = (By.CSS_SELECTOR, '#hispanic-ethnicity-radio')
    not_hispanic_ethnicity_radio = (By.CSS_SELECTOR, '#nothispanic-ethnicity-radio')
    prefer_not_share_ethnicity_radio = (By.CSS_SELECTOR, '#prefernottoshare-ethnicity-radio')
    american_indian_race_checkbox = (By.CSS_SELECTOR, '#americanindian-race-checkbox')
    asian_race_checkbox = (By.CSS_SELECTOR, '#asian-race-checkbox')
    black_or_african_american_race_checkbox = (By.CSS_SELECTOR, '#africanamerican-race-checkbox')
    native_hawaiian_race_checkbox = (By.CSS_SELECTOR, '#nativehawaiian-race-checkbox')
    white_race_checkbox = (By.CSS_SELECTOR, '#white-race-checkbox')
    other_race_checkbox = (By.CSS_SELECTOR, '#otherrace-race-checkbox')
    prefer_not_share_race_checkbox = (By.CSS_SELECTOR, '#prefernottoshare-race-checkbox')
    specify_other_race_input = (By.CSS_SELECTOR, '#other-race-text-input')

    # Methods
    def select_random_gender_radio(self):
        gender_radios = [self.male_gender_radio, self.female_gender_radio, self.other_gender_radio]
        random.choice(gender_radios).click()

    def select_random_ethnicity(self):
        ethnicities = [self.hispanic_ethnicity_radio, self.not_hispanic_ethnicity_radio,
                       self.prefer_not_share_ethnicity_radio]
        random.choice(ethnicities).click()

    def select_random_race(self):
        races = [self.american_indian_race_checkbox, self.asian_race_checkbox,
                 self.black_or_african_american_race_checkbox,
                 self.native_hawaiian_race_checkbox, self.white_race_checkbox, self.other_race_checkbox,
                 self.prefer_not_share_race_checkbox]
        random_race = random.choice(races)
        random_race.click()
        if random_race == self.other_race_checkbox:
            self.specify_other_race_input.send_keys("RandomRaceName")  # Replace with your random generation logic

    def select_gender(self, member):
        gender = member.lower() if isinstance(member, str) else member['gender'].lower()
        self.driver.find_element(By.CSS_SELECTOR, f"#gender-{gender}-sex-radio").click()

    def tap_next(self):
        self.next_button.click()
