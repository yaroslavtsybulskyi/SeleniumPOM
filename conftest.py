import pytest
from selenium import webdriver


@pytest.fixture()
def delassus_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://delassus.com/en/")

    yield driver

    driver.quit()
