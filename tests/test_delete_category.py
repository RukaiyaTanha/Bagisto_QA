# tests/test_delete_category.py
import time
from pages.categories_page import CategoriesPage
from utils.data_reader import generate_random_string


def test_create_and_delete_category(logged_in_driver):
    categories_page = CategoriesPage(logged_in_driver)
    categories_page.open_create_page()

    unique_name = "Delete Test Category " + generate_random_string(5)

    categories_page.enter_name(unique_name)
    categories_page.enter_position("1")
    categories_page.select_display_mode("products_and_description")
    categories_page.check_filterable_attribute("Price")
    categories_page.enter_description("This category will be deleted in this test.")
    categories_page.enter_slug("delete-test-" + generate_random_string(5).lower())
    categories_page.click_save()

    time.sleep(2)

    # Go to the list and confirm it exists
    categories_page.open_categories_list()
    assert categories_page.is_category_present(unique_name), "Category should exist before deletion"

    # Delete it
    categories_page.click_delete_icon_for_category(unique_name)
    categories_page.click_agree()

    assert categories_page.is_category_absent(unique_name), "Category should be deleted after confirming"