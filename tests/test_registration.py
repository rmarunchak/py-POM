import time
from data.factories.member_factory import MemberFactory
import pytest
import allure
from data.constants import Constants


@allure.title("Test Registration Functionality")
@allure.description("This test case verifies the registration functionality.")
@pytest.mark.nondestructive
def test_registration(home_page, get_started_page, health_equity_page, account_info_page):
    member = MemberFactory()

    home_page.click_get_started_button()
    get_started_page.enter_first_name(member['first_name'])
    get_started_page.enter_last_name(member['last_name'])
    get_started_page.enter_dob_month(member['dob'].strftime('%m'))
    get_started_page.enter_dob_day(member['dob'].strftime('%d'))
    get_started_page.enter_dob_year(member['dob'].strftime('%Y'))
    get_started_page.enter_zip_code(member['addresses'][0]['postal'])
    get_started_page.enter_email(member['email_address'])
    get_started_page.click_promo_code_checkbox()
    get_started_page.enter_promo_code(Constants.constants['promo_code'])
    get_started_page.click_continue()
    health_equity_page.select_random_gender()
    health_equity_page.select_random_ethnicity()
    health_equity_page.select_random_race()
    health_equity_page.click_next()
    account_info_page.put_username(member['username'])
