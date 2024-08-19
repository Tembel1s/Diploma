import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv

from fatsecret_tests_project.utils.helpers import response_attaching_html, response_logging

load_dotenv()

valid_login = os.getenv("FATSECRET_LOGIN")
valid_password = os.getenv("FATSECRET_PASSWORD")
user_name = os.getenv("FATSECRET_USER_NAME")
user_id = os.getenv("FATSECRET_USER_ID")


def get_cookies():
    form_data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        f"ctl00$ctl11$Logincontrol1$Name": {valid_login},
        f"ctl00$ctl11$Logincontrol1$Password": {valid_password},
    }

    response = requests.post(
        "https://www.fatsecret.com/Auth.aspx?pa=s",
        data=form_data,
        allow_redirects=False,
    )
    auth_cookie_value = response.cookies.get(".FSASPXAUTH")

    return auth_cookie_value


@allure.tag("API")
@allure.feature("API tests")
@allure.story("Authorization")
@allure.title("Successful authorization")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.BLOCKER)
def test_authorization(url):
    form_data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        "ctl00$ctl11$Logincontrol1$Name": f"{valid_login}",
        "ctl00$ctl11$Logincontrol1$Password": f"{valid_password}",
    }

    response_before_redirect = requests.post(
        f"{url}/Auth.aspx?pa=s", data=form_data, allow_redirects=False
    )

    with allure.step("Check Status Code = 302"):
        assert response_before_redirect.status_code == 302

    with allure.step("Check getting Auth-cookies from server"):
        assert ".FSASPXAUTH" in response_before_redirect.cookies

    response = requests.post(
        f"{url}/Auth.aspx?pa=s", data=form_data, allow_redirects=True
    )

    response_attaching_html(response)
    response_logging(response)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    with allure.step("Check successful authorization"):
        assert f"Hello {user_name}" in response.text


@allure.tag("API")
@allure.feature("API tests")
@allure.story("Authorization")
@allure.title("Unsuccessful authorization (wrong login)")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_authorization_wrong_password(url):
    form_data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        "ctl00$ctl11$Logincontrol1$Name": f"{valid_login}",
        "ctl00$ctl11$Logincontrol1$Password": "invalid_password",
    }

    response = requests.post(
        f"{url}/Auth.aspx?pa=s",
        data=form_data,
    )

    response_attaching_html(response)
    response_logging(response)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    with allure.step("Check not getting Auth-cookies from server"):
        assert ".FSASPXAUTH" not in response.cookies

    with allure.step("Check unsuccessful authorization"):
        assert "Sign in to your FatSecret account" in response.text
