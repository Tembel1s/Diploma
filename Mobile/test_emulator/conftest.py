import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
import os
from appium import webdriver
import allure
from utils import attach_mob


# @pytest.fixture(scope='session', autouse=True)
# def load_env():
#     load_dotenv()
#
#
# @pytest.fixture(scope='function', autouse=True)
# def mobile_management():
#     with allure.step('Configurate options'):
#         options = UiAutomator2Options().load_capabilities({
#             "platformName": "android",
#             "udid": "emulator-5554",
#             "appWaitActivity": "com.fatsecret.android.*",
#             "app": "/Users/tembelis/PycharmProjects/Diploma/com.fatsecret.android-702.apk",
#
#
#             'autoGrantPermissions': 'true',
#         })
#
#     with allure.step('init app session'):
#         browser.config.driver = webdriver.Remote(os.getenv('LOCAL_URL'),
#                                                  options=options)
#         browser.config.timeout = float(os.getenv("TIMEOUT"))
#
#     yield
#
#     # attach.add_screenshot(browser)
#     # attach.add_xml(browser)
#     # attach.add_video(browser)
#
#     with allure.step('Close app session'):
#         browser.quit()


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
    assert os.getenv("BROWSERSTACK_USER_NAME") is not None, "BROWSERSTACK_USER_NAME not set in environment"
    assert os.getenv("BROWSERSTACK_ACCESS_KEY") is not None, "BROWSERSTACK_ACCESS_KEY not set in environment"


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    user_name = os.getenv("BROWSERSTACK_USER_NAME")
    access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://a778d0672f42cd670a9ad09b06c508e2827d7447",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": user_name,
            "accessKey": access_key,
        }
    })

    browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)

    browser.config.timeout = float(os.getenv("TIMEOUT"))

    yield

    attach_mob.add_screenshot(browser)
    attach_mob.add_xml(browser)
    attach_mob.add_video(browser)

    browser.quit()




