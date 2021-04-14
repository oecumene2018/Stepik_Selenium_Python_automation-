from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.no_items_in_basket()
        self.is_element_present(*BasePageLocators.BASKET_CONTENT)
        self.basket_is_empty()

    def no_items_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS), "No items"

    def basket_is_empty(self):
        print(self.browser.find_element(*BasePageLocators.BASKET_CONTENT).text)
        assert "Your basket is empty." in \
            self.browser.find_element(*BasePageLocators.BASKET_CONTENT).text
    
