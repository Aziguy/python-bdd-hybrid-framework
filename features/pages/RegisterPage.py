from selenium.webdriver.common.by import By

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.type_into_element("first_name_field_id", self.first_name_field_id, first_name_text)

    def enter_last_name(self, last_name_text):
        self.type_into_element("last_name_field_id", self.last_name_field_id, last_name_text)

    def enter_email(self, email_text):
        self.type_into_element("email_field_id", self.email_field_id, email_text)

    def enter_telephone(self, telephone_text):
        self.type_into_element("telephone_field_id", self.telephone_field_id, telephone_text)

    def enter_password(self, password_text):
        self.type_into_element("password_field_id", self.password_field_id, password_text)

    def enter_password_confirm(self, password_confirm_text):
        self.type_into_element("password_confirm_field_id", self.confirm_password_field_id, password_confirm_text)

    def select_agree_checkbox_field(self):
        self.click_on_element("agree_field_name", self.agree_field_name)

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def select_yes_radio_button(self):
        self.click_on_element("yes_radio_button_xpath", self.yes_radio_button_xpath)

    def register_an_account(self, **user_data):
        field_methods = {
            'first_name': self.enter_first_name,
            'last_name': self.enter_last_name,
            'email': self.enter_email,
            'telephone': self.enter_telephone,
            'password': self.enter_password,
            'password_confirm': self.enter_password_confirm,
        }

        for field, method in field_methods.items():
            if field in user_data:
                method(user_data[field])

        if user_data.get('yes_or_no') == 'yes':
            self.select_yes_radio_button()

        if user_data.get('privacy_policy') == 'select':
            self.select_agree_checkbox_field()

    def retrieve_duplicate_email_warning(self, expected_warning_text):
        return self.retrieved_element_text_contains(
            "duplicate_email_warning_xpath", self.duplicate_email_warning_xpath, expected_warning_text
        )

    def display_status_of_all_warning_messages(
        self,
        expected_privacy_warning,
        expected_first_name_warning,
        expected_last_name_warning,
        expected_email_warning,
        expected_telephone_warning,
        expected_password_warning,
    ):
        privacy_status = self.retrieved_element_text_contains(
            "privacy_policy_warning_xpath", self.privacy_policy_warning_xpath, expected_privacy_warning
        )
        first_name_status = self.retrieved_element_text_equals(
            "first_name_warning_xpath", self.first_name_warning_xpath, expected_first_name_warning
        )
        last_name_status = self.retrieved_element_text_equals(
            "last_name_warning_xpath", self.last_name_warning_xpath, expected_last_name_warning
        )
        email_status = self.retrieved_element_text_equals(
            "email_warning_xpath", self.email_warning_xpath, expected_email_warning
        )
        telephone_status = self.retrieved_element_text_equals(
            "telephone_warning_xpath", self.telephone_warning_xpath, expected_telephone_warning
        )
        password_status = self.retrieved_element_text_equals(
            "password_warning_xpath", self.password_warning_xpath, expected_password_warning
        )
        return self.return_and_status(
            privacy_status, first_name_status, last_name_status, email_status, telephone_status, password_status
        )
