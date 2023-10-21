import pytest


@pytest.mark.nondestructive
def test_open_base_url(driver, base_url):
    """
    Test to open the base URL.
    """
    driver.get(base_url)
    assert driver.current_url == base_url
