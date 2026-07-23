from pages.categories_page import CategoriesPage


def test_categories_next_page(logged_in_driver):

    page = CategoriesPage(logged_in_driver)
    page.open_categories_list()
    first_page_row = page.get_first_category_name()
    page.go_to_next_page()
    second_page_row = page.get_first_category_name()
    
    assert first_page_row != second_page_row