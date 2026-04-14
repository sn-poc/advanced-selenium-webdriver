from playwright.sync_api import Page

from playwright_tests.pages import HorizontalSliderPage


def test_slider(page: Page):
    horizontal_slider_page = HorizontalSliderPage(page)
    horizontal_slider_page.open_page()

    value = "3.5"
    horizontal_slider_page.set_slider_to(value)

    slider_value = horizontal_slider_page.get_slider_value()
    assert slider_value == value, f"Range is not correct. It is: {slider_value}"
