from behave import *
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'I am on home page screen')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_home_page_title("Your Store")


@when(u'I enter valid product into the search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field('HP')


@when(u'I click on Search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()


@then(u'Valid product should get display in search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.display_status_of_product()


@when(u'I enter invalid product into the search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field('Honda')


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.display_status_of_message("There is no product that matches the search criteria.")


@when(u'I don\'t enter any term into search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")
