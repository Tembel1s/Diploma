import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

from fatsecret_tests_project.data.products import product_1
from fatsecret_tests_project.schemas.schemas import frequent_foods
from fatsecret_tests_project.utils.helpers import (
    response_logging,
    response_attaching_json,
)

load_dotenv()

login = os.getenv("FATSECRET_LOGIN")
password = os.getenv("FATSECRET_PASSWORD")
user_id = os.getenv("FATSECRET_USER_ID")


def get_cookies():
    form_data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        f"ctl00$ctl11$Logincontrol1$Name": {login},
        f"ctl00$ctl11$Logincontrol1$Password": {password},
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
@allure.story("User history")
@allure.title('"Recently Eaten" tab')
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.MINOR)
def test_recently_eaten(url):
    auth_cookies_value = get_cookies()

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = requests.get(
        (f"{url}/ajax/JsonRecipeMulti.aspx?uid={user_id}&meal=1&mec=mor"),
        cookies=cookies,
    )

    response_attaching_json(response)
    response_logging(response)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    body = response.json()

    with allure.step('Check product is in "Recently Eaten" tab'):
        assert any(
            product_1.name in recipe.get("title", "")
            for recipe in body.get("recipes", [])
        )

    with allure.step("Validate response schema"):
        validate(body, schema=frequent_foods)


@allure.tag("API")
@allure.feature("API tests")
@allure.story("User history")
@allure.title('"Most Eaten" tab')
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.MINOR)
def test_most_eaten(url):
    auth_cookies_value = get_cookies()

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = requests.get(
        (f"{url}/ajax/JsonRecipeMulti.aspx?uid={user_id}&meal=1&mec=fav"),
        cookies=cookies,
    )

    response_attaching_json(response)
    response_logging(response)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    body = response.json()

    with allure.step('Check product is in "Most Eaten" tab'):
        assert any(
            product_1.name in recipe.get("title", "")
            for recipe in body.get("recipes", [])
        )

    with allure.step("Validate response schema"):
        validate(body, schema=frequent_foods)
