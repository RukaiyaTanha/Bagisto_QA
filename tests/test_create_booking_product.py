# tests/test_create_booking_product.py
from selenium.webdriver.support.ui import WebDriverWait
from pages.products_page import ProductsPage
from utils.data_reader import generate_unique_sku
import config


def test_create_booking_product(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)
    products_page.open()

    unique_sku = generate_unique_sku(prefix="booking-test")

    products_page.create_quick_product(
        type_value="booking",
        family_value="9",
        sku=unique_sku
    )

    wait = WebDriverWait(logged_in_driver, config.DEFAULT_TIMEOUT)
    wait.until(lambda d: d.current_url != "http://127.0.0.1:8000/admin/catalog/products")

    assert "edit" in products_page.get_current_url()
    assert "/admin/catalog/products/edit/" in products_page.get_current_url()