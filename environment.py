from pages.login_page import LoginPage
from pages.alerts_frame_page import Alerts_Frame_Page
from pages.demoblaze_page import Demoblaze
from pages.base_page import BasePage
from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()
    context.alerts_frame_page = Alerts_Frame_Page()
    context.demoblaze_page = Demoblaze()

def after_all(context):
    context.browser.close()