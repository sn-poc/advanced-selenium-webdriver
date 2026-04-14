import logging

from playwright.sync_api import Page

from .base_page import BasePage


class JSErrorPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/javascript_error"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")
