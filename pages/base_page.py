"""Module for the base page object and common methods."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger.logger_util import setup_logger
from selenium.webdriver.support.ui import Select


LOGGER = setup_logger(__name__)


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        """Initialize the BasePage object with a driver."""
        self.driver = driver

    def find_element(self, by_locator, timeout=10):
        """Find and return an element by its locator."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            LOGGER.info(f"[INFO], [{self.get_current_time()}]: Found element with locator '{by_locator}'")
            return element
        except TimeoutException:
            LOGGER.error(
                f"[ERROR], [{self.get_current_time()}]: Element not found with locator: {by_locator} within {timeout} seconds.")
            raise

    def click(self, by_locator):
        """Click on an element by its locator."""
        self.find_element(by_locator).click()
        LOGGER.info(f"[INFO], [{self.get_current_time()}]: Click on element with locator '{by_locator}'")

    def enter_text(self, by_locator, text):
        """Enter text into an input field by its locator."""
        self.find_element(by_locator).send_keys(text)
        LOGGER.info(
            f"[INFO], [{self.get_current_time()}]: Entered text '{text}' into element with locator '{by_locator}'")

    def get_text(self, by_locator):
        """Get the text of an element by its locator."""
        text = self.find_element(by_locator).text
        LOGGER.info(
            f"[INFO], [{self.get_current_time()}]: Retrieved text '{text}' from element with locator '{by_locator}'")
        return text

    def capture_screenshot(self, screenshot_name):
        """Capture a screenshot and save it with the given name."""
        self.driver.save_screenshot(screenshot_name)
        LOGGER.info(f"[INFO], [{self.get_current_time()}]: Captured screenshot with name '{screenshot_name}'")

    @staticmethod
    def get_current_time():
        """Get the current time in the desired format."""
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')

    def select_dropdown_by_text(self, by_locator, text):
        """Select a dropdown option by its visible text."""
        dropdown = Select(self.find_element(by_locator))
        dropdown.select_by_visible_text(text)

    def find_elements(self, by_locator, timeout=10):
        """Find and return a list of elements by their locator."""
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(by_locator))
            LOGGER.info(f"[INFO], [{self.get_current_time()}]: Found elements with locator '{by_locator}'")
            return elements
        except TimeoutException:
            LOGGER.error(
                f"[ERROR], [{self.get_current_time()}]: Elements not found with locator: {by_locator} within {timeout} seconds.")
            raise

    def wait_until_enabled(self, by_locator, timeout=10):
        """Wait until an element is enabled and clickable."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator))
            LOGGER.info(
                f"[INFO], [{self.get_current_time()}]: Element with locator '{by_locator}' is enabled and clickable")
            return element
        except TimeoutException:
            LOGGER.error(
                f"[ERROR], [{self.get_current_time()}]: Element not enabled with locator: {by_locator} within {timeout} seconds.")
            raise

    def clear_text(self, by_locator):
        """Clear the text of an input field by its locator."""
        self.find_element(by_locator).clear()
        LOGGER.info(f"[INFO], [{self.get_current_time()}]: Cleared text from element with locator '{by_locator}'")

