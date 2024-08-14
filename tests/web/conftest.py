import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from models.pages.web.user_actions_page import AddFood, DeleteFood


@pytest.fixture(scope="function", autouse=True)
def browser_management(request):
    browser.config.base_url = "https://fatsecret.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options

    yield

    if "test_authorization" not in request.fspath.basename:
        add_food = AddFood()
        delete_food = DeleteFood()

        add_food.go_to_food_diary()
        delete_food.clear_diary()

    browser.quit()


# import os
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selene import browser
# from dotenv import load_dotenv
# from models.pages.web.user_actions_page import AddFood, DeleteFood
# from utils import attach
#
#
# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope="function", autouse=True)
# def setup_browser(request):
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     browser.config.base_url = "https://www.fatsecret.com"
#
#     options = Options()
#     selenoid_capabilities = {
#         "browserName": "chrome",
#         "browserVersion": "126.0",
#         "selenoid:options": {
#             "enableVNC": True,
#             "enableVideo": True
#         }
#     }
#
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--incognito")
#
#     selenoid_login = os.getenv("SELENOID_LOGIN")
#     selenoid_pass = os.getenv("SELENOID_PASS")
#     selenoid_url = os.getenv("SELENOID_URL")
#
#     options.capabilities.update(selenoid_capabilities)
#     driver = webdriver.Remote(
#         command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
#         options=options)
#
#     browser.config.driver = driver
#
#     yield
#
#     attach.add_screenshot()
#     attach.add_xml()
#     attach.add_video_web()
#     attach.add_logs()
#
#
#     if 'test_authorization' not in request.fspath.basename:
#         add_food = AddFood()
#         delete_food = DeleteFood()
#
#         add_food.go_to_food_diary()
#         delete_food.clear_diary()
#
#     browser.quit()
