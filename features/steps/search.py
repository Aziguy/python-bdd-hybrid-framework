from behave import *


@given(u'I am on home page screen')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on home page screen')


@when(u'I enter valid product into the search box field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid product into the search box field')


@when(u'I click on Search button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on Search button')


@then(u'Valid product should get display in search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Valid product should get display un search results')


@when(u'I enter invalid product into the search box field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid product into the search box field')


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper message should be displayed in search results')


@when(u'I don\'t enter any term into search box field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I don\'t enter anything into search box field')
