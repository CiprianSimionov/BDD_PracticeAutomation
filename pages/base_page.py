from browser import Browser


class BasePage(Browser):
    def access_login_page(self):
        self.chrome.get("https://practicetestautomation.com/practice-test-login/")
    def access_elements_page(self):
        self.chrome.get("https://demoqa.com/")
