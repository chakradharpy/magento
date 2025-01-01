
from selenium.webdriver.common.by import By

class SetsignupLocators:

    create_account_path = (By.XPATH, "(//a[normalize-space()='Create an Account'])[1]")
    first_name = (By.XPATH, "//input[@id='firstname']")
    last_name = (By.XPATH, "(//input[@id='lastname'])[1]")
    email = (By.XPATH, "(//input[@id='email_address'])[1]")
    password = (By.XPATH, "(//input[@id='password'])[1]")
    confirm_password = (By.XPATH, "(//input[@id='password-confirmation'])[1]")
    create_Account_button = (By.XPATH, "//button[@title='Create an Account']//span[contains(text(),'Create an Account')]")
    success_message = (By.XPATH, "//div[contains(text(), 'Thank you for registering')]")

class SetLoginLocators:
    login_email = (By.XPATH, "//input[@id='email']")
    login_password = (By.XPATH, "(//input[@id='pass'])[1]")
    login_button = (By.XPATH, "(//button[@id='send2'])[1]")
    signin_path = (By.XPATH, "(//li[@class='authorization-link'])[1]")