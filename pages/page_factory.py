from factory import Factory
from pages.home_page import HomePage
from pages.get_started_page import GetStartedPage
from pages.health_equity_page import HealthEquityPage
from pages.account_info_page import AccountInfoPage
from pages.confirm_page import ConfirmPage


class HomePageFactory(Factory):
    class Meta:
        model = HomePage

    driver = None


class GetStartedPageFactory(Factory):
    class Meta:
        model = GetStartedPage

    driver = None


class HealthEquityPageFactory(Factory):
    class Meta:
        model = HealthEquityPage

    driver = None


class AccountInfoPageFactory(Factory):
    class Meta:
        model = AccountInfoPage

    driver = None


class ConfirmPageFactory(Factory):
    class Meta:
        model = ConfirmPage

    driver = None
