import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    class TestResizablePage:

        def test_resizable_page(self, driver):
            url = "https://demoqa.com/resizable"
            resizable_page = ResizablePage(driver, url)
            resizable_page.open()
            limit_max, limit_min = resizable_page.change_size_limit_box()
            no_limit_max, no_limit_min = resizable_page.change_size_no_limit_box()
            assert limit_max == ('500px', '300px'), "Max size not equal to '500px', '300px'"
            assert limit_min == ('150px', '150px'), "Min size not equal to '150px', '150px'"
            assert no_limit_min != no_limit_max, "No limit box has not been changed"



