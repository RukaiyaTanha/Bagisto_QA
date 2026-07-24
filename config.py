# config.py
import os
BASE_URL = os.getenv('BASE_URL', 'http://localhost:8000')
#BASE_URL = "http://127.0.0.1:8000"
ADMIN_URL = BASE_URL + "/admin"
PRODUCTS_URL = ADMIN_URL + "/catalog/products"
CURRENCIES_URL = ADMIN_URL + "/settings/currencies"
PRODUCT_EDIT_URL = ADMIN_URL + "/catalog/products/edit/"

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"

'''
ADMIN_EMAIL = os.getenv(
    "ADMIN_EMAIL",
    "admin@example.com"
)

ADMIN_PASSWORD = os.getenv(
    "ADMIN_PASSWORD",
    "admin123"
)
'''
DEFAULT_TIMEOUT = 10