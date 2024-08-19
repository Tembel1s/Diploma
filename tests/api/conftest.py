import os

import pytest
import requests
from dotenv import load_dotenv

from fatsecret_tests_project.utils.helpers import (
    response_attaching_html,
    response_logging,
)

load_dotenv()

valid_login = os.getenv("FATSECRET_LOGIN")
valid_password = os.getenv("FATSECRET_PASSWORD")
user_name = os.getenv("FATSECRET_USER_NAME")
user_id = os.getenv("FATSECRET_USER_ID")


@pytest.fixture(scope="function", autouse=True)
def url():
    return "https://www.fatsecret.com"


@pytest.fixture(scope="function", autouse=True)
def get_cookies(url):
    form_data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        f"ctl00$ctl11$Logincontrol1$Name": {valid_login},
        f"ctl00$ctl11$Logincontrol1$Password": {valid_password},
    }

    response = requests.post(
        f"{url}/Auth.aspx?pa=s",
        data=form_data,
        allow_redirects=False,
    )
    auth_cookie_value = response.cookies.get(".FSASPXAUTH")

    return auth_cookie_value


@pytest.fixture(scope="function", autouse=True)
def api_request_html():
    def _api_request_html(
        base_api_url, endpoint, method, data=None, params=None, cookies=None
    ):
        url = f"{base_api_url}{endpoint}"
        if params is None:
            params = {}
        response = requests.request(
            method,
            url,
            data=data,
            params=params,
            cookies=cookies,
            allow_redirects=params.get("allow_redirects", True),
        )
        response_logging(response)
        response_attaching_html(response)
        return response

    return _api_request_html


@pytest.fixture(scope="function", autouse=True)
def api_request_json():
    def _api_request_json(
        base_api_url, endpoint, method, data=None, params=None, cookies=None
    ):
        url = f"{base_api_url}{endpoint}"
        if params is None:
            params = {}
        response = requests.request(
            method,
            url,
            data=data,
            params=params,
            cookies=cookies,
            allow_redirects=params.get("allow_redirects", True),
        )
        response_logging(response)
        response_attaching_html(response)
        return response

    return _api_request_json
