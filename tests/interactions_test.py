import time

from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:
    class TestSortablePage:

        def test_sortable_page(self, driver):
            url = "https://demoqa.com/sortable"
            sortable_page = SortablePage(driver, url)
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'List items order did not changed'
            assert grid_before != grid_after, 'Grid items order did not changed'

    class TestSelectablePage:

        def test_selectable_page(self, driver):
            url = "https://demoqa.com/selectable"
            selectable_page = SelectablePage(driver, url)
            selectable_page.open()
            list_item = selectable_page.select_list_item()
            grid_item = selectable_page.select_grid_item()
            assert len(list_item) > 0, 'List item did not selected'
            assert len(grid_item) > 0, 'Grid item did not selected'
