from behave import *
from selenium.webdriver.common.by import By
from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage
from utilities.utils import get_new_email_with_timestamp


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when(u'I fill mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.register_an_account(
        first_name='John',
        last_name='Doe',
        email=get_new_email_with_timestamp(),
        telephone='0123456789',
        password='the_super_password',
        password_confirm='the_super_password',
        yes_or_no='no',
        privacy_policy='select',
    )


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.click_on_continue_button()


@then(u'Account should be created')
def step_impl(context):
    context.account_success_page = AccountSuccessPage(context.driver)
    assert context.account_success_page.display_status_of_account_created_heading("Your Account Has Been Created!")


@when(u'I fill all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.register_an_account(
        first_name='John',
        last_name='Doe',
        email=get_new_email_with_timestamp(),
        telephone='0123456789',
        password='the_super_password',
        password_confirm='the_super_password',
        yes_or_no='yes',
        privacy_policy='select',
    )


@when(u'I fill all fields except email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.register_an_account(
        first_name='John',
        last_name='Doe',
        email='',
        telephone='0123456789',
        password='the_super_password',
        password_confirm='the_super_password',
        yes_or_no='no',
        privacy_policy='select',
    )


@when(u'I fill an existing amail address into the email field')
def step_impl(context):
    context.register_page.enter_email("aziguy_one@gmail.com")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    assert context.register_page.retrieve_duplicate_email_warning("Warning: E-Mail Address is already registered!")


@when(u'I don\'t fill any fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.register_an_account(
        first_name='',
        last_name='',
        email='',
        telephone='',
        password='',
        password_confirm='',
        yes_or_no='no',
        privacy_policy='no',
    )


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    assert context.register_page.display_status_of_all_warning_messages(
        "Warning: You must agree to the Privacy Policy!",
        "First Name must be between 1 and 32 characters!",
        "Last Name must be between 1 and 32 characters!",
        "E-Mail Address does not appear to be valid!",
        "Telephone must be between 3 and 32 characters!",
        "Password must be between 4 and 20 characters!",
    )
