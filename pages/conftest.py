import pytest
from .page_factory import HomePageFactory
from .page_factory import GetStartedPageFactory
from .page_factory import HealthEquityPageFactory
from .page_factory import AccountInfoPageFactory


@pytest.fixture(scope="function")
def home_page(driver):
    return HomePageFactory(driver=driver)


@pytest.fixture(scope="function")
def get_started_page(driver):
    return GetStartedPageFactory(driver=driver)


@pytest.fixture(scope="function")
def health_equity_page(driver):
    return HealthEquityPageFactory(driver=driver)


@pytest.fixture(scope="function")
def account_info_page(driver):
    return AccountInfoPageFactory(driver=driver)