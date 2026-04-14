import logging

from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage


def test_log_in(page: Page):
    log = logging.getLogger("test_log_in")

    welcome_page = WelcomePage(page, log)
    welcome_page.open_page()
    login_page = welcome_page.click_form_authentication_link()

    login_page.set_cookie("username", "tomsmith", "the-internet.herokuapp.com", "/")

    secure_area_page = login_page.log_in("tomsmith", "SuperSecretPassword!")

    username = secure_area_page.get_cookie("username")
    log.info(f"Username cookie: {username}")
    session = secure_area_page.get_cookie("rack.session")
    log.info(f"Session cookie: {session}")

    assert secure_area_page.get_current_url() == secure_area_page.get_page_url()
    assert secure_area_page.is_logout_button_visible(), "LogOut Button is not visible."

    expected_success_message = "You logged into a secure area!"
    actual_success_message = secure_area_page.get_success_message_text()
    assert expected_success_message in actual_success_message, (
        f"actualSuccessMessage does not contain expectedSuccessMessage\n"
        f"expectedSuccessMessage: {expected_success_message}\n"
        f"actualSuccessMessage: {actual_success_message}"
    )
