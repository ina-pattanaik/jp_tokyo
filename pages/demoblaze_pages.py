from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import wait_till

class DemoblazePage:
    def __init__(self, driver):
        self.driver = driver

    def signup(self, url, username, password):
        self.driver.get(url)
        wait_till(self.driver, EC.element_to_be_clickable((By.ID, "signin2")))
        self.driver.find_element(By.ID, "signin2").click()
        wait_till(self.driver, EC.visibility_of_element_located((By.ID, "sign-username")))
        self.driver.find_element(By.ID, "sign-username").send_keys(username)
        self.driver.find_element(By.ID, "sign-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
        wait_till(self.driver, EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def login(self, username, password):
        wait_till(self.driver, EC.element_to_be_clickable((By.ID, "login2")))
        self.driver.find_element(By.ID, "login2").click()
        wait_till(self.driver, EC.visibility_of_element_located((By.ID, "loginusername")))
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        wait_till(self.driver, EC.visibility_of_element_located((By.ID, "nameofuser")))

    def add_products_to_cart(self, num_products, added_products):
        for i in range(num_products):
            product_links = self.driver.find_elements(By.XPATH, "//a[contains(@class, 'hrefch')]")
            wait_till(self.driver, EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'hrefch')]")))
            product_links[i].click()
            wait_till(self.driver, EC.visibility_of_element_located((By.XPATH, "//h2[@class='name']")))
            product_name = self.driver.find_element(By.XPATH, "//h2[@class='name']").text
            added_products.append(product_name)
            wait_till(self.driver, EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))
            self.driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
            wait_till(self.driver, EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            wait_till(self.driver, EC.element_to_be_clickable((By.ID, "nava")))
            self.driver.find_element(By.ID, "nava").click()
            # Wait for home page to reload before next iteration
            wait_till(self.driver, EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'hrefch')]")))

    def go_to_cart(self):
        wait_till(self.driver, EC.element_to_be_clickable((By.ID, "cartur")))
        self.driver.find_element(By.ID, "cartur").click()
        wait_till(self.driver, EC.visibility_of_element_located((By.XPATH, "//tr/td[2]")))

    def get_cart_products(self):
        cart_items = self.driver.find_elements(By.XPATH, "//tr/td[2]")
        return [item.text for item in cart_items]

    def delete_one_product(self):
        # Wait for at least one delete button to be present
        wait_till(self.driver, EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']")))
        delete_buttons = self.driver.find_elements(By.XPATH, "//a[text()='Delete']")
        if delete_buttons:
            # Get the number of products before deletion
            num_products_before = len(self.driver.find_elements(By.XPATH, "//tr/td[2]"))
            delete_buttons[0].click()
            # Wait until the number of products decreases by 1
            wait_till(self.driver, lambda d: len(d.find_elements(By.XPATH, "//tr/td[2]")) == num_products_before - 1)
   
    # ---------- Negative Scenarios for Sign-in ----------

    def open_login_modal(self, url):
        self.driver.get(url)
        wait_till(self.driver, EC.element_to_be_clickable((By.ID, "login2")))
        self.driver.find_element(By.ID, "login2").click()
        wait_till(self.driver, EC.visibility_of_element_located((By.ID, "loginusername")))

    def login_negative(self, url, username, password):
        self.open_login_modal(url)
        self.driver.find_element(By.ID, "loginusername").clear()
        self.driver.find_element(By.ID, "loginpassword").clear()
        if username:
            self.driver.find_element(By.ID, "loginusername").send_keys(username)
        if password:
            self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        wait_till(self.driver, EC.alert_is_present())
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert_text

    # ---------- Negative Scenarios for Sign-up ----------

    def open_signup_modal(self, url):
        self.driver.get(url)
        wait_till(self.driver, EC.element_to_be_clickable((By.ID, "signin2")))
        self.driver.find_element(By.ID, "signin2").click()
        wait_till(self.driver, EC.visibility_of_element_located((By.ID, "sign-username")))

    def signup_negative(self, url, username, password):
        self.open_signup_modal(url)
        self.driver.find_element(By.ID, "sign-username").clear()
        self.driver.find_element(By.ID, "sign-password").clear()
        if username:
            self.driver.find_element(By.ID, "sign-username").send_keys(username)
        if password:
            self.driver.find_element(By.ID, "sign-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
        wait_till(self.driver, EC.alert_is_present())
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return alert_text
