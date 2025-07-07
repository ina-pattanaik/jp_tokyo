# tests/test_demoblaze.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.demoblaze_pages import DemoblazePage
from utils.helpers import generate_username
from utils.config import TestConfig

config = TestConfig()

@pytest.fixture(scope="class")
def driver(request):
    browser = request.config.getoption("browser").lower()
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        drv = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        drv = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.fixture(scope="class", autouse=True)
def setup_class(request, driver):
    request.cls.driver = driver
    request.cls.demoblaze = DemoblazePage(driver)
    request.cls.username = generate_username()
    request.cls.password = "TestPassword123"
    request.cls.config = config
    request.cls.added_products = []

@pytest.mark.usefixtures("setup_class")
class TestDemoblaze:

    def test_signup(self):
        self.demoblaze.signup(self.config.url, self.username, self.password)

    def test_login(self):
        self.demoblaze.login(self.username, self.password)

    def test_add_products_to_cart(self):
        self.demoblaze.add_products_to_cart(self.config.num_products_to_add, self.added_products)

    def test_verify_cart(self):
        self.demoblaze.go_to_cart()
        cart_product_names = self.demoblaze.get_cart_products()
        print(f"Products in cart ({self.driver.name}):", cart_product_names)
        assert len(cart_product_names) >= self.config.num_products_to_add

    def test_delete_one_product(self):
        self.demoblaze.delete_one_product()
        cart_product_names = self.demoblaze.get_cart_products()
        print(f"Products in cart after deletion ({self.driver.name}):", cart_product_names)
        assert len(cart_product_names) >= (self.config.num_products_to_add - 1)

    def test_login_wrong_username(self):
        alert_text = self.demoblaze.login_negative(self.config.url, "wronguser", self.password)
        assert "User does not exist" in alert_text or "Wrong password" in alert_text

    def test_login_wrong_password(self):
        alert_text = self.demoblaze.login_negative(self.config.url, self.username, "wrongpassword")
        assert "Wrong password" in alert_text

    def test_login_wrong_username_and_password(self):
        alert_text = self.demoblaze.login_negative(self.config.url, "wronguser", "wrongpassword")
        assert "User does not exist" in alert_text or "Wrong password" in alert_text

    def test_signup_only_username(self):
        alert_text = self.demoblaze.signup_negative(self.config.url, "useronly", "")
        assert "Please fill out Username and Password." in alert_text

    def test_signup_only_password(self):
        alert_text = self.demoblaze.signup_negative(self.config.url, "", "passwordonly")
        assert "Please fill out Username and Password." in alert_text

