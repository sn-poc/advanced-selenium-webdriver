import logging

from playwright.sync_api import Page

from .base_page import BasePage


class DropdownPage(BasePage):
    DROPDOWN = "#dropdown"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def select_option(self, value: int) -> None:
        self.log.info(f"Selecting option {value} from dropdown")
        self.page.locator(self.DROPDOWN).select_option(value=str(value))

    def get_selected_option(self) -> str:
        selected_value = self.page.locator(self.DROPDOWN).input_value()
        selected_text = self.page.locator(f"{self.DROPDOWN} option[value='{selected_value}']").inner_text()
        self.log.info(f"{selected_text} is selected in dropdown")
        return selected_text
