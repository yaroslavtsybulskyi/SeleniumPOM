from selenium.webdriver.common.by import By


class Locators:
    LOCATORS_COOKIEACCEPT = (By.XPATH, '//*[@id="Cks"]/div/ul/li[1]/button')
    SKIP_BUTTON = (By.XPATH, '//*[@id="Intro"]/div[2]/button[2]')
    LEGAL = (By.XPATH, "/html/body/nav/div/ul[2]/li[1]/a")
    COOKIES_REJECT = (By.XPATH, '//*[@id="Cks"]/div/ul/li[2]/button')
    LEARN_MORE = (By.XPATH, '//*[@id="Cks"]/p/a')
    RU_LOCALE = (By.XPATH, "/html/body/nav/div/ul[1]/li[2]/a")
    BURGER = (By.CLASS_NAME, "o-BBurger")
    ABOUT = (By.XPATH, '//*[@id="M"]/div[2]/div/nav/ul[1]/li[2]/a')
