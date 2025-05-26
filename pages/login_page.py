from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    username = (By.XPATH, "//input[@id=\"username\"]")
    password = (By.XPATH, "//input[@id=\"password\"]")
    login_button = (By.XPATH, "//button[@id=\"submit\"]")
    logout_button = (By.XPATH, "//a[contains(text(),\"Log out\")]")
    logged_In_area = (By.XPATH, "//h1")
    display_banner = (By.ID, "error")
    banner_invalid_password = "Your password is invalid!"
    banner_invalid_username = "Your username is invalid!"
    valid_username = "student"
    valid_password = "Password123"
    wrong_password = "Pass123"

    def send_valid_username_and_password(self):
        self.chrome.find_element(*self.username).send_keys(self.valid_username)
        self.chrome.find_element(*self.password).send_keys(self.valid_password)

    def click_login_button(self):
        self.chrome.find_element(*self.login_button).click()

    def check_Logged_In_page(self):
        check = self.chrome.find_element(*self.logged_In_area)
        assert check.text == "Logged In Successfully", check.text

    def check_logout_button(self):
        assert self.chrome.find_element(*self.logout_button).is_enabled()

    def send_correct_username_wrong_password(self):
        self.chrome.find_element(*self.username).send_keys(self.valid_username)
        self.chrome.find_element(*self.password).send_keys(self.wrong_password)

    def password_invalid_banner(self):
        if self.display_banner == self.banner_invalid_password:
            assert True

    def send_wrong_username_and_password(self, username, password):
        self.chrome.find_element(*self.username).send_keys(username)
        self.chrome.find_element(*self.password).send_keys(password)

    def username_invalid_banner(self):
        if self.display_banner == self.banner_invalid_username:
            assert True
