import pytest
from pages.signup import SignupPage


@pytest.mark.usefixtures("setup")
class TestSignup:
    def test_admin_name(self):
        sp = SignupPage(self.driver)
        sp.enter_first_name()
        sp.enter_last_name()
        sp.enter_email()
        sp.enter_password()
        sp.enter_confirm_password()
        sp.click_create_account()
        assert sp.is_success_message_present(), "Success message not displayed after signup"