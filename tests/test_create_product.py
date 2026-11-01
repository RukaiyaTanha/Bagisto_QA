
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.products_page import ProductsPage
from utils.data_reader import load_json_data, generate_unique_sku
import config


product_test_data = load_json_data("product_data.json")


@pytest.mark.parametrize("row", product_test_data)
def test_create_product_data_driven(logged_in_driver, row):
    products_page = ProductsPage(logged_in_driver)
    products_page.open()

    unique_sku = generate_unique_sku(prefix=row["sku_prefix"])

    products_page.create_quick_product(
        type_value=row["type"],
        family_value=row["family"],
        sku=unique_sku
    )

    wait = WebDriverWait(logged_in_driver, config.DEFAULT_TIMEOUT)

    wait.until(
        lambda d: "/admin/catalog/products/edit/" in d.current_url
    )

    assert "/admin/catalog/products/edit/" in logged_in_driver.current_url
