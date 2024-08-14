import requests
from jsonschema import validate
from schemas.schemas import upload_photo, frequent_foods
import os
from dotenv import load_dotenv
import allure
from allure_commons.types import Severity
from utils.helpers import (
    response_logging,
    response_attaching_html,
    response_attaching_json,
)

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
@allure.story("User actions")
@allure.title("View user profile")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_view_user_profile(url):
    auth_cookies_value = get_cookies()

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = requests.get((f"{url}/member/{user_name}"), cookies=cookies)

    response_attaching_html(response)
    response_logging(response)

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
def test_fill_bio(url):
    auth_cookies_value = get_cookies()
    text = "kak dela"

    form_data = {"__EVENTTARGET": "ctl00$ctl11$ctl04", "ctl00$ctl11$Bio": f"{text}"}

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = requests.post(
        f"{url}/Default.aspx?pa=mbe", data=form_data, cookies=cookies
    )

    response_attaching_html(response)
    response_logging(response)

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
def test_upload_photo(url):
    import base64

    auth_cookies_value = get_cookies()

    current_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_dir, "images", "image.jpg")

    def image_to_base64(image_path):
        with open(file_path, "rb") as image_file:
            image_data = image_file.read()

            base64_encoded = base64.b64encode(image_data).decode("utf-8")
            return base64_encoded

    base64_image = image_to_base64(file_path)

    payload = {
        "image": base64_image,
        "target": "300",
        "maxWidth": "650",
        "suffix": "prof",
    }

    cookies = {
        ".FSASPXAUTH": f"{auth_cookies_value}",
    }

    response = requests.post(
        f"{url}/ajax/ImageUpload.aspx", data=payload, cookies=cookies
    )

    response_attaching_json(response)
    response_logging(response)

    body = response.json()

    with allure.step("Check Status Code = 200"):
        assert response.status_code == 200

    with allure.step("Check successful upload"):
        assert body.get("success", {}).get("value") == "True"

    with allure.step("Validate response schema"):
        validate(body, schema=upload_photo)
