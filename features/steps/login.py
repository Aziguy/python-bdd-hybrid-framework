from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.utils import get_new_email_with_timestamp


@given(u'I navigated to login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
    context.driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('aziguy_one@gmail.com')
    context.driver.find_element(By.ID, 'input-password').send_keys('secure_password_one')


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()


@then(u'I should get logged in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'Edit your account information').is_displayed()
    context.driver.quit()


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys(get_new_email_with_timestamp())
    context.driver.find_element(By.ID, 'input-password').send_keys('secure_password_one')


@then(u'I should get a proper warning message')
def step_impl(context):
    expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.driver.find_element(By.XPATH, '//*[@id="account-login"]/div[1]').text.__contains__(
        expected_warning_message
    )
    context.driver.quit()


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('aziguy_one@gmail.com')
    context.driver.find_element(By.ID, 'input-password').send_keys('secure_password_one_false')


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys(get_new_email_with_timestamp())
    context.driver.find_element(By.ID, 'input-password').send_keys('secure_password_one_false')


@then(u'I should get proper warning message')
def step_impl(context):
    expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.driver.find_element(By.XPATH, '//*[@id="account-login"]/div[1]').text.__contains__(
        expected_warning_message
    )
    context.driver.quit()


@when(u'I don\'t enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('')
    context.driver.find_element(By.ID, 'input-password').send_keys('')
