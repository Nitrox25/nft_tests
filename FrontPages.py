from BaseApp import BasePage
from selenium.webdriver.common.by import By


class FrontLocators:
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_ENTER = (By.CSS_SELECTOR, "button[data-testid='unlock-submit']")
    LOCATOR_collection_name = (By.CSS_SELECTOR, 'input[placeholder="Enter collection name"]')
    LOCATOR_collection_symbol = (By.CSS_SELECTOR, 'input[placeholder="Enter collection symbol"]')
    LOCATOR_collection_token_url = (By.CSS_SELECTOR, 'input[placeholder="Enter collection token URI"]')
    LOCATOR_button = (By.CSS_SELECTOR, '.btn-primary')
    LOCATOR_button_conform = (By.CSS_SELECTOR, 'button[data-testid="page-container-footer-next"]')
    LOCATOR_events = (By.CSS_SELECTOR, '.list-group-item:last-child')
    LOCATOR_collection_addres = (By.CSS_SELECTOR, "input.form-control[placeholder='Enter collection address']")
    LOCATOR_recipient_address = (By.CSS_SELECTOR , "input[placeholder = 'Enter recipient address']")
    LOCATOR_token_id = (By.CSS_SELECTOR, "input[placeholder = 'Enter token id']")



class SearchHelper(BasePage):
    def enter_password(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_PASSWORD).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_PASSWORD).send_keys(words)

    def enter_button(self):
        return self.find_element_to_click(FrontLocators.LOCATOR_ENTER)

    def enter_collection_name(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_collection_name).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_collection_name).send_keys(words)

    def enter_collection_symbol(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_collection_symbol).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_collection_symbol).send_keys(words)

    def enter_collection_token_url(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_collection_token_url).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_collection_token_url).send_keys(words)

    def buttons_send_to(self):
        return self.find_elements(FrontLocators.LOCATOR_button)

    def enter_button_conform(self):
        return self.find_element_to_click(FrontLocators.LOCATOR_button_conform)

    def select_last_event(self):
        return self.find_element(FrontLocators.LOCATOR_events)

    def enter_collection_address(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_collection_addres).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_collection_addres).send_keys(words)

    def enter_recipient_address(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_recipient_address).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_recipient_address).send_keys(words)

    def enter_token_id(self, words):
        self.find_element_to_click(FrontLocators.LOCATOR_token_id).click()
        return self.find_element_to_click(FrontLocators.LOCATOR_token_id).send_keys(words)

