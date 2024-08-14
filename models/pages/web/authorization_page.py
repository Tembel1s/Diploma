from selene import browser
from selene import have, be
import os
from dotenv import load_dotenv
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

user_name = os.getenv('FATSECRET_USER_NAME')


class AuthorizationPage:

    @allure.step('Open browser')
    def open(self):
        browser.open('/')

    @allure.step('Click "Sign In" button')
    def click_sign_in_button(self):
        browser.element('[href="/Auth.aspx?pa=s"]').should(be.clickable).click()

    @allure.step('Fill login')
    def fill_login(self, login):
        browser.element('#ctl11_Logincontrol1_Name').type(login)

    @allure.step('Fill password')
    def fill_password(self, password):
        browser.element('#ctl11_Logincontrol1_Password').type(password)

    @allure.step('Submit credentials')
    def submit_credentials(self):
        browser.element('#ctl11_Logincontrol1_Login').should(be.clickable).click()

    @allure.step('Check successful authorization')
    def check_successful_authorization(self):
        browser.element(f'[href="/member/{user_name}"]').should(have.text(f'Hello {user_name}'))

    @allure.step('Check unsuccessful authorization')
    def check_unsuccessful_authorization(self):
        alert = WebDriverWait(browser.driver, 10).until(EC.alert_is_present())

        assert 'Login failed.' in alert.text
