import logging

from playwright.sync_api import Page

from .base_page import BasePage


class CheckboxesPage(BasePage):
    CHECKBOX = "input[type='checkbox']"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def select_all_checkboxes(self) -> None:
        self.log.info("Checking all unchecked checkboxes")
        checkboxes = self.page.locator(self.CHECKBOX)
        count = checkboxes.count()
        for i in range(count):
            if not checkboxes.nth(i).is_checked():
                checkboxes.nth(i).click()

    def are_all_checkboxes_checked(self) -> bool:
        self.log.info("Verifying that all checkboxes are checked")
        checkboxes = self.page.locator(self.CHECKBOX)
        count = checkboxes.count()
        for i in range(count):
            if not checkboxes.nth(i).is_checked():
                return False
        return True
