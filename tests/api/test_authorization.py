import os

import allure
from allure_commons.types import Severity
from dotenv import load_dotenv

load_dotenv()

valid_login = os.getenv("FATSECRET_LOGIN")
valid_password = os.getenv("FATSECRET_PASSWORD")
user_name = os.getenv("FATSECRET_USER_NAME")
user_id = os.getenv("FATSECRET_USER_ID")


@allure.tag("API")
@allure.feature("API tests")
@allure.story("Authorization")
@allure.title("Successful authorization")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.BLOCKER)
def test_authorization(url, api_request):
    data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        "ctl00$ctl11$Logincontrol1$Name": f"{valid_login}",
        "ctl00$ctl11$Logincontrol1$Password": f"{valid_password}",
    }
    params = {
        'allow_redirects': False
    }
    response_before_redirect = api_request(url, endpoint="/Auth.aspx?pa=s", method="POST", data=data,
                                                params=params)
    with allure.step("Check Status Code = 302"):
        assert response_before_redirect.status_code == 302
    with allure.step("Check getting Auth-cookies from server"):
        assert ".FSASPXAUTH" in response_before_redirect.cookies

    response_after_redirect = api_request(url, endpoint="/Auth.aspx?pa=s", method="POST", data=data)
    with allure.step("Check Status Code = 200"):
        assert response_after_redirect.status_code == 200
    with allure.step("Check successful authorization"):
        assert f"Hello {user_name}" in response_after_redirect.text


@allure.tag("API")
@allure.feature("API tests")
@allure.story("Authorization")
@allure.title("Unsuccessful authorization (wrong login)")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_authorization_wrong_password(url, api_request):
    data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        "ctl00$ctl11$Logincontrol1$Name": f"{valid_login}",
        "ctl00$ctl11$Logincontrol1$Password": "invalid_password",
    }

    response = api_request(url, endpoint="/Auth.aspx?pa=s", method="POST", data=data)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    with allure.step("Check not getting Auth-cookies from server"):
        assert ".FSASPXAUTH" not in response.cookies

    with allure.step("Check unsuccessful authorization"):
        assert "Sign in to your FatSecret account" in response.text
