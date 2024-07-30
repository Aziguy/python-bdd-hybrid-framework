from behave import *

@given(u'I navigate to register page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I navigate to register page')


@when(u'I fill mandatory fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill mandatory fields')


@when(u'I click on continue button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on continue button')


@then(u'Account should be created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Account should be created')


@when(u'I fill all fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill all fields')


@when(u'I fill all fields except email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill all fields except email field')


@when(u'I fill an existing amail address into the email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill an existing amail address into the email field')


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning message informing about duplicate account should be displayed')


@when(u'I don\'t fill any fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I don\'t fill any fields')


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning message for every mandatory fields should be displayed')
