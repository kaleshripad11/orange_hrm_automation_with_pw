from playwright.sync_api import Page
from pages.page_base import PageBase

class PageAddUser(PageBase):
    def __init__(self, page):
        super().__init__(page)
        self.menu_items = "a.oxd-main-menu-item>span"
