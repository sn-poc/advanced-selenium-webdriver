import logging

from playwright.sync_api import Page

from .base_page import BasePage


class WindowsPage(BasePage):
    CLICK_HERE_LINK = "text=Click Here"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_new_window(self):
        self.log.info("Clicking 'Click Here' link")
        with self.page.expect_popup() as popup_info:
            self.page.locator(self.CLICK_HERE_LINK).click()
        return popup_info.value

    def switch_to_new_window_page(self):
        new_page = self.open_new_window()
        from .new_window_page import NewWindowPage

        return NewWindowPage(new_page, self.log)
