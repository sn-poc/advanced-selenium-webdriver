import logging

from playwright.sync_api import Page

from playwright_tests.pages import HoversPage


def test_user2_profile(page: Page):
    log = logging.getLogger("test_user2_profile")
    log.info("Starting test_user2_profile")

    hovers_page = HoversPage(page, log)
    hovers_page.open_page()
    hovers_page.open_user_profile(2)

    assert "/users/2" in hovers_page.get_current_url(), (
        "Url of opened page is not expected User 2 page url"
    )
