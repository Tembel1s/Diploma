import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

valid_login = os.getenv("FATSECRET_LOGIN")
valid_password = os.getenv("FATSECRET_PASSWORD")
user_name = os.getenv("FATSECRET_USER_NAME")
user_id = os.getenv("FATSECRET_USER_ID")


@pytest.fixture(scope="function", autouse=True)
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


@pytest.fixture(scope="function", autouse=True)
def url():
    return "https://www.fatsecret.com"
