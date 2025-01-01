from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.logger import Logger
from locators.locator import SetsignupLocators
from pages.readexcel import read_sheet 

logger = Logger.get_logger()

class SignupPage:
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
        sheet_name = "signup"
        result = read_sheet(excel_name, sheet_name, loc, col)  # Fixed argument call
        logger.info(f"Read value from Excel: {result}")
        return result

    def create_account(self):
        create_account_page = self.wait_for_element(SetsignupLocators.create_Account_button)
        create_account_page.click()

    def enter_first_name(self):
        user_first_name = self.wait_for_element(SetsignupLocators.first_name)
        user_first_name.send_keys(SignupPage.read_value(0, 'First Name'))

    def enter_last_name(self):
        user_last_name = self.wait_for_element(SetsignupLocators.last_name)
        user_last_name.send_keys(SignupPage.read_value(0, 'Last Name'))

    def enter_email(self):
        user_email = self.wait_for_element(SetsignupLocators.email)
        user_email.send_keys(SignupPage.read_value(0, 'Email'))

    def enter_password(self):
        user_password = self.wait_for_element(SetsignupLocators.password)
        user_password.send_keys(SignupPage.read_value(0, 'Password'))

    def enter_confirm_password(self):
        user_confirm_password = self.wait_for_element(SetsignupLocators.confirm_password)
        user_confirm_password.send_keys(SignupPage.read_value(0, 'Confirm Password'))

    def click_create_account(self):
        button = self.wait_for_element(SetsignupLocators.create_Account_button)
        button.click()

    def is_success_message_present(self):
        try:
            success_message = self.driver.find_element(SetsignupLocators.success_message)
            return success_message.is_displayed()
        except NoSuchElementException:
            return False

