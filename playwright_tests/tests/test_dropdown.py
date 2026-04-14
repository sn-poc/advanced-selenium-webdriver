from playwright.sync_api import Page

from playwright_tests.pages import WelcomePage, DropdownPage


def test_option_two(page: Page):
    welcome_page = WelcomePage(page)
    welcome_page.open_page()

    dropdown_page: DropdownPage = welcome_page.click_dropdown_link()
    dropdown_page.select_option(2)

    selected_option = dropdown_page.get_selected_option()
    assert selected_option == "Option 2", (
        f"Option 2 is not selected. Instead selected - {selected_option}"
    )
