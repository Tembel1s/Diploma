import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fatSecret_tests_project.pages.web.user_actions_page import AddFood, DeleteFood
from fatSecret_tests_project.utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    if "skip_setup_browser" in request.keywords:
        yield
    else:
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.config.base_url = "https://www.fatsecret.com"

        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "126.0",
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }

        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--incognito")

        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options,
        )

        browser.config.driver = driver

        yield

        if "accept_alert" in request.keywords:
            browser.driver.switch_to.alert.accept()
        attach.add_screenshot()
        attach.add_video_web()
        attach.add_logs()

        if "test_authorization" not in request.fspath.basename:
            add_food = AddFood()
            delete_food = DeleteFood()

            add_food.go_to_food_diary()
            delete_food.clear_diary()

        browser.quit()
