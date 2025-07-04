from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.company_page import CompanyPage

# Test data for login
username = "it.qa@edot.id"
password = "it.QA2025"


#Test data for createCompany & verifyCompanyCreation
companyName="PT Gaharu Sejahtera 6"
email="gaharu6@gmail.com"
phone="89600000081"
address="Jl Mangga Harum Manis"
branch="Kantor Pusat"
industry="Education"
companyType="Marketplace"
language="Indonesia"
country="Indonesia"
province="JAMBI"
city="KAB MERANGIN"
district="BANGKO"
subDistrict="SUNGAI KAPAS"
postalCode=""

def test_login_success(browser):
    login_page = LoginPage(browser)

    login_page.load()
    login_page.login(username, password)

def test_create_company(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)

    login_page.load()
    login_page.login(username, password)
    home_page.createCompany(companyName, email, phone, address, branch, industry, companyType, language, country, province, city, district, subDistrict)
    global postalCode
    postalCode = home_page.postalCode #untuk verify postalCode di test_verify_data, namun saat ini kosong

def test_verify_data(browser):
    global postalCode
    print("Setelah createCompany, postalCode =", postalCode)
    login_page = LoginPage(browser)
    company_page = CompanyPage(browser)

    login_page.load()
    login_page.login(username, password)
    company_page.verifyCompanyCreation(companyName, email, phone, address, industry, companyType, country, province, city, district)