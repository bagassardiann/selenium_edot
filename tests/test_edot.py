from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_success(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("it.qa@edot.id", "it.QA2025")

def test_create_company(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(
        browser,
        email="sagabnaidra@gmail.com",
        phone="89600000081",
        address="Jl Mangga Harum Manis",
        branch="Kantor Pusat",
        industry="Teknologi",
        company="Contoh Corp",
        language="Indonesia",
        country="Indonesia",
        province="Jawa Barat",
        city="Bandung",
        district="Sukasari",
        subDistrict="Sarijadi",
        postalCode="40151"
    )
    home_page.load()
    login_page.login("it.qa@edot.id", "it.QA2025")
    home_page.createCompany()