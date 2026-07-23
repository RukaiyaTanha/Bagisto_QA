from pages.products_page import ProductsPage
from pages.product_edit_page import ProductEditPage


def test_edit_product(logged_in_driver):

    products = ProductsPage(
        logged_in_driver
    )

    products.open()

    products.open_product_edit(53)


    edit_page = ProductEditPage(
        logged_in_driver
    )


    edit_page.enter_product_name(
        "Azure Comfort Updated Test Product"
    )


    edit_page.save_product()


    assert "Azure Comfort Updated Test Product" in logged_in_driver.page_source