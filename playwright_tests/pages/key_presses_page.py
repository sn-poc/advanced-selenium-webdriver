import logging

from playwright.sync_api import Page

from .base_page import BasePage


class KeyPressesPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/key_presses"

    RESULT_TEXT = "#result"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")

    def press_key(self, key: str) -> None:
        self.log.info(f"Pressing {key}")
        self.page.keyboard.press(key)

    def get_result_text(self) -> str:
        result = self.page.locator(self.RESULT_TEXT).inner_text()
        self.log.info(f"Result text: {result}")
        return result
