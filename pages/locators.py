from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPageLocators():
    USER_LOGIN = (By.XPATH, "//input[@id='login_form-username']")
    USER_PASS = (By.XPATH, "//input[@id='login_form-password']")
    ENTER_BTN = (By.XPATH, "//button[@id='login_form-submit']")
class MainPageLocators():
    LOGOUT_BTN = (By.XPATH, "//button[@id='mrf_logout']")
