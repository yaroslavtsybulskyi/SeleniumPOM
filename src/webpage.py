from base import BasePage
from locators import Locators


class WebPageAssistant(BasePage):
    def press_skip_button(self):
        skip_btn = self.find_element(Locators.SKIP_BUTTON)
        return self.execute_script(skip_btn)

    def accept_cookies(self):
        cookies = self.find_element(Locators.LOCATORS_COOKIEACCEPT)
        return self.execute_script(cookies)

    def go_to_legals(self):
        legal_btn = self.find_element(Locators.LEGAL)
        return self.execute_script(legal_btn)

    def reject_cookies(self):
        reject = self.find_element(Locators.COOKIES_REJECT)
        return self.execute_script(reject)

    def learn_more(self):
        learn = self.find_element(Locators.LEARN_MORE)
        return self.execute_script(learn)

    def switch_ru(self):
        ru_locale = self.find_element(Locators.RU_LOCALE)
        return self.execute_script(ru_locale)

    def press_burger(self):
        burger = self.find_element(Locators.BURGER)
        return self.execute_script(burger)

    def press_about(self):
        about = self.find_element(Locators.ABOUT)
        return self.execute_script(about)
