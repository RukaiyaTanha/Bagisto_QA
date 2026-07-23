from pages.sales_report_page import SalesReportPage


def test_sales_report_filter_by_date(logged_in_driver):

    sales = SalesReportPage(
        logged_in_driver
    )

    sales.open()

    sales.open_start_date()


    # June = 5 because Flatpickr month values start from 0
    sales.select_month_year(
        month=6,
        year=2026
    )


    sales.select_day(
        "July 15, 2026"
    )

    assert "Sales" in logged_in_driver.page_source             