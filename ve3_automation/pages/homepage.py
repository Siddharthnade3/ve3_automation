from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://www.ve3.global/"
    SEARCH_ICON = (By.CLASS_NAME, "ast-search-menu-icon")

    def load(self):
        self.open(self.URL)

    def click_search_icon(self):
        self.click(self.SEARCH_ICON)
