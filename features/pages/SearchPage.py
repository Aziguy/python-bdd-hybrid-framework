from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    valid_product_link_text = "HP LP3065"
    message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_product_link_text)
        return self.display_status("valid_product_link_text", self.valid_product_link_text).is_displayed()

    def display_status_of_message(self, expected_message_text):
        return self.driver.find_element(By.XPATH, self.message_xpath).text.__eq__(expected_message_text)
