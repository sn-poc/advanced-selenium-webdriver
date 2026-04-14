import logging

from playwright.sync_api import Page

from .base_page import BasePage


class HoversPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/hovers"

    AVATAR = "div.figure"
    VIEW_PROFILE_LINK = "a:has-text('View profile')"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")

    def open_user_profile(self, user_number: int) -> None:
        avatars = self.page.locator(self.AVATAR)
        specified_avatar = avatars.nth(user_number - 1)
        specified_avatar.hover()
        specified_avatar.locator(self.VIEW_PROFILE_LINK).click()
