import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
import os
from appium import webdriver
import allure
from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    with allure.step('Configurate options'):
        options = UiAutomator2Options().load_capabilities({
            "platformName": "android",
            "udid": "emulator-5554",
            "appWaitActivity": "com.fatsecret.android.*",
            # "app": "/Users/tembelis/PycharmProjects/qa_guru_python_13_19/base.apk",
            "app": "/Users/tembelis/PycharmProjects/Diploma/com.fatsecret.android-702.apk",


            'autoGrantPermissions': 'true',
        })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(os.getenv('LOCAL_URL'),
                                                 options=options)
        browser.config.timeout = float(os.getenv("TIMEOUT"))

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    # attach.add_video(browser)

    with allure.step('Close app session'):
        browser.quit()
