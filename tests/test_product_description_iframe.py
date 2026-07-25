# tests/test_product_description_iframe.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from conftest import logged_in_driver
from pages.products_page import ProductsPage
from pages.product_edit_page import ProductEditPage
from utils.data_reader import generate_unique_sku
from selenium.webdriver.common.by import By
import config


def test_description_saved_after_reload(logged_in_driver):
    products_page = ProductsPage(logged_in_driver)
    products_page.open()

    unique_sku = generate_unique_sku(prefix="frame-test")
    products_page.create_quick_product(type_value="simple", family_value="1", sku=unique_sku)

    wait = WebDriverWait(logged_in_driver, config.DEFAULT_TIMEOUT)
    wait.until(lambda d: "/edit/" in d.current_url)

    product_id = logged_in_driver.current_url.split("/")[-1]
    print("Extracted product ID:", product_id)

    edit_page = ProductEditPage(logged_in_driver)

    edit_page.enter_product_name(f"Frame Test Product {unique_sku}")
    edit_page.enter_url_key(unique_sku)
    edit_page.enter_price("99.99")
    edit_page.enter_weight("1.5")

    short_desc_text = "This is the SHORT description, typed via Selenium inside an iframe."
    full_desc_text = "This is the FULL description, also typed via Selenium inside a separate iframe."

    edit_page.enter_short_description(short_desc_text)
    edit_page.enter_description(full_desc_text)

    edit_page.save_product()
    time.sleep(2)

    logged_in_driver.save_screenshot("debug_after_save.png")
    # Actively search for ANY red validation error text on the page
    error_elements = logged_in_driver.find_elements(By.XPATH, "//*[contains(@class,'text-red') or contains(text(),'required')]")
    for el in error_elements:
        if el.text.strip():
            print("VALIDATION ERROR FOUND:", el.text.strip())

    print("URL right after save attempt:", logged_in_driver.current_url)

    edit_page.open(product_id)

    saved_short_desc = edit_page.get_short_description_text()
    saved_full_desc = edit_page.get_description_text()

    assert short_desc_text in saved_short_desc, "Short Description text was not saved correctly"
    assert full_desc_text in saved_full_desc, "Description text was not saved correctly"