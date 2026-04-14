from pathlib import Path

import pytest
from playwright.sync_api import Page

from playwright_tests.pages import FileUploaderPage

RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources" / "files"


@pytest.mark.parametrize(
    "no, file_name",
    [
        (1, "index.html"),
        (2, "logo.png"),
        (3, "text.txt"),
    ],
)
def test_file_upload(page: Page, no: int, file_name: str) -> None:
    file_uploader_page = FileUploaderPage(page)
    file_uploader_page.open_page()

    file_path = str(RESOURCES_DIR / file_name)
    file_uploader_page.select_file(file_path)
    file_uploader_page.push_upload_button()

    uploaded_names = file_uploader_page.get_uploaded_files_names()
    assert file_name in uploaded_names, (
        f"Our file ({file_name}) is not one of the uploaded ({uploaded_names})"
    )
