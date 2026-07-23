# tests/test_create_product_validation.py
import time
from pages.products_page import ProductsPage


def test_create_product_fails_without_sku(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)
    products_page.open()

    products_page.create_product_without_sku(
        type_value="simple",
        family_value="1"
    )

    time.sleep(2)   # give Bagisto a moment to attempt/reject the save

    # Should NOT have navigated to an edit page - validation should have blocked it
    assert products_page.is_still_on_products_page(), "Product should NOT be created without SKU"