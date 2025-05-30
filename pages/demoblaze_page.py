from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Demoblaze(BasePage):
    laptops = (By.XPATH, "//a[@onclick=\"byCat('notebook')\"]")
    macBook_air = (By.XPATH, "//a[contains(text(), \"MacBook air\")]")
    add_to_cart_button = (By.XPATH, "//a[contains(@class, \"btn btn-success btn-lg\")]")
    product_title = (By.XPATH, "//td[contains(text(), \"MacBook air\")]")
    cart = (By.ID, "cartur")
    place_order_button = (By.XPATH, "//button[@class=\"btn btn-success\"]")
    name = (By.ID, "name")
    country = (By.ID, "country")
    city = By.ID, ("city")
    credit_card = By.ID, ("card")
    month = By.ID, ("month")
    year = By.ID, ("year")
    purchase_button = (By.XPATH, "//button[contains(text(), \"Purchase\")]")
    purchase_banner = (By.XPATH, "//div[@class= \"sweet-alert  showSweetAlert visible\"]/h2[contains(text(), \"Thank you for your purchase!\")]")


    def click_laptops_categories(self):
        self.chrome.find_element(*self.laptops).click()

    def click_macBook_air(self):
        self.chrome.find_element(*self.macBook_air).click()

    def add_to_cart(self):
        self.chrome.find_element(*self.add_to_cart_button).click()

    def verify_cart_product(self):
        self.chrome.find_element(*self.cart).click()
        assert self.chrome.find_element(*self.product_title).text == "MacBook air"

    def place_order(self):
        self.chrome.find_element(*self.cart).click()
        self.chrome.find_element(*self.place_order_button).click()

    def fill_out_form(self):
        self.chrome.find_element(*self.name).send_keys("userOne")
        self.chrome.find_element(*self.country).send_keys("Malta")
        self.chrome.find_element(*self.city).send_keys("Valleta")
        self.chrome.find_element(*self.credit_card).send_keys("0001-0100-0110")
        self.chrome.find_element(*self.month).send_keys("june")
        self.chrome.find_element(*self.year).send_keys("2025")
        self.chrome.find_element(*self.purchase_button).click()

    def verify_purchase(self):
        verify_banner = self.chrome.find_element(*self.purchase_banner)
        assert verify_banner.text == "Thank you for your purchase!", verify_banner.text



