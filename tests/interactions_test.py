import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            url = "https://demoqa.com/droppable"
            droppable_page = DroppablePage(driver, url)
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'the element has not been dropped'

        def test_accept_droppable(self, driver):
            url = "https://demoqa.com/droppable"
            droppable_page = DroppablePage(driver, url)
            droppable_page.open()
            text_not_accept, text_accept = droppable_page.drop_accept()
            assert text_not_accept == 'Drop here', 'the element "not accept" has been accepted'
            assert text_accept == 'Dropped!', 'the element "accept" has not been accepted'

        def test_prevent_droppable(self, driver):
            url = "https://demoqa.com/droppable"
            droppable_page = DroppablePage(driver, url)
            droppable_page.open()
            not_greedy_outer_text, not_greedy_inner_text, greedy_outer_text, greedy_inner_text = droppable_page.drop_prevent_propogation()
            assert not_greedy_outer_text == 'Dropped!', 'the element text has not been changed'
            assert not_greedy_inner_text == 'Dropped!', 'the element text has not been changed'
            assert greedy_outer_text == 'Outer droppable', 'the element text has been changed'
            assert greedy_inner_text == 'Dropped!', 'the element text has not been changed'

        def test_revert_draggable(self, driver):
            url = "https://demoqa.com/droppable"
            droppable_page = DroppablePage(driver, url)
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'element has not been reverted'
            assert not_will_after_move == not_will_after_revert, 'element has been reverted'






