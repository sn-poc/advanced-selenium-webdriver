import logging

from playwright.sync_api import Page

from .base_page import BasePage


class EditorPage(BasePage):
    EDITOR_LOCATOR = "#tinymce"
    FRAME = "iframe"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def get_editor_text(self) -> str:
        frame = self.page.frame_locator(self.FRAME)
        text = frame.locator(self.EDITOR_LOCATOR).inner_text()
        self.log.info(f"Text from TinyMCE WYSIWYG Editor: {text}")
        return text
