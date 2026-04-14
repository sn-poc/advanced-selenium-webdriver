import logging

from playwright.sync_api import Page

from .base_page import BasePage


class SecureAreaPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/secure"

    LOGOUT_BUTTON = "a.button.secondary.radius"
    MESSAGE = "#flash-messages"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def get_page_url(self) -> str:
        return self.PAGE_URL

    def is_logout_button_visible(self) -> bool:
        return self.page.locator(self.LOGOUT_BUTTON).is_visible()

    def get_success_message_text(self) -> str:
        return self.page.locator(self.MESSAGE).inner_text()
