from pages.homepage import HomePage
from pages.search_page import SearchPage

def test_valid_search(driver):
    home = HomePage(driver)
    home.load()
    home.click_search_icon()

    search = SearchPage(driver)
    search.search("cloud")
    assert search.result_exists("cloud")

def test_invalid_search(driver):
    home = HomePage(driver)
    home.load()
    home.click_search_icon()

    search = SearchPage(driver)
    search.search("invalidterm123")
    assert search.is_no_result_shown()
