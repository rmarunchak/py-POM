"""
This module contains pytest fixtures for setting up and tearing down test prerequisites.
"""

import pytest
import allure
import logging
import os
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from utils.url_utils import generate_base_url
from pages.conftest import home_page, get_started_page, health_equity_page, account_info_page, confirm_page

load_dotenv()

try:
    import pytest_selenium
    from pytest_selenium import pytest_configure
except ImportError:
    pytest_selenium = None  # Set pytest_selenium to None if the import fails
    pytest_selenium_available = False
else:
    pytest_selenium_available = True

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pytest_addoption(parser):
    """Add browser, capabilities, and headless options to pytest command-line."""
    default_browser = os.environ.get('DEFAULT_BROWSER', 'chrome')
    parser.addoption(
        "--browser",
        action="store",
        default=default_browser,
        choices=["chrome", "firefox"],
        help="Specify browser to use: chrome or firefox"
    )
    parser.addoption(
        "--capabilities",
        action="store",
        default={},
        help="Specify browser capabilities as a dictionary"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def base_url():
    return generate_base_url(service_type='application')


@pytest.fixture(scope="function")
def driver(request, base_url):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    logging.info(f"Initializing {browser_name} browser in {'headless' if headless else 'headed'} mode.")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        driver_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)
        logging.info("Chrome browser started successfully.")
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        if headless:
            firefox_options.add_argument("--headless")
        driver_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=driver_service, options=firefox_options)
        logging.info("Firefox browser started successfully.")
    else:
        logging.error(f"Unsupported browser: {browser_name}")
        raise ValueError(f"Unsupported browser: {browser_name}")

    # Navigate to the base URL after initializing the browser
    print(f"Base URL: {base_url}")
    driver.get(base_url)

    yield driver

    logging.info(f"Closing {browser_name} browser.")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_exception_interact(node, call, report):
    """
    Capture screenshot and attach to Allure report when a test fails.
    """
    yield  # This line makes the function a generator

    if report.failed:
        driver = node.funcargs.get('driver')
        if driver:
            # Define the directory where screenshots will be saved
            screenshot_dir = "/Users/rmaru/PycharmProjects/pythonProject/utils/screenshots"
            screenshot_name = f"{node.name}_screenshot.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)

            # Create the directory if it doesn't exist
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            # Capture the screenshot and save it to the specified directory
            driver.save_screenshot(screenshot_path)

            # Attach the saved screenshot to the Allure report
            allure.attach.file(screenshot_path, name=screenshot_name, attachment_type=allure.attachment_type.PNG)


if pytest_selenium_available:
    @pytest.hookimpl(tryfirst=True)
    def pytest_configure(config):
        # Add the missing attribute
        if not hasattr(config, '_variables'):
            config._variables = {}

        # Your existing logic
        if hasattr(config, 'getoption'):
            capabilities = config.getoption("capabilities", {})
            config._capabilities = capabilities


    # Workaround 2: Bypass the problematic function
    def bypass_function(*args, **kwargs):
        pass


    pytest_selenium.pytest_configure = bypass_function
