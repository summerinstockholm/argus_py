from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_on_main_page(self):
        self.should_be_logout_button
    def should_be_logout_button(self):
        # проверка на наличие кнопки выхода
        assert self.is_element_present(*MainPageLocators.LOGOUT_BTN), "logout button is not presented"
