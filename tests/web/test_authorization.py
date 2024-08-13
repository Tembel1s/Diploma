import time
from Models.pages.web.authorization_page import AuthorizationPage
import os
from dotenv import load_dotenv
import allure
from allure_commons.types import Severity

load_dotenv()

valid_login = os.getenv('VALID_LOGIN')
valid_password = os.getenv('VALID_PASSWORD')

@allure.tag('UI')
@allure.feature('UI tests')
@allure.story('Authorization')
@allure.title('Successful authorization')
@allure.link('https://fatsecret.com/')
@allure.severity(Severity.BLOCKER)
def test_authorization():
    authorization_page = AuthorizationPage()

    authorization_page.open()
    authorization_page.click_sign_in_button()

    time.sleep(2)

    authorization_page.fill_login(valid_login)
    time.sleep(2)
    authorization_page.fill_password(valid_password)

    time.sleep(2)

    authorization_page.submit_credentials()
    time.sleep(2)
    authorization_page.check_successful_authorization()

@allure.tag('UI')
@allure.feature('UI tests')
@allure.story('Authorization')
@allure.title('Unsuccessful authorization (wrong password)')
@allure.link('https://fatsecret.com/')
@allure.severity(Severity.CRITICAL)
def test_authorization_invalid_password():
    authorization_page = AuthorizationPage()

    authorization_page.open()
    time.sleep(2)
    authorization_page.click_sign_in_button()

    time.sleep(2)

    authorization_page.fill_login(valid_login)
    time.sleep(2)
    authorization_page.fill_password('invalid password')
    time.sleep(2)
    authorization_page.submit_credentials()

    time.sleep(2)

    authorization_page.check_unsuccessful_authorization()


@allure.tag('UI')
@allure.feature('UI tests')
@allure.story('Authorization')
@allure.title('Unsuccessful authorization (wrong login)')
@allure.link('https://fatsecret.com/')
@allure.severity(Severity.CRITICAL)
def test_authorization_wrong_login():
    authorization_page = AuthorizationPage()

    authorization_page.open()
    time.sleep(2)
    authorization_page.click_sign_in_button()

    time.sleep(2)
    authorization_page.fill_login('invalid login')
    time.sleep(2)
    authorization_page.fill_password(valid_password)

    time.sleep(2)
    authorization_page.submit_credentials()

    time.sleep(2)

    authorization_page.check_unsuccessful_authorization()
    time.sleep(2)
