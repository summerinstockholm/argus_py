from .pages.login_page import LoginPage
from .pages.main_page import MainPage

def test_guest_can_authorize(browser):
    link = 'http://argusnext.ur.rt.ru:8080/argus/'
    page = LoginPage(browser, link)
    page.open()
    page.authorize_in_system()
    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_on_main_page()