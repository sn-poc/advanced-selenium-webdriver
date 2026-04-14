import logging

from playwright.sync_api import Page

from .base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    JS_ALERT_BUTTON = "button:has-text('Click for JS Alert')"
    JS_CONFIRM_BUTTON = "button:has-text('Click for JS Confirm')"
    JS_PROMPT_BUTTON = "button:has-text('Click for JS Prompt')"
    RESULT_TEXT = "#result"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_js_alert(self) -> None:
        self.log.info("Clicking on 'Click for JS Alert' button to open alert")
        self.page.locator(self.JS_ALERT_BUTTON).click()

    def open_js_confirm(self) -> None:
        self.log.info("Clicking on 'Click for JS Confirm' button to open alert")
        self.page.locator(self.JS_CONFIRM_BUTTON).click()

    def open_js_prompt(self) -> None:
        self.log.info("Clicking on 'Click for JS Prompt' button to open alert")
        self.page.locator(self.JS_PROMPT_BUTTON).click()

    def get_result_text(self) -> str:
        result = self.page.locator(self.RESULT_TEXT).inner_text()
        self.log.info(f"Result text: {result}")
        return result
