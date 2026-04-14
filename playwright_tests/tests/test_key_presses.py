import logging

from playwright.sync_api import Page

from playwright_tests.pages import KeyPressesPage


def test_press_key(page: Page):
    log = logging.getLogger("test_press_key")
    log.info("Starting test_press_key")

    key_presses_page = KeyPressesPage(page, log)
    key_presses_page.open_page()
    key_presses_page.press_key("Enter")

    result = key_presses_page.get_result_text()
    assert result == "You entered: ENTER", (
        f"result is not expected. \nShould be 'You entered: ENTER', but it is '{result}'"
    )


def test_press_key_with_actions(page: Page):
    log = logging.getLogger("test_press_key_with_actions")
    log.info("Starting test_press_key_with_actions")

    key_presses_page = KeyPressesPage(page, log)
    key_presses_page.open_page()
    key_presses_page.press_key("Space")

    result = key_presses_page.get_result_text()
    assert result == "You entered: SPACE", (
        f"result is not expected. \nShould be 'You entered: SPACE', but it is '{result}'"
    )
