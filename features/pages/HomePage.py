from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()

    def check_home_page_title(self, expected_title_text):
        return self.driver.title.__eq__(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_text)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
