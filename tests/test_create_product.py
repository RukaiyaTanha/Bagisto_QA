# tests/test_create_product.py
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.products_page import ProductsPage
from utils.data_reader import load_json_data, generate_unique_sku

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

    wait = WebDriverWait(logged_in_driver, 10)
    wait.until(lambda d: d.current_url != "http://127.0.0.1:8000/admin/catalog/products")

    assert "edit" in logged_in_driver.current_url