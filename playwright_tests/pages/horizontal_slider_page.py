import logging

from playwright.sync_api import Page

from .base_page import BasePage


class HorizontalSliderPage(BasePage):
    PAGE_URL = "http://the-internet.herokuapp.com/horizontal_slider"

    RANGE = "#range"
    SLIDER = "input[type='range']"

    def __init__(self, page: Page, log: logging.Logger | None = None):
        super().__init__(page, log)

    def open_page(self) -> None:
        self.log.info(f"Opening page: {self.PAGE_URL}")
        self.open_url(self.PAGE_URL)
        self.log.info("Page opened!")

    def set_slider_to(self, value: str) -> None:
        self.log.info(f"Moving slider to {value}")
        steps = int(float(value) / 0.5)
        slider = self.page.locator(self.SLIDER)
        slider.press("Enter")
        for _ in range(steps):
            slider.press("ArrowRight")

    def get_slider_value(self) -> str:
        value = self.page.locator(self.RANGE).inner_text()
        self.log.info(f"Slider value is {value}")
        return value
