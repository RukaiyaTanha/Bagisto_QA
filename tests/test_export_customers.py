import os
import time

from pages.customers_page import CustomersPage


def test_export_customers_xls(logged_in_driver):

    customers_page = CustomersPage(logged_in_driver)

    customers_page.open()

    customers_page.export_customers("xls")


    download_folder = "downloads"

    timeout = 20
    downloaded = False

    for _ in range(timeout):

        files = os.listdir(download_folder)

        print("Downloaded files:", files)

        if any(
            file.endswith(".xls")
            for file in files
        ):
            downloaded = True
            break

        time.sleep(1)


    assert downloaded, "Customer XLS file was not downloaded"