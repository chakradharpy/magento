import pytest
from pages.login import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_user_login(self):
        lp = LoginPage(self.driver)
        lp.login_page()
        lp.enter_email()
        lp.enter_password()
        lp.click_login_button()
