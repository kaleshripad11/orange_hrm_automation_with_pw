from .page_base import PageBase
from playwright.sync_api import Page, expect

class PageDashboard(PageBase):
    def __init__(self, page):
        super().__init__(page)
        self.dashboard_heading = ".oxd-topbar-header-breadcrumb>h6"

    def is_header_displayed(self):
        expect(self.page.locator(self.dashboard_heading)).to_have_text("Dashboard")
