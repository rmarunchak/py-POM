"""Module for the base page object and common methods."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        """Initialize the BasePage object with a driver."""
        self.driver = driver

    def find_element(self, by_locator, timeout=10):
        """Find and return an element by its locator."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            raise TimeoutException(f"Element not found with locator: {by_locator} within {timeout} seconds.")

    def click(self, by_locator):
        """Click on an element by its locator."""
        self.find_element(by_locator).click()

    def enter_text(self, by_locator, text):
        """Enter text into an input field by its locator."""
        self.find_element(by_locator).send_keys(text)

    def get_text(self, by_locator):
        """Get the text of an element by its locator."""
        return self.find_element(by_locator).text

    def capture_screenshot(self, screenshot_name):
        """Capture a screenshot and save it with the given name."""
        self.driver.save_screenshot(screenshot_name)
