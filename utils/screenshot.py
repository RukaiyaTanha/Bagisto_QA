# utils/screenshot.py
import os
from datetime import datetime


def take_screenshot(driver, test_name):
    """Saves a screenshot named after the test, with a timestamp, into /screenshots"""
    screenshots_dir = "screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = test_name.replace("[", "_").replace("]", "_").replace("/", "_")
    screenshot_path = f"{screenshots_dir}/{safe_test_name}_{timestamp}.png"

    driver.save_screenshot(screenshot_path)
    return screenshot_path