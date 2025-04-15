from pages.homepage import HomePage
from pages.contact_page import ContactPage

def test_valid_contact_form(driver):
    home = HomePage(driver)
    home.load()

    contact = ContactPage(driver)
    contact.open_contact()
    contact.fill_contact_form("Siddharth", "test@example.com", "Test", "This is a test message.")
    contact.submit()
    assert contact.is_success_message()

def test_invalid_contact_form(driver):
    home = HomePage(driver)
    home.load()

    contact = ContactPage(driver)
    contact.open_contact()
    contact.fill_contact_form("", "wrong-email", "", "")
    contact.submit()
    assert contact.has_errors()
