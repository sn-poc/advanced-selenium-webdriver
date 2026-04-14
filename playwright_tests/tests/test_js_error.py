import logging

from playwright.sync_api import Page

from playwright_tests.pages import JSErrorPage


def test_js_error(page: Page):
    log = logging.getLogger("test_js_error")
    log.info("Starting test_js_error")

    errors: list[str] = []

    def handle_console(msg):
        if msg.type == "error":
            errors.append(msg.text)

    page.on("console", handle_console)

    js_error_page = JSErrorPage(page, log)
    js_error_page.open_page()

    assert len(errors) == 0, (
        "JavaScript errors found on page:\n" + "\n".join(f"Severe error: {e}" for e in errors)
    )
