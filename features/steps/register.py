from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.utils import get_new_email_with_timestamp


@given(u'I navigate to register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://tutorialsninja.com/demo/')
    context.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    context.driver.find_element(By.LINK_TEXT, 'Register').click()


@when(u'I fill mandatory fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('John')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('Doe')
    context.driver.find_element(By.ID, 'input-email').send_keys(get_new_email_with_timestamp())
    context.driver.find_element(By.ID, 'input-telephone').send_keys('0956437895')
    context.driver.find_element(By.ID, 'input-password').send_keys('the_super_password')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('the_super_password')
    context.driver.find_element(By.NAME, 'agree').click()


@when(u'I click on continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()


@then(u'Account should be created')
def step_impl(context):
    expected_message = 'Your Account Has Been Created!'
    context.driver.find_element(By.XPATH, '//*[@id="content"]/h1').text.__eq__(expected_message)
    context.driver.quit()


@when(u'I fill all fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('Octavius')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('Mcconnell')
    context.driver.find_element(By.ID, 'input-email').send_keys(get_new_email_with_timestamp())
    context.driver.find_element(By.ID, 'input-telephone').send_keys('0856437895')
    context.driver.find_element(By.ID, 'input-password').send_keys('the_super_password_2')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('the_super_password_2')
    context.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value="1"]').click()
    context.driver.find_element(By.NAME, 'agree').click()


@when(u'I fill all fields except email field')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('Aurelia')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('Mcclain')
    context.driver.find_element(By.ID, 'input-telephone').send_keys('0756437895')
    context.driver.find_element(By.ID, 'input-password').send_keys('the_super_password_3')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('the_super_password_3')
    context.driver.find_element(By.NAME, 'newsletter').click()
    context.driver.find_element(By.NAME, 'agree').click()


@when(u'I fill an existing amail address into the email field')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('aziguy_one@gmail.com')


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning_message = 'Warning: E-Mail Address is already registered!'
    assert context.driver.find_element(By.XPATH, '//*[@id="account-register"]/div[1]').text.__contains__(
        expected_warning_message
    )
    context.driver.quit()


@when(u'I don\'t fill any fields')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys('')
    context.driver.find_element(By.ID, 'input-lastname').send_keys('')
    context.driver.find_element(By.ID, 'input-telephone').send_keys('')
    context.driver.find_element(By.ID, 'input-password').send_keys('')
    context.driver.find_element(By.ID, 'input-confirm').send_keys('')


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    expected_privacy_warning_message = 'Warning: You must agree to the Privacy Policy!'
    expected_firstname_warning_message = 'First Name must be between 1 and 32 characters!'
    expected_lastname_warning_message = 'Last Name must be between 1 and 32 characters!'
    expected_email_warning_message = 'E-Mail Address does not appear to be valid!'
    expected_telephone_warning_message = 'Telephone must be between 3 and 32 characters!'
    expected_pwd_warning_message = 'Password must be between 4 and 20 characters!'
    assert context.driver.find_element(By.XPATH, '//*[@id="account-register"]/div[1]').text.__contains__(
        expected_privacy_warning_message
    )
    assert context.driver.find_element(By.XPATH, '//*[@id="account"]/div[2]/div/div').text.__eq__(
        expected_firstname_warning_message
    )
    assert context.driver.find_element(By.XPATH, '//*[@id="account"]/div[3]/div/div').text.__eq__(
        expected_lastname_warning_message
    )
    assert context.driver.find_element(By.XPATH, '//*[@id="account"]/div[4]/div/div').text.__eq__(
        expected_email_warning_message
    )
    assert context.driver.find_element(By.XPATH, '//*[@id="account"]/div[5]/div/div').text.__eq__(
        expected_telephone_warning_message
    )
    assert context.driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[2]/div[1]/div/div').text.__eq__(
        expected_pwd_warning_message
    )
    context.driver.quit()
