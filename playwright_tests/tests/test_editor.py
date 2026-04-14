import logging

from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage


def test_default_editor_value(page: Page):
    log = logging.getLogger("test_default_editor_value")
    log.info("Starting test_default_editor_value")

    welcome_page = WelcomePage(page, log)
    welcome_page.open_page()
    welcome_page.scroll_to_bottom()

    editor_page = welcome_page.click_wysiwyg_editor_link()
    editor_text = editor_page.get_editor_text()

    assert editor_text == "Your content goes here.", (
        f"Editor default text is not expected. It is: {editor_text}"
    )
