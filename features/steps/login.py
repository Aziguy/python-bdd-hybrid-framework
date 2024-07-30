from behave import *


@given(u'I navigated to login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigated to login page')


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email and valid password into the fields')


@when(u'I click on login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on login button')


@then(u'I should get logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get logged in')


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid email and valid password into the fields')


@then(u'I should get a proper warning message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get a proper warning message')


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email and invalid password into the fields')


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter invalid email and invalid password into the fields')


@then(u'I should get proper warning message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get proper warning message')


@when(u'I don\'t enter anything into email and password fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I don\'t enter anything into email and password fields')
