from pages.products_page import ProductsPage


def test_filter_products_by_active_status(logged_in_driver):

    products = ProductsPage(logged_in_driver)

    products.open()

    products.filter_by_status("active")

    assert "Active" in logged_in_driver.page_source