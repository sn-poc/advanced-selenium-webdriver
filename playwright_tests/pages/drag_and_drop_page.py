import logging

from playwright.sync_api import Page

from .base_page import BasePage


class DragAndDropPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/drag_and_drop"

    COLUMN_A = "#column-a"
    COLUMN_B = "#column-b"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")

    def drag_a_to_b(self) -> None:
        self.log.info("Drag and drop A box on B box")
        self.perform_drag_and_drop(self.COLUMN_A, self.COLUMN_B)

    def get_column_a_text(self) -> str:
        text = self.page.locator(self.COLUMN_A).inner_text()
        self.log.info(f"Column A Text: {text}")
        return text

    def get_column_b_text(self) -> str:
        text = self.page.locator(self.COLUMN_B).inner_text()
        self.log.info(f"Column B Text: {text}")
        return text
