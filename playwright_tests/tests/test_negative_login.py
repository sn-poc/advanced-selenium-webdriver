import csv
import logging
import os

import pytest
from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage


def _load_csv_test_data():
    csv_path = os.path.join(
        os.path.dirname(__file__), os.pardir, "data", "negative_login_test.csv"
    )
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return [
        pytest.param(row, id=f"#{row['no']}-{row['description']}")
        for row in rows
    ]


@pytest.mark.parametrize("test_data", _load_csv_test_data())
def test_negative_log_in(page: Page, test_data: dict):
    log = logging.getLogger("test_negative_log_in")

    no = test_data["no"]
    username = test_data["username"]
    password = test_data["password"]
    expected_error_message = test_data["expectedMessage"]
    description = test_data["description"]

    log.info(f"Starting negativeLogInTest #{no} for {description}")

    welcome_page = WelcomePage(page, log)
    welcome_page.open_page()
    login_page = welcome_page.click_form_authentication_link()
    login_page.negative_log_in(username, password)
    login_page.wait_for_error_message()
    message = login_page.get_error_message_text()
    assert expected_error_message in message, "Message doesn't contain expected text."
