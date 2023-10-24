"""
This module contains pytest fixtures for setting up and tearing down test prerequisites.
"""

import pytest
import allure
from pathlib import Path
import logging
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.conftest import home_page, get_started_page, health_equity_page, account_info_page


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pytest_addoption(parser):
    """Add browser option to pytest command-line."""
    default_browser = os.environ.get('DEFAULT_BROWSER', 'chrome')  # Fetch the DEFAULT_BROWSER environment variable,
    # if not set, default to 'chrome'
    parser.addoption(
        "--browser",
        action="store",
        default=default_browser,
        choices=["chrome", "firefox"],
        help="Specify browser to use: chrome or firefox"
    )


@pytest.fixture(scope="session")
def base_url():
    """Retrieve base URL from environment variables."""
    APP_TYPE = os.environ.get('APP_TYPE', 'member')
    TEST_ENV = os.environ.get('TEST_ENV', 'default_value_if_not_set')
    SUBDOMAIN = os.environ.get('SUBDOMAIN', 'default_subdomain')
    CLUSTER = os.environ.get('CLUSTER', 'default_cluster')
    DOMAIN = os.environ.get('DOMAIN', 'teladoc.io')
    return f"https://{APP_TYPE}.{SUBDOMAIN}.{CLUSTER}.{DOMAIN}/"


@pytest.fixture(scope="function")
def driver(request, base_url):
    """
    Returns a WebDriver instance based on the browser type (Chrome or Firefox).
    The browser is closed after the test completes.
    """
    browser_name = request.config.getoption("--browser")
    logging.info(f"Initializing {browser_name} browser.")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)
        logging.info("Chrome browser started successfully.")
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
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