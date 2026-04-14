import logging

from playwright.sync_api import Page


class BasePage:
    """Base page object providing common browser interaction methods."""

    def __init__(self, page: Page, log: logging.Logger | None = None):
        self.page = page
        self.log = log or logging.getLogger(self.__class__.__name__)

    def open_url(self, url: str) -> None:
        self.page.goto(url)

    def find(self, selector: str):
        return self.page.locator(selector)

    def find_all(self, selector: str):
        return self.page.locator(selector)

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def type_text(self, text: str, selector: str) -> None:
        self.page.locator(selector).fill(text)

    def get_current_url(self) -> str:
        return self.page.url

    def get_current_page_title(self) -> str:
        return self.page.title()

    def get_current_page_source(self) -> str:
        return self.page.content()

    def switch_to_alert_and_get_text(self) -> str:
        dialog_message = ""

        def handle_dialog(dialog):
            nonlocal dialog_message
            dialog_message = dialog.message

        self.page.once("dialog", handle_dialog)
        return dialog_message

    def accept_alert(self) -> None:
        self.page.once("dialog", lambda dialog: dialog.accept())

    def dismiss_alert(self) -> None:
        self.page.once("dialog", lambda dialog: dialog.dismiss())

    def type_into_alert_and_accept(self, text: str) -> None:
        self.page.once("dialog", lambda dialog: dialog.accept(text))

    def switch_to_frame(self, frame_selector: str):
        return self.page.frame_locator(frame_selector)

    def press_key(self, selector: str, key: str) -> None:
        self.page.locator(selector).press(key)

    def press_key_on_page(self, key: str) -> None:
        self.log.info(f"Pressing {key} using keyboard")
        self.page.keyboard.press(key)

    def scroll_to_bottom(self) -> None:
        self.log.info("Scrolling to the bottom of the page")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def perform_drag_and_drop(self, from_selector: str, to_selector: str) -> None:
        self.page.evaluate(
            """([fromSel, toSel]) => {
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function (key, value) { this.data[key] = value; },
                    getData: function (key) { return this.data[key]; }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) { event.dataTransfer = transferData; }
                if (element.dispatchEvent) { element.dispatchEvent(event); }
                else if (element.fireEvent) { element.fireEvent("on" + event.type, event); }
            }
            function simulateHTML5DragAndDrop(element, destination) {
                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(element, dragStartEvent);
                var dropEvent = createEvent('drop');
                dispatchEvent(destination, dropEvent, dragStartEvent.dataTransfer);
                var dragEndEvent = createEvent('dragend');
                dispatchEvent(element, dragEndEvent, dropEvent.dataTransfer);
            }
            var source = document.querySelector(fromSel);
            var destination = document.querySelector(toSel);
            simulateHTML5DragAndDrop(source, destination);
            }""",
            [from_selector, to_selector],
        )

    def hover_over_element(self, selector: str) -> None:
        self.page.locator(selector).hover()

    def set_cookie(self, name: str, value: str, domain: str, path: str) -> None:
        self.log.info(f"Adding cookie {name}")
        self.page.context.add_cookies(
            [{"name": name, "value": value, "domain": domain, "path": path}]
        )
        self.log.info("Cookie added")

    def get_cookie(self, name: str) -> str:
        self.log.info(f"Getting value of cookie {name}")
        cookies = self.page.context.cookies()
        for cookie in cookies:
            if cookie["name"] == name:
                return cookie["value"]
        raise ValueError(f"Cookie '{name}' not found")
