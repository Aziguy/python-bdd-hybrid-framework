from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I am on home page screen')
def step_impl(context):
    expected_title = 'Your Store'
    assert context.driver.title.__eq__(expected_title)


@when(u'I enter valid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('HP')


@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()


@then(u'Valid product should get display in search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()


@when(u'I enter invalid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('Honda')


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    expected_message = 'Products meeting the search criteria'
    assert context.driver.find_element(By.XPATH, '//*[@id="content"]/h2').text.__eq__(expected_message)


@when(u'I don\'t enter any term into search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('')
