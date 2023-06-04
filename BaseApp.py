from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://localhost:3000/"

    def find_element_to_click(self, locator, time=120):
        try:
            return WebDriverWait(self.driver, time,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     StaleElementReferenceException]).until(
                EC.element_to_be_clickable(locator))
        except TimeoutError:
            print(f"Can't find element by locator")

    def find_element(self, locator, time=120):
        try:
            return WebDriverWait(self.driver, time,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     StaleElementReferenceException]).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")
        except TimeoutError:
            print(f"Can't find element by locator")

    def find_elements(self, locator, time=120):
        try:
            return WebDriverWait(self.driver, time,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     StaleElementReferenceException]).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}")
        except TimeoutError:
            print(f"Can't find element by locator")

    def wait_for_new_window(self, time=120):
        try:

            WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(3))
        except TimeoutError:
            print("A new window did not open within the given time")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def authorization(self):
        return self.driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#unlock')

    def notification(self):
        return self.driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/notification.html')


