from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Alerts_Frame_Page(BasePage):
    alerts_frame = (By.XPATH, "//h5[contains(text(),\"Alerts, Frame & Windows\")]")
    alerts = (By.XPATH, "//ul[@class=\"menu-list\"] / li / span[contains(text(), \"Alerts\")]")
    confirm_button = (By.ID, "confirmButton")
    confirmed_text = (By.ID, "confirmResult")

    def click_alerts_frame(self):
        self.chrome.find_element(*self.alerts_frame).click()

    def click_alerts(self):
        self.chrome.find_element(*self.alerts).click()

    def click_confirm_button(self):
        self.chrome.find_element(*self.confirm_button).click()

    def click_ok_button(self):
        self.chrome.switch_to.alert.accept()

    def confirmed_ok(self):
        confirmed_ok = self.chrome.find_element(*self.confirmed_text)
        assert confirmed_ok.text == "You selected Ok", confirmed_ok.text

    def click_cancel_button(self):
        self.chrome.switch_to.alert.dismiss()

    def confirmed_cancel(self):
        confirmed_cancel = self.chrome.find_element(*self.confirmed_text)
        assert confirmed_cancel.text == "You selected Cancel", confirmed_cancel.text
