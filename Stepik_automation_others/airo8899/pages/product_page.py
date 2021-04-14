from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.equal_name()
        self.total_baslet_is_price()


    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
    
    def equal_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT).text == \
                self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text, \
                "Different name"
    
    def total_baslet_is_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text == \
                self.browser.find_element(*ProductPageLocators.TOTAL_BASKET).text, \
                "Different price"



    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"