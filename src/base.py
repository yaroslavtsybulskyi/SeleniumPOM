from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = f"https://delassus.com/en/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def go_to_site(self):
        self.driver.get(self.base_url)

    def get_page_title(self):
        return self.driver.title

    def execute_script(self, locator):
        return self.driver.execute_script("arguments[0].click();", locator)

    def get_current_page(self):
        return self.driver.current_url
