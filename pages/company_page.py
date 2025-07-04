from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CompanyPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verifyCompanyCreation(self, companyName, email, phone, address, industry, companyType, country, province, city, district):
        #object verify company
        self.menu_companies = (By.XPATH, "//a[text()='Companies']")
        self.button_goToCompany = (By.XPATH, f"//div[text()='{companyName}']/parent::div/following-sibling::div//button[text()='Manage']")
        self.vCompName = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.vEmail = (By.XPATH, "//input[@placeholder='Input Email']")
        self.vPhone = (By.XPATH, "//input[@placeholder='Input Mobile Number']")
        self.vIndustryType = (By.XPATH, "//span[text()='Industry Type']/following-sibling::button/span")
        self.vCompanyType = (By.XPATH, "//span[text()='Company Type']/following-sibling::button/span")
        self.vStreetAddress = (By.XPATH, "//span[text()='Company Address']/following-sibling::textarea")
        self.vCountry = (By.XPATH, "//span[text()='Country']/following-sibling::button/span")
        self.vProvince = (By.XPATH, "//span[text()='Province']/following-sibling::button/span")
        self.vCity = (By.XPATH, "//span[text()='City']/following-sibling::button/span")
        self.vDistrict = (By.XPATH, "//span[text()='District']/following-sibling::button/span")


        self.wait.until(EC.element_to_be_clickable(self.menu_companies)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_goToCompany)).click()
        assert companyName == self.wait.until(EC.visibility_of_element_located(self.vCompName)).get_attribute("value")
        assert email == self.wait.until(EC.visibility_of_element_located(self.vEmail)).get_attribute("value")
        assert phone == self.wait.until(EC.visibility_of_element_located(self.vPhone)).get_attribute("value")
        assert address == self.wait.until(EC.visibility_of_element_located(self.vStreetAddress)).get_attribute("value")
        assert industry == self.wait.until(EC.visibility_of_element_located(self.vIndustryType)).text
        assert companyType == self.wait.until(EC.visibility_of_element_located(self.vCompanyType)).text
        assert country == self.wait.until(EC.visibility_of_element_located(self.vCountry)).text
        assert province == self.wait.until(EC.visibility_of_element_located(self.vProvince)).text
        assert city == self.wait.until(EC.visibility_of_element_located(self.vCity)).text
        assert district == self.wait.until(EC.visibility_of_element_located(self.vDistrict)).text
        time.sleep(5)

