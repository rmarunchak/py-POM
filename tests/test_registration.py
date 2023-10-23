import time

from pages.get_started_page import GetStartedPage
from data.factories.member_factory import MemberFactory
from pages.home_page import HomePage
import pytest
import allure
from utils.logger.logger_util import setup_logger

# Set up the logger
logger = setup_logger(__name__)


@allure.title("Test Registration Functionality")
@allure.description("This test case verifies the registration functionality.")
@pytest.mark.nondestructive
def test_registration(driver):
    home_page = HomePage(driver)
    registration_page = GetStartedPage(driver)
    member = MemberFactory()

    home_page.click_get_started_button()
    registration_page.enter_first_name(member['first_name'])
    registration_page.enter_last_name(member['last_name'])
    registration_page.enter_dob_month(member['dob'].strftime('%m'))
    registration_page.enter_dob_day(member['dob'].strftime('%d'))
    registration_page.enter_dob_year(member['dob'].strftime('%Y'))
    registration_page.enter_zip_code(member['addresses'][0]['postal'])
    registration_page.enter_email(member['email_address'])

