import logging

from playwright.sync_api import Page

from .base_page import BasePage


class WelcomePage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/"

    FORM_AUTHENTICATION_LINK = "text=Form Authentication"
    CHECKBOXES_LINK = "text=Checkboxes"
    DROPDOWN_LINK = "text=Dropdown"
    JAVASCRIPT_ALERTS_LINK = "text=JavaScript Alerts"
    MULTIPLE_WINDOWS_LINK = "text=Multiple Windows"
    EDITOR_LINK = "text=WYSIWYG Editor"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")

    def click_form_authentication_link(self):
        self.log.info("Clicking Form Authentication link on Welcome Page")
        self.click(self.FORM_AUTHENTICATION_LINK)
        from .login_page import LoginPage

        return LoginPage(self.page, self.log)

    def click_checkboxes_link(self):
        self.log.info("Clicking Checkboxes link on Welcome Page")
        self.click(self.CHECKBOXES_LINK)
        from .checkboxes_page import CheckboxesPage

        return CheckboxesPage(self.page, self.log)

    def click_dropdown_link(self):
        self.log.info("Clicking Dropdown link on Welcome Page")
        self.click(self.DROPDOWN_LINK)
        from .dropdown_page import DropdownPage

        return DropdownPage(self.page, self.log)

    def click_javascript_alerts_link(self):
        self.log.info("Clicking JavaScript Alerts link on Welcome Page")
        self.click(self.JAVASCRIPT_ALERTS_LINK)
        from .javascript_alerts_page import JavaScriptAlertsPage

        return JavaScriptAlertsPage(self.page, self.log)

    def click_multiple_windows_link(self):
        self.log.info("Clicking Multiple Windows link on Welcome Page")
        self.click(self.MULTIPLE_WINDOWS_LINK)
        from .windows_page import WindowsPage

        return WindowsPage(self.page, self.log)

    def click_wysiwyg_editor_link(self):
        self.log.info("Clicking WYSIWYG Editor link on Welcome Page")
        self.click(self.EDITOR_LINK)
        from .editor_page import EditorPage

        return EditorPage(self.page, self.log)
