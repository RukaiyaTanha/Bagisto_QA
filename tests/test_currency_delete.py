# tests/test_currency_delete.py
from pages.currencies_page import CurrenciesPage


def test_delete_currency_popup_disagree(logged_in_driver):
    currencies_page = CurrenciesPage(logged_in_driver)
    currencies_page.open()

    # Sanity check: USD should exist before we even attempt delete
    assert currencies_page.is_currency_present(), "USD currency should exist before test starts"

    currencies_page.click_delete_icon()
    currencies_page.click_disagree()

    # USD should STILL be present after clicking Disagree
    assert currencies_page.is_currency_present(), "USD should NOT be deleted after clicking Disagree"