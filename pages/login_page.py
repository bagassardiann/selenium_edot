from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        #object login
        self.button_useEmailUsername = (By.XPATH, "//button[text()='Use Email or Username']")
        self.field_emailUsername = (By.XPATH, "//input[@name='username']")
        self.button_login = (By.XPATH, "//button[text()='Log In']")
        self.field_password = (By.XPATH, "//input[@name='password']")
        self.text_welcome = (By.XPATH, "/html/body/div/main/div/div[1]/span[1]")


    def load(self):
        self.driver.get("https://esuite.edot.id")

    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self.button_useEmailUsername)).click()
        self.wait.until(EC.visibility_of_element_located(self.field_emailUsername)).send_keys(username)
        self.wait.until(EC.element_to_be_clickable(self.button_login)).click()
        self.wait.until(EC.visibility_of_element_located(self.field_password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.button_login)).click()

        welcome_text = self.wait.until(EC.visibility_of_element_located(self.text_welcome)).text
        assert "Welcome Back," in welcome_text
