"""Tests for JavaScript Alerts - migrated from AlertsTests.java."""

import logging

import pytest
from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage


@pytest.fixture()
def alerts_page(page: Page) -> "JavaScriptAlertsPage":
    """Navigate to the JavaScript Alerts page."""
    log = logging.getLogger("AlertsTests")
    welcome_page = WelcomePage(page, log)
    welcome_page.open_page()
    return welcome_page.click_javascript_alerts_link()


def test_js_alert(alerts_page, page: Page) -> None:
    """Verify JS Alert can be accepted and result text is correct."""
    alert_message = None

    def handle_dialog(dialog):
        nonlocal alert_message
        alert_message = dialog.message
        dialog.accept()

    page.on("dialog", handle_dialog)
    alerts_page.open_js_alert()

    result = alerts_page.get_result_text()

    assert alert_message == "I am a JS Alert", (
        f"Alert message is not expected. \n"
        f"Should be 'I am a JS Alert', but it is '{alert_message}'"
    )
    assert result == "You successfuly clicked an alert", (
        f"result is not expected. \n"
        f"Should be 'You successfuly clicked an alert', but it is '{result}'"
    )


def test_js_dismiss(alerts_page, page: Page) -> None:
    """Verify JS Confirm can be dismissed and result text is correct."""
    alert_message = None

    def handle_dialog(dialog):
        nonlocal alert_message
        alert_message = dialog.message
        dialog.dismiss()

    page.on("dialog", handle_dialog)
    alerts_page.open_js_confirm()

    result = alerts_page.get_result_text()

    assert alert_message == "I am a JS Confirm", (
        f"Alert message is not expected. \n"
        f"Should be 'I am a JS Confirm', but it is '{alert_message}'"
    )
    assert result == "You clicked: Cancel", (
        f"result is not expected. \n"
        f"Should be 'You clicked: Cancel', but it is '{result}'"
    )


def test_js_prompt(alerts_page, page: Page) -> None:
    """Verify JS Prompt - intentionally fails (mirrors original Java test)."""
    alert_message = None

    def handle_dialog(dialog):
        nonlocal alert_message
        alert_message = dialog.message
        dialog.accept(prompt_text="Hello Alert, it's Dmitry here")

    page.on("dialog", handle_dialog)
    alerts_page.open_js_prompt()

    # Intentionally append "[FAIL]" to make assertions fail, matching original Java test
    alert_message = alert_message + "[FAIL]"
    result = alerts_page.get_result_text() + "[FAIL]"

    assert alert_message == "I am a JS prompt", (
        f"Alert message is not expected. \n"
        f"Should be 'I am a JS prompt', but it is '{alert_message}'"
    )
    assert result == "You entered: Hello Alert, it's Dmitry here", (
        f"result is not expected. \n"
        f"Should be 'You entered: Hello Alert, its Dmitry here', but it is '{result}'"
    )
