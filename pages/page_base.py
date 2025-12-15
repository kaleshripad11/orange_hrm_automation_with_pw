from playwright.sync_api import Page, expect
from utils.log_manager import get_logger
import inspect

class PageBase:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def log_actions(self, locator: str, action: str):
        action_method = inspect.currentframe().f_code.co_name

    # Action methods
    def click(self, locator: str):
        self.logger.info(f"Clicking element: {locator}")
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=10000)
        element.click()

    def clear_text(self, locator: str):
        self.logger.info(f"Clearing input text for: {locator}")
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=10000)
        element.clear()

    def enter_text(self, locator: str, input_text: str):
        self.logger.info(f"Entering input text '{input_text}' for: {locator}")
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=10000)
        element.fill(input_text)

    def get_text(self, locator: str):
        self.logger.info(f"Fetching visible text from element: {locator}")
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=10000)
        return element.inner_text()