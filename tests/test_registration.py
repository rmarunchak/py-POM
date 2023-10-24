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
    get_started_page.enter_promo_code(Constants.promo_codes['open_group'])
    get_started_page.click_continue()
    health_equity_page.select_random_gender()
    health_equity_page.select_random_ethnicity()
    health_equity_page.select_random_race()
    health_equity_page.click_next()

    # Account Info Page
    account_info_page.enter_address_details(
        member['addresses'][0]['address_line_1'],
        member['addresses'][0]['address_line_2'],
        member['addresses'][0]['city'],
        member['addresses'][0]['postal']
    )
    account_info_page.enter_user_details(member['username'], member['password'])
    for i in range(3):  # Fill in 3 security questions
        account_info_page.select_random_security_question(i)
        account_info_page.enter_security_answer(i, member['security_questions'][i]['response'])
    account_info_page.enter_card_details(
        member['card_details']['card_type'],
        member['card_details']['card_number'],
        member['card_details']['exp_month'],
        member['card_details']['exp_year']
    )
    account_info_page.tap_same_as_home_address_checkbox()
    account_info_page.put_preferred_phone(member['phone_numbers'][0]['number'])
    account_info_page.tap_notice_of_privacy_practices_checkbox()
    account_info_page.complete_registration(member)
