from pages.homepage import HomePage

def test_homepage_load(driver):
    home = HomePage(driver)
    home.load()
    assert "VE3" in driver.title
