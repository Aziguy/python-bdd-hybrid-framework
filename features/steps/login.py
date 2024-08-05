from behave import *
from features.pages.HomePage import HomePage
from utilities.utils import get_new_email_with_timestamp


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_login_credentials(email, password)


@when(u'I click on login button')
def step_impl(context):
    context.account_page = context.login_page.click_on_login_button()


@then(u'I should get logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_account_info_option()


@when(u'I enter invalid email as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_login_credentials(email=get_new_email_with_timestamp(), password=password)


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.login_page.display_status_of_warning_message(expected_warning_message)


@when(u'I enter valid email as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_login_credentials(email, password)


@when(u'I enter invalid email as "{email}" and invalid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_login_credentials(email=get_new_email_with_timestamp(), password=password)


@then(u'I should get proper warning message')
def step_impl(context):
    expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.login_page.display_status_of_warning_message(expected_warning_message)


@when(u'I don\'t enter anything into email and password fields')
def step_impl(context):
    context.login_page.enter_login_credentials('', '')
