import base64
import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

from fatsecret_tests_project.schemas.schemas import upload_photo
from fatsecret_tests_project.utils.file_path import relative_path

load_dotenv()

valid_login = os.getenv("FATSECRET_LOGIN")
valid_password = os.getenv("FATSECRET_PASSWORD")
user_name = os.getenv("FATSECRET_USER_NAME")
user_id = os.getenv("FATSECRET_USER_ID")

file_path = relative_path('tests/api/images/image.jpg')


def image_to_base64(image_path):
    with open(file_path, "rb") as image_file:
        image_data = image_file.read()

        base64_encoded = base64.b64encode(image_data).decode("utf-8")
        return base64_encoded


base64_image = image_to_base64(file_path)


@allure.tag("API")
@allure.feature("API tests")
@allure.story("User actions")
@allure.title("View user profile")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_view_user_profile(url, get_cookies, api_request_html):
    auth_cookies_value = get_cookies

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = api_request_html(url, endpoint=f"/member/{user_name}", method="GET", cookies=cookies)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    with allure.step("Check User data are in response"):
        assert f"FatSecret member: {user_name}" in response.text

    with allure.step('Check "My Weight History" title is in response'):
        assert "My Weight History" in response.text


@allure.tag("API")
@allure.feature("API tests")
@allure.story("User actions")
@allure.title("Fill Bio")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_fill_bio(url, get_cookies, api_request_html):
    auth_cookies_value = get_cookies
    text = "kak dela"

    data = {"__EVENTTARGET": "ctl00$ctl11$ctl04", "ctl00$ctl11$Bio": f"{text}"}

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = api_request_html(url, endpoint="/Default.aspx?pa=mbe", method="POST", data=data, cookies=cookies)

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    response = requests.get(f"{url}/Default.aspx?pa=mbe", cookies=cookies)

    with allure.step("Check filled text is in Bio"):
        assert text in response.text


@allure.tag("API")
@allure.feature("API tests")
@allure.story("User actions")
@allure.title("Upload photo")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.MINOR)
def test_upload_photo(url, get_cookies, api_request_json):
    auth_cookies_value = get_cookies

    data = {
        "image": base64_image,
        "target": "300",
        "maxWidth": "650",
        "suffix": "prof",
    }

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = api_request_json(url, endpoint="/ajax/ImageUpload.aspx", method="POST", data=data, cookies=cookies)

    body = response.json()

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    with allure.step("Check successful upload"):
        assert body.get("success", {}).get("value") == "True"

    with allure.step("Validate response schema"):
        validate(body, schema=upload_photo)
