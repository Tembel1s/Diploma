import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from Models.pages.web.user_actions_page import AddFood, DeleteFood


@pytest.fixture(scope="function", autouse=True)
def browser_management(request):
    browser.config.base_url = "https://fatsecret.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options

    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    CONTENT_DIR = os.path.abspath('content_folder')

    if 'test_authorization' not in request.fspath.basename:
        os.makedirs('content_folder', exist_ok=True)
        CONTENT_DIR = os.path.abspath('content_folder')

        prefs = {
            "download.default_directory": CONTENT_DIR,
            "plugins.always_open_pdf_externally": True
        }
        driver_options.add_experimental_option("prefs", prefs)

    yield

    if 'test_authorization' not in request.fspath.basename:
        add_food = AddFood()
        delete_food = DeleteFood()

        add_food.go_to_food_diary()
        delete_food.clear_diary()
        shutil.rmtree(CONTENT_DIR)

    browser.quit()
