# tests/test_product_type_dropdown_options.py
from pages.products_page import ProductsPage


def test_product_type_dropdown_has_all_expected_options(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)
    products_page.open()

    actual_options = products_page.get_all_type_options()
    print("Actual dropdown options found:", actual_options)

    expected_options = [
        "Simple",
        "Configurable",
        "Grouped",
        "Bundle",
        "Downloadable",
        "Virtual",
        "Booking"
    ]

    for expected in expected_options:
        assert expected in actual_options, f"Expected option '{expected}' not found in dropdown"