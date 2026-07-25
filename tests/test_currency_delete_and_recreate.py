# tests/test_currency_delete_and_recreate.py
from pages.currencies_page import CurrenciesPage

def test_delete_and_recreate_currency(logged_in_driver):
    currencies_page = CurrenciesPage(logged_in_driver)
    currencies_page.open()

    # Create a throwaway second currency first (so USD isn't the last one)
    currencies_page.create_currency(name="Euro", code_value="EUR")
    currencies_page.open()

    assert currencies_page.is_currency_present("Euro"), "EUR should exist after creation"

    # Now delete EUR (safe, since USD still exists as the other currency)
    currencies_page.click_delete_icon_for("Euro")
    currencies_page.click_agree()

    assert currencies_page.is_currency_absent("Euro"), "EUR should be deleted after clicking Agree"
    
def test_cannot_delete_last_currency(logged_in_driver):
    currencies_page = CurrenciesPage(logged_in_driver)
    currencies_page.open()

    assert currencies_page.is_currency_present("United States Dollar"), "USD should exist before test starts"

    currencies_page.click_delete_icon()
    currencies_page.click_agree()

    # USD should STILL be present - Bagisto should have blocked this deletion
    assert currencies_page.is_currency_present("United States Dollar"), "USD should NOT be deletable as the only currency"