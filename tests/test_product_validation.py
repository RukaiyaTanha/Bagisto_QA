from pages import products_page

def test_create_product_without_sku(logged_in_driver):

    products = products_page(logged_in_driver)
    products.open()
    products.click_create_product()
    products.select_type("simple")
    products.select_family("1")
    products.click_save_product()

    assert "required" in logged_in_driver.page_source.lower()