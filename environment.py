from pages.login_page import LoginPage
from pages.base_page import BasePage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()

def after_all(context):
    context.browser.close()