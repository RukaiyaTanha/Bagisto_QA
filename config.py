import os

BASE_URL = os.getenv(
    "BASE_URL",
    "http://localhost:8000"
).rstrip("/")
ADMIN_URL = BASE_URL + "/admin"
PRODUCTS_URL = ADMIN_URL + "/catalog/products"
CURRENCIES_URL = ADMIN_URL + "/settings/currencies"
PRODUCT_EDIT_URL = ADMIN_URL + "/catalog/products/edit/"
ADMIN_EMAIL = os.getenv(
    "ADMIN_EMAIL",
    "admin@example.com"
)
ADMIN_PASSWORD = os.getenv(
    "ADMIN_PASSWORD",
    "admin123"
)
DEFAULT_TIMEOUT = 10
