from pages.page_login import PageLogin
from pages.page_dashboard import PageDashboard
from playwright.sync_api import Page
from utils import config_reader
from utils import log_manager
import inspect
import pytest

configs = config_reader.read_config()
logger = log_manager.get_logger("TestLogin")

@pytest.fixture
def login(page):
    page.goto(configs["base_url"])
    return PageLogin(page)

@pytest.fixture
def dashboard(page):
    return PageDashboard(page)

class TestLogin:
    def test_login_with_valid_credentials(self,login, dashboard):
        logger.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        """Verify, user logs in successfully with valid credentials"""
        login.enter_username(configs["username"])
        login.enter_password(configs["password"])
        login.click_login_button()
        dashboard.is_header_displayed()
        logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test Finished~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def test_login_with_invalid_user_valid_password(self,login):
        logger.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        """Verify, login fails when user enters invalid username"""
        login.enter_username("admins")
        login.enter_password(configs["password"])
        login.click_login_button()
        assert login.get_alert_message() == "Invalid credentials", f"Expected 'Invalid credentials, got '{login.get_alert_message()}'"
        logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test Finished~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def test_login_with_valid_user_invalid_password(self,login):
        logger.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        """Verify, login fails when user enters valid username & invalid password"""
        login.enter_username(configs["username"])
        login.enter_password("pass")
        login.click_login_button()
        assert login.get_alert_message() == "Invalid credentials", f"Expected 'Invalid credentials, got '{login.get_alert_message()}'"
        logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test Finished~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def test_login_with_invalid_user_and_invalid_password(self,login):
        logger.info(f"Starting test: {inspect.currentframe().f_code.co_name}")
        """Verify, login fails when user enters invalid username & invalid password"""
        login.enter_username("userx")
        login.enter_password("pass")
        login.click_login_button()
        assert login.get_alert_message() == "Invalid credentials", f"Expected 'Invalid credentials, got '{login.get_alert_message()}'"
        logger.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Test Finished~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        