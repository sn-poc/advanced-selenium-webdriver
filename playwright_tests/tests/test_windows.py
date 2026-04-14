from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage


def test_new_window(page: Page) -> None:
    welcome_page = WelcomePage(page)
    welcome_page.open_page()

    windows_page = welcome_page.click_multiple_windows_link()

    new_window_page = windows_page.switch_to_new_window_page()

    page_source = new_window_page.get_current_page_source()
    assert "New Window" in page_source, (
        "New page source doesn't contain expected text"
    )
