# utils/click_helper.py
import time

def safe_click(driver, element):
    """Scrolls an element into view and clicks it, with a JS-click fallback if intercepted."""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)
    try:
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)