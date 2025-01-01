from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.logger import Logger
from locators.locator import SetLoginLocators
from pages.readexcel import read_sheet
import time

logger = Logger.get_logger()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Element with locator {locator} not found within {timeout} seconds.")
            raise

    @staticmethod
    def read_value(loc, col):
        excel_name = "signup_data.xlsx"
        sheet_name = "login"
        result = read_sheet(excel_name, sheet_name, loc, col)
        logger.info(f"Read value from Excel: {result}")
        return result
    
    def login_page(self):
        time.sleep(6)
        signin_page = self.wait_for_element(SetLoginLocators.signin_path)
        signin_page.click()

    def enter_email(self):
        email_field = self.wait_for_element(SetLoginLocators.login_email)
        email_field.send_keys(LoginPage.read_value(0, 'Email'))

    def enter_password(self):
        password_field = self.wait_for_element(SetLoginLocators.login_password)
        password_field.send_keys(LoginPage.read_value(0, 'Password'))

    def click_login_button(self):
        login_button = self.wait_for_element(SetLoginLocators.login_button)
        login_button.click()

