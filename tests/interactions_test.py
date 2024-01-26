from pages.interactions_page import SortablePage


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
