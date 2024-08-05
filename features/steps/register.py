from behave import *
from features.pages.HomePage import HomePage
from utilities.utils import get_new_email_with_timestamp


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.register_an_account(
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=get_new_email_with_timestamp(),
            telephone=row["telephone"],
            password=row["password"],
            password_confirm=row["password"],
            yes_or_no='no',
            privacy_policy='select',
        )


@when(u'I click on Continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_on_continue_button()


@then(u'Account should be created')
def step_impl(context):
    assert context.account_success_page.display_status_of_account_created_heading("Your Account Has Been Created!")


@when(u'I enter below details into all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.register_an_account(
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=get_new_email_with_timestamp(),
            telephone=row["telephone"],
            password=row["password"],
            password_confirm=row["password"],
            yes_or_no='yes',
            privacy_policy='select',
        )


@when(u'I enter details into all fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.register_an_account(
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=get_new_email_with_timestamp(),
            telephone=row["telephone"],
            password=row["password"],
            password_confirm=row["password"],
            yes_or_no='no',
            privacy_policy='select',
        )


@when(u'I fill an existing email address as "{email}" into the email field')
def step_impl(context, email):
    context.register_page.enter_email(email)


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    assert context.register_page.retrieve_duplicate_email_warning("Warning: E-Mail Address is already registered!")


@when(u'I don\'t fill any fields')
def step_impl(context):
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
