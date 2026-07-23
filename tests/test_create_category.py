# tests/test_create_category.py
import time
from pages.categories_page import CategoriesPage
from utils.data_reader import generate_random_string


def test_create_category(logged_in_driver):
    categories_page = CategoriesPage(logged_in_driver)
    categories_page.open_create_page()

    unique_name = "Test Category " + generate_random_string(5)

    categories_page.enter_name(unique_name)
    categories_page.enter_position("1")
    categories_page.select_display_mode("products_and_description")
    categories_page.check_filterable_attribute("Price")
    categories_page.enter_description("This is a test category created via Selenium.")
    categories_page.enter_slug("test-category-" + generate_random_string(5).lower())
    categories_page.click_save()

    time.sleep(2)

    logged_in_driver.save_screenshot("debug_category_save.png")
    print("URL right after save attempt:", logged_in_driver.current_url)

    assert "/create" not in logged_in_driver.current_url, "Category was not saved successfully"