from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage, CheckboxesPage


def test_selecting_two_checkboxes(page: Page):
    welcome_page = WelcomePage(page)
    welcome_page.open_page()

    checkboxes_page: CheckboxesPage = welcome_page.click_checkboxes_link()
    checkboxes_page.select_all_checkboxes()

    assert checkboxes_page.are_all_checkboxes_checked(), "Not all checkboxes are checked"
