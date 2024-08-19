import os

import allure
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

from fatsecret_tests_project.data.products import product_1
from fatsecret_tests_project.schemas.schemas import frequent_foods

load_dotenv()

login = os.getenv("FATSECRET_LOGIN")
password = os.getenv("FATSECRET_PASSWORD")
user_id = os.getenv("FATSECRET_USER_ID")


@allure.tag("API")
@allure.feature("API tests")
@allure.story("User history")
@allure.title('"Recently Eaten" tab')
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.MINOR)
def test_recently_eaten(url, get_cookies, api_request_json):
    auth_cookies_value = get_cookies

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = api_request_json(
        url,
        endpoint=f'/ajax/JsonRecipeMulti.aspx?uid={user_id}&meal=1&mec=mor',
        method='POST',
        cookies=cookies
    )

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
def test_most_eaten(url, get_cookies, api_request_json):
    auth_cookies_value = get_cookies

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = api_request_json(
        url,
        endpoint=f'/ajax/JsonRecipeMulti.aspx?uid={user_id}&meal=1&mec=fav',
        method='POST',
        cookies=cookies
    )

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
