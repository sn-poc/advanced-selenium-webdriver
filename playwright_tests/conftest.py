import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def page(browser):
    """Create a new browser page for each test."""
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()
