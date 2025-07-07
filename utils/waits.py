from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_till(driver, condition, timeout=10):
    """
    Wait until the given Selenium expected condition is met.
    :param driver: Selenium WebDriver instance
    :param condition: expected_conditions instance
    :param timeout: Maximum wait time in seconds
    :return: The element or True if condition met, raises TimeoutException otherwise
    """
    return WebDriverWait(driver, timeout).until(condition)

