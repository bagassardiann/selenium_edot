from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:

    

    def __init__(self, driver, email, phone, address, branch, industry, company, language, country, province, city, district, subDistrict, postalCode):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        #object create company
        self.menu_companies = (By.XPATH, "//a[text()='Companies']")
        self.button_addCompany = (By.XPATH, "//button[contains(text(), 'View Company Structure')]/following-sibling::button")
        self.field_compName = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.field_email = (By.XPATH, "//input[@placeholder='Input Email']")
        self.field_phone = (By.XPATH, "//input[@placeholder='Input Phone']")
        
        email="sagabnaidra@gmail.com"
        phone="89600000081"
        address="Jl Mangga Harum Manis"
        branch="Kantor Pusat"
        industry="Education"
        company="Marketplace"
        language="Indonesia"
        country="Indonesia"
        province="JAMBI"
        city="KAB MERANGIN"
        district="BANGKO"
        subDistrict="SUNGAI KAPAS"
        postalCode=""
        
        self.button_industryType = (By.XPATH, "//button/span[text()='Choose Industry Type']")
        self.choose_industryType = (By.XPATH, f"//div/span[text()='{industry}']")

        self.button_companyType = (By.XPATH, "//button/span[text()='Choose Company Type']")
        self.choose_companyType = (By.XPATH, f"//div/span[text()='{company}']")

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
        
        self.choose_postalCode = (By.XPATH, "//span[text()='Postal Code']/following-sibling::button//span")
        self.button_next = (By.XPATH, "//button[text()='Next']")
        self.field_branch = (By.XPATH, "//input[@placeholder='Input Branch Name']")
        self.button_fillSameCompany = (By.XPATH, "//button[text()='Fill in with the same data from the Company records']")
        self.button_cbAgreement = (By.XPATH, "//button[@id='select-all']")
        self.button_register = (By.XPATH, "//button[text()='Register']")
        self.text_company = (By.XPATH, "/html/body/div/main/div/div[1]/span")

        #object verify company
        self.menu_vCompanies = (By.XPATH, "//a[text()='Companies']")
        self.button_vAddCompany = (By.XPATH, "//button[contains(text(), 'View Company Structure')]/following-sibling::button")
        self.field_vCompName = (By.XPATH, "//input[@placeholder='Input Company Name']")
        self.field_vEmail = (By.XPATH, "//input[@placeholder='Input Email']")
        self.field_vPhone = (By.XPATH, "//input[@placeholder='Input Mobile Number']")
        self.button_vIndustryType = (By.XPATH, "//button/span[text()='Choose Industry Type']")
        self.choose_vIndustryType = (By.XPATH, "//div/span[text()='Education']")
        self.button_vCompanyType = (By.XPATH, "//button/span[text()='Choose Company Type']")
        self.choose_vCompanyType = (By.XPATH, "//div/span[text()='Marketplace']")
        self.button_vLanguage = (By.XPATH, "//button/span[text()='Choose Language']")
        self.choose_vLanguage = (By.XPATH, "//div/span[text()='Indonesia']")
        self.field_vStreetAddress = (By.XPATH, "//input[@placeholder='Input Company Address']")
        self.button_vCountry = (By.XPATH, "//button/span[text()='Choose Country']")
        self.choose_vCountry = (By.XPATH, "//div/span[text()='Indonesia']")
        self.button_vProvince = (By.XPATH, "//button/span[text()='Choose Province']")
        self.choose_vProvince = (By.XPATH, "//div/span[text()='JAMBI']")
        self.button_vCity = (By.XPATH, "//button/span[text()='Choose City']")
        self.choose_vCity = (By.XPATH, "//div/span[text()='KAB MERANGIN']")
        self.button_vDistrict = (By.XPATH, "//button/span[text()='Choose District']")
        self.choose_vDistrict = (By.XPATH, "//div/span[text()='BANGKO']")
        self.button_vSubDistrict = (By.XPATH, "//button/span[text()='Choose Sub District']")
        self.choose_vSubDistrict = (By.XPATH, "//div/span[text()='SUNGAI KAPAS']")
        self.button_vNext = (By.XPATH, "//button[text()='Next']")
        self.field_vBranch = (By.XPATH, "//input[@placeholder='Input Branch Name']")
        self.button_vFillSameCompany = (By.XPATH, "//button[text()='Fill in with the same data from the Company records']")
        self.button_vCbAgreement = (By.XPATH, "//button[@id='select-all']")
        self.button_vRegister = (By.XPATH, "//button[text()='Register']")
        self.text_vCompany = (By.XPATH, "/html/body/div/main/div/div[1]/span")
        

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

    def createCompany(self):
        # Klik menu "Companies"
        self.wait.until(EC.element_to_be_clickable(self.menu_companies)).click()

        # Klik tombol "Add Company" (following-sibling dari "View Company Structure")
        self.wait.until(EC.element_to_be_clickable(self.button_addCompany)).click()

        # Isi Company Name
        self.wait.until(EC.visibility_of_element_located(self.field_compName)).send_keys("Contoh Perusahaan2")

        # Isi Email
        self.wait.until(EC.visibility_of_element_located(self.field_email)).send_keys("contoh@email2.com")

        # Isi Phone
        self.wait.until(EC.visibility_of_element_located(self.field_phone)).send_keys("81234567890")

        # Pilih Industry Type: Education
        self.wait.until(EC.element_to_be_clickable(self.button_industryType)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_industryType)).click()

        # Pilih Company Type: Marketplace
        self.wait.until(EC.element_to_be_clickable(self.button_companyType)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_companyType)).click()

        # Pilih Language: Indonesia
        self.wait.until(EC.element_to_be_clickable(self.button_language)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_language)).click()

        # Isi Street Address
        self.wait.until(EC.visibility_of_element_located(self.field_streetAddress)).send_keys("Jl. Contoh Alamat No. 123")

        # Pilih Country: Indonesia
        self.wait.until(EC.element_to_be_clickable(self.button_country)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_country)).click()

        # Pilih Province: JAMBI
        self.wait.until(EC.element_to_be_clickable(self.button_province)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_province)).click()

        # Pilih City: KAB MERANGIN
        self.wait.until(EC.element_to_be_clickable(self.button_city)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_city)).click()

        # Pilih District: BANGKO
        self.wait.until(EC.element_to_be_clickable(self.button_district)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_district)).click()

        # Pilih Sub District: SUNGAI KAPAS
        self.wait.until(EC.element_to_be_clickable(self.button_subDistrict)).click()
        self.wait.until(EC.element_to_be_clickable(self.choose_subDistrict)).click()

        # Klik tombol Next
        self.wait.until(EC.element_to_be_clickable(self.button_next)).click()

        # Klik tombol Next
        self.wait.until(EC.element_to_be_clickable(self.button_next)).click()

        self.wait.until(EC.visibility_of_element_located(self.field_branch)).send_keys("Pusat")

        self.wait.until(EC.element_to_be_clickable(self.button_fillSameCompany)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_cbAgreement)).click()
        self.wait.until(EC.element_to_be_clickable(self.button_register)).click()
        company_text = self.wait.until(EC.visibility_of_element_located(self.text_company)).text
        assert "My Company" in company_text #assert ke halaman depan, karena success kecepatan dan tidak ke get
        time.sleep(20)
