from playwright.sync_api import Page

from playwright_tests.pages import DragAndDropPage


def test_drag_a_to_b(page: Page):
    drag_and_drop_page = DragAndDropPage(page)
    drag_and_drop_page.open_page()

    drag_and_drop_page.drag_a_to_b()

    column_a_text = drag_and_drop_page.get_column_a_text()
    assert column_a_text == "B", f"Column A header should be B, but it is: {column_a_text}"

    column_b_text = drag_and_drop_page.get_column_b_text()
    assert column_b_text == "A", f"Column B header should be A, but it is: {column_b_text}"
