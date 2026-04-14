import logging

from playwright.sync_api import Page

from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button"
    ERROR_MESSAGE = "#flash"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def log_in(self, username: str, password: str):
        self.log.info(f"Executing LogIn with username [{username}] and password [{password}]")
        self.type_text(username, self.USERNAME_INPUT)
        self.type_text(password, self.PASSWORD_INPUT)
        self.click(self.LOGIN_BUTTON)
        from .secure_area_page import SecureAreaPage

        return SecureAreaPage(self.page, self.log)

    def negative_log_in(self, username: str, password: str) -> None:
        self.log.info(
            f"Executing Negative LogIn with username [{username}] and password [{password}]"
        )
        self.type_text(username, self.USERNAME_INPUT)
        self.type_text(password, self.PASSWORD_INPUT)
        self.click(self.LOGIN_BUTTON)

    def wait_for_error_message(self) -> None:
        self.page.locator(self.ERROR_MESSAGE).wait_for(state="visible", timeout=5000)

    def get_error_message_text(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()
