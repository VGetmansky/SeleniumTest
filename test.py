# start arguments -v -m 'test'
import pytest

from testPage import testPageValues as TestValues
from testFunctions import WorkWithFields as FieldsFunction


@pytest.mark.test
def test_open_url(driver, url):
    FieldsFunction.open_url(FieldsFunction, driver, url, TestValues.set_base_page_title(TestValues))


@pytest.mark.test
def test_fill_max_filter_value(driver):
    FieldsFunction.get_filter_element(FieldsFunction, driver, TestValues.set_max_value_name(TestValues), 15800,
                                      TestValues.set_cell_filter_tag(TestValues))


@pytest.mark.test
def test_fill_min_filter_value(driver):
    FieldsFunction.get_filter_element(FieldsFunction, driver, TestValues.set_min_value_name(TestValues), 15000,
                                      TestValues.set_cell_filter_tag(TestValues))


@pytest.mark.test
def test_check_search_result(driver):
    FieldsFunction.price_check_search_result(FieldsFunction, driver, TestValues.set_cell_price_xpath(TestValues),
                                             15000, 15800)
