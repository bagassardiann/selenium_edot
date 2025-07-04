from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)     

    def createCompany(self, companyName, email, phone, address, branch, industry, companyType, language, country, province, city, district, subDistrict):
        
        #object create company
        self.menu_companies = (By.XPATH, "//a[text()='Companies']")
        self.button_addCompany = (By.XPATH, "//button[contains(text(), 'View Company Structure')]/following-sibling::button")
        self.field_compName = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.field_email = (By.XPATH, "//input[@placeholder='Input Email']")
        self.field_phone = (By.XPATH, "//input[@placeholder='Input Phone']")
        
        self.button_industryType = (By.XPATH, "//button/span[text()='Choose Industry Type']")
        self.choose_industryType = (By.XPATH, f"//div/span[text()='{industry}']")

        self.button_companyType = (By.XPATH, "//button/span[text()='Choose Company Type']")
        self.choose_companyType = (By.XPATH, f"//div/span[text()='{companyType}']")

        self.button_language = (By.XPATH, "//button/span[text()='Choose Language']")
        self.choose_language = (By.XPATH, f"//div/span[text()='{language}']")

        self.field_streetAddress = (By.XPATH, "//input[@placeholder='Input Address']")

        self.button_country = (By.XPATH, "//button/span[text()='Choose Country']")
        self.choose_country = (By.XPATH, f"//div/span[text()='{country}']")

        self.button_province = (By.XPATH, "//button/span[text()='Choose Province']")
        self.choose_province = (By.XPATH, f"//div/span[text()='{province}']")

        self.button_city = (By.XPATH, "//button/span[text()='Choose City']")
        self.choose_city = (By.XPATH, f"//div/span[text()='{city}']")

        self.button_district = (By.XPATH, "//button/span[text()='Choose District']")
        self.choose_district = (By.XPATH, f"//div/span[text()='{district}']")

        self.button_subDistrict = (By.XPATH, "//button/span[text()='Choose Sub District']")
        self.choose_subDistrict = (By.XPATH, f"//div/span[text()='{subDistrict}']")
        
        self.postalCode = (By.XPATH, "//span[text()='Postal Code']/following-sibling::button//span")
        self.button_next = (By.XPATH, "//button[text()='Next']")
        self.field_branch = (By.XPATH, "//input[@placeholder='Input Branch Name']")
        self.button_fillSameCompany = (By.XPATH, "//button[text()='Fill in with the same data from the Company records']")
        self.button_cbAgreement = (By.XPATH, "//button[@id='select-all']")
        self.button_register = (By.XPATH, "//button[text()='Register']")
        self.text_company = (By.XPATH, "/html/body/div/main/div/div[1]/span")
        
        self.wait.until(EC.element_to_be_clickable(self.menu_companies)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_addCompany)).click()
        self.wait.until(EC.visibility_of_element_located(self.field_compName)).send_keys(companyName)
        self.wait.until(EC.visibility_of_element_located(self.field_email)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.field_phone)).send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(self.button_industryType)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_industryType)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_companyType)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_companyType)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_language)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_language)).click()
        self.wait.until(EC.visibility_of_element_located(self.field_streetAddress)).send_keys(address)
        self.wait.until(EC.element_to_be_clickable(self.button_country)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_country)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_province)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_province)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_city)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_city)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_district)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_district)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_subDistrict)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_subDistrict)).click()
        self.postalCode = self.wait.until(EC.visibility_of_element_located(self.postalCode)).text

        self.wait.until(EC.element_to_be_clickable(self.button_next)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_next)).click()

        self.wait.until(EC.visibility_of_element_located(self.field_branch)).send_keys(branch)

        self.wait.until(EC.element_to_be_clickable(self.button_fillSameCompany)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_cbAgreement)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_register)).click()
        
        company_text = self.wait.until(EC.visibility_of_element_located(self.text_company)).text
        assert "My Company" in company_text #assert ke halaman depan, karena success kecepatan dan tidak ke get
        time.sleep(5)
