__author__ = 'orieken'
from behave import *
import requests
from hamcrest import *
import json


@when(u'I request one user')
def step_impl(context):
    url = 'http://derp-bear-users-api.herokuapp.com/users/1'
    response = requests.get(url)
    context.status_code = response.status_code
    context.response = json.loads(response.text)


@then(u'I be returned one user')
def step_impl(context):
    assert_that(context.status_code, is_(equal_to(200)))
    assert_that(context.response['first_name'], is_(equal_to('Jarod')))
    assert_that(context.response['last_name'], is_(equal_to('Adair')))
