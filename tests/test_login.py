from pages.home_page import HomePage
from data.test_data import TestData
import pytest
import allure
from utils.logger.logger_util import setup_logger

# Set up the logger
logger = setup_logger(__name__)


@allure.title("Test Login Functionality")
@allure.description("This test case verifies the login functionality.")
@pytest.mark.nondestructive
def test_login(driver):
    home_page = HomePage(driver)

    home_page.enter_username(TestData.data['login']['username'])
    home_page.enter_password(TestData.data['login']['password'])
    home_page.click_login()

    welcome_text = home_page.get_welcome_text()
    logger.info(f"Retrieved welcome text: {welcome_text}")

    # Assertion to check 'Welcome' text
    assert "Welcome" in welcome_text, f"Expected 'Welcome' in the text, but got '{welcome_text}'"
