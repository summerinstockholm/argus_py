from .pages.login_page import LoginPage


def test_guest_authorize_elements_visible(browser):
    link = 'http://argusnext.ur.rt.ru:8080/argus/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_on_login_page()
