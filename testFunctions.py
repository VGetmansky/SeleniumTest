from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class WorkWithFields:

    def fill_filter(self, element, value):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(value)
        element.send_keys(Keys.ENTER)
        assert (int(''.join(str(element.get_attribute('value')).split())) == value)

    def open_url(self, driver, url, value):
        driver.get(url)
        assert (value in driver.title)

    def find_filter_element(self, driver, value):
        if len(driver.find_elements(By.NAME, value)) > 0:
            element = driver.find_elements(By.NAME, value)
            return element
        else:
            assert False

    def get_filter_element(self, driver, element, value, tag_value):
        elem = self.find_filter_element(self, driver, element)[1]
        tag_before = driver.find_element(By.XPATH, tag_value).text
        self.fill_filter(self, elem, value)
        assert (int(''.join(str(elem.get_attribute('value')).split())) == value)
        self.wait_tag_changing(self, driver, tag_value, tag_before)

    def price_check_search_result(self, driver, element, min_value, max_value):
        elements = driver.find_elements(By.XPATH, element)
        for element in elements:
            element = ''.join(str(element.text).split())
            assert min_value <= int(element) <= max_value

    def wait_tag_changing(self, driver, element, value):
        try:
            WebDriverWait(driver, 120).until(lambda x: (driver.find_element(By.XPATH, element).text != value))
        except:
            assert False
