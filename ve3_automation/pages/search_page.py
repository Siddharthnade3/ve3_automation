from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class SearchPage(BasePage):
    SEARCH_INPUT = (By.CLASS_NAME, "search-field")

    def search(self, term):
        self.type(self.SEARCH_INPUT, term + Keys.RETURN)
        time.sleep(2)

    def result_exists(self, keyword):
        return keyword.lower() in self.driver.page_source.lower()

    def is_no_result_shown(self):
        return "nothing found" in self.driver.page_source.lower()
