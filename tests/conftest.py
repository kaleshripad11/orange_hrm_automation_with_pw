import pytest
from playwright.sync_api import sync_playwright
from pytest_metadata.plugin import metadata_key
from utils import config_reader
import time
import pytest_html
import base64
import os

timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
config = config_reader.read_config()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config["headless_mode"], slow_mo=config["exec_speed"])
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def pytest_html_report_title(report):
    report.title = "Orange HRM Demo Automation"
    
def pytest_configure(config):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    report_file = f"reports/orange_hrm_demo_{timestamp}.html"
    config.option.htmlpath = report_file
    config.option.self_contained_html = True

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def capture_screenshot(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.capture_screenshot(path=file_path, full_page = True)

            if file_path:
                with open(file_path, "rb") as screen:
                    encoded_image = base64.b64encode(screen.read()).decode("utf-8")
                extra_html = (
                    '<div><img src="data:image/png;base64,{0}" ' 
                    'alt="screenshot" style="width:600px;height:auto;" ' 
                    'onclick="this.style.width=\'auto\';this.style.height=\'auto\'"></div>'
                ).format(encoded_image)
                report.extra = getattr(report,"extra", [])
                report.extra.append(pytest_html.extras.html(extra_html))