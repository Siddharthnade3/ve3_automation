from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ContactPage(BasePage):
    CONTACT_LINK = (By.LINK_TEXT, "CONTACT")
    NAME = (By.NAME, "your-name")
    EMAIL = (By.NAME, "your-email")
    SUBJECT = (By.NAME, "your-subject")
    MESSAGE = (By.NAME, "your-message")
    SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
    RESPONSE = (By.CLASS_NAME, "wpcf7-response-output")
    ERROR = (By.CLASS_NAME, "wpcf7-not-valid-tip")

    def open_contact(self):
        self.click(self.CONTACT_LINK)

    def fill_contact_form(self, name, email, subject, message):
        self.type(self.NAME, name)
        self.type(self.EMAIL, email)
        self.type(self.SUBJECT, subject)
        self.type(self.MESSAGE, message)

    def submit(self):
        self.click(self.SUBMIT)
        time.sleep(3)

    def is_success_message(self):
        return "thank" in self.get_text(self.RESPONSE).lower()

    def has_errors(self):
        return self.is_element_visible(self.ERROR)
