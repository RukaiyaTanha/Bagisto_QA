from pages.products_page import ProductsPage


def test_search_product(logged_in_driver):

    products = ProductsPage(logged_in_driver)

    products.open()

    products.search_product(
        "shirt"
    )

    assert products.is_product_visible("shirt")