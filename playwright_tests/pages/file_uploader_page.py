import logging
import os

from playwright.sync_api import Page

from .base_page import BasePage


class FileUploaderPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/upload"

    CHOOSE_FILE_FIELD = "#file-upload"
    UPLOAD_BUTTON = "#file-submit"
    UPLOADED_FILES = "#uploaded-files"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")

    def push_upload_button(self) -> None:
        self.log.info("Clicking on upload button")
        self.page.locator(self.UPLOAD_BUTTON).click()

    def select_file(self, file_path: str) -> None:
        self.log.info(f"Selecting '{file_path}' file")
        self.page.locator(self.CHOOSE_FILE_FIELD).set_input_files(file_path)
        self.log.info("File selected")

    def get_uploaded_files_names(self) -> str:
        names = self.page.locator(self.UPLOADED_FILES).inner_text()
        self.log.info(f"Uploaded files: {names}")
        return names
