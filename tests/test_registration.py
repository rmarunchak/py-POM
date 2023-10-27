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
    account_info_page.put_username(member['username'])
    account_info_page.put_password(member['password'])
    account_info_page.put_first_address(member['addresses'][0]['address_line_1'])
    account_info_page.put_city(member['addresses'][0]['city'])
    account_info_page.select_state(member['addresses'][0]['state'])
    account_info_page.select_random_first_sec_question()
    account_info_page.put_first_security_answer(member['security_questions'][0]['response'])
    account_info_page.select_random_second_sec_question()
    account_info_page.put_second_security_answer(member['security_questions'][1]['response'])
    account_info_page.select_random_third_sec_question()
    account_info_page.put_third_security_answer(member['security_questions'][2]['response'])
    account_info_page.select_card_type(member['card_details']['card_type'])
    account_info_page.put_card_number(member['card_details']['card_number'])
    account_info_page.select_card_exp_month(member['card_details']['exp_month'])
    account_info_page.select_card_exp_year(member['card_details']['exp_year'])
    account_info_page.tap_same_as_home_address_checkbox()
    account_info_page.put_preferred_phone(member['phone_numbers'][0]['number'])
    account_info_page.tap_notice_of_privacy_practices_checkbox()
    account_info_page.complete_registration(member)
    time.sleep(25)
    person_response = account_info_page.retrieve_person_by_username(member['username'])
    assert member['first_name'] == person_response[
        'first_nm'], f"Expected first name {member['first_name']} but got {person_response['first_nm']}"
    assert member['last_name'] == person_response[
        'last_nm'], f"Expected last name {member['last_name']} but got {person_response['last_nm']}"

