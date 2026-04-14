import logging

from playwright.sync_api import Page

from .base_page import BasePage


class NewWindowPage(BasePage):
    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)
