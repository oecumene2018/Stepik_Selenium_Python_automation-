from krutik228.pages.base_page import BasePage
from krutik228.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login" in self.browser.current_url, "Неверный url-адрес"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Отсутствует логин-форма"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Отсутствует форма " \
                                                                            "регистрации"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
