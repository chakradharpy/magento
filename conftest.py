import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import Logger

logger = Logger.get_logger()

@pytest.fixture(scope="class")
def setup(request):
    logger.info("Initializing WebDriver.")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.maximize_window()
        driver.get("https://magento.softwaretestingboard.com//")
        request.cls.driver = driver
        # yield driver
    finally:
        # driver.quit()
        logger.info("WebDriver closed successfully.")