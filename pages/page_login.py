from .page_base import PageBase
from playwright.sync_api import Page, expect

class PageLogin(PageBase):
    def __init__(self, page: Page):
        super().__init__(page)
        self.txt_username = "input[name='username']"
        self.txt_password = "input[name='password']"
        self.btn_login = "button[type='submit']"
        self.alert_failed_login = ".oxd-alert-content>p"

    def enter_username(self, username: str):
        self.enter_text(self.txt_username, username)

    def enter_password(self, password: str):
        self.enter_text(self.txt_password, password)

    def click_login_button(self):
        self.click(self.btn_login)

    def get_alert_message(self):
        return self.page.locator(self.alert_failed_login).inner_text()