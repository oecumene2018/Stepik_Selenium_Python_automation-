from .base_page import BasePage
from .locators import LoginPageLocarors, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is not login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocarors.LOGIN_FORN), "There is not login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocarors.REGISTER_FORM), "There is not register form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocarors.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocarors.REGISTRATION_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocarors.REGISTRATION_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocarors.REGISTRATION_BUTTON).click()