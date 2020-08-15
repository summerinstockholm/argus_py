from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_on_login_page(self):
        self.should_be_login_form()
    def should_be_login_form(self):
        # проверка на наличие формы логина, пароля и кнопки входа в систему.
        assert self.is_element_present(*LoginPageLocators.USER_LOGIN), "username form is not presented"
        assert self.is_element_present(*LoginPageLocators.USER_PASS), "pass form is not presented"
        assert self.is_element_present(*LoginPageLocators.ENTER_BTN), "enter button is not presented"
    def authorize_in_system(self):
        username = 'ARGUS_TESTER_MRF'
        password = '789789789'
        username_form = self.browser.find_element(*LoginPageLocators.USER_LOGIN)
        password_form = self.browser.find_element(*LoginPageLocators.USER_PASS)
        enter_button = self.browser.find_element(*LoginPageLocators.ENTER_BTN)
        username_form.send_keys(username)
        password_form.send_keys(password)
        enter_button.click()